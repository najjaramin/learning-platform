const express = require("express");
const jwt = require("jsonwebtoken");
const Joi = require("joi");
const User = require("../models/user.model");
const { authenticate } = require("../middleware/auth");

const router = express.Router();

const genAccess = (u) =>
  jwt.sign({ id: u._id, role: u.role }, process.env.JWT_SECRET, { expiresIn: "7d" });

const genRefresh = (u) =>
  jwt.sign({ id: u._id }, process.env.JWT_SECRET, { expiresIn: "30d" });

const registerSchema = Joi.object({
  firstName: Joi.string().required(),
  lastName: Joi.string().required(),
  email: Joi.string().email().required(),
  password: Joi.string().min(8).required(),
  idNumber: Joi.string().pattern(/^\d{8}$/).required(),
  phone: Joi.string().pattern(/^[259]\d{7}$/).required(),
  department: Joi.string().required(),
  role: Joi.string().valid("student", "instructor", "admin").default("student"),
});

router.post("/register", async (req, res) => {
  const { error, value } = registerSchema.validate(req.body);
  if (error) return res.status(400).json({ error: error.message });

  if (await User.findOne({ email: value.email }))
    return res.status(409).json({ error: "Email exists" });

  const user = await User.create(value);
  const accessToken = genAccess(user);
  const refreshToken = genRefresh(user);

  user.refreshTokens.push(refreshToken);
  await user.save();

  res.status(201).json({ user: user.toPublicJSON(), accessToken, refreshToken });
});

router.post("/login", async (req, res) => {
  const user = await User.findOne({ email: req.body.email }).select("+password");
  if (!user || !(await user.comparePassword(req.body.password)))
    return res.status(401).json({ error: "Invalid credentials" });

  const accessToken = genAccess(user);
  const refreshToken = genRefresh(user);
  user.refreshTokens.push(refreshToken);
  await user.save();

  res.json({ user: user.toPublicJSON(), accessToken, refreshToken });
});

router.post("/logout", authenticate, async (req, res) => {
  req.user.refreshTokens = [];
  await req.user.save();
  res.json({ message: "Logged out" });
});

module.exports = router;