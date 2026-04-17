const express = require("express");
const Joi = require("joi");
const User = require("../models/user.model");
const { authenticate, authorize } = require("../middleware/auth");

const router = express.Router();

router.get("/profile", authenticate, (req, res) => {
  res.json({ user: req.user.toPublicJSON() });
});

router.get("/", authenticate, authorize("admin"), async (req, res) => {
  const users = await User.find();
  res.json(users.map(u => u.toPublicJSON()));
});

module.exports = router;
