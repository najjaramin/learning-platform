const User = require("../models/User");
const jwt = require("jsonwebtoken");

exports.register = async (req, res) => {
  try {
    const { firstName, lastName, email, password, role } = req.body;

    const exists = await User.findOne({ email });
    if (exists) {
      return res.status(400).json({ message: "Email already in use" });
    }

    const user = await User.create({
      firstName,
      lastName,
      email,
      password,
      role: role || "student",
    });

    res.status(201).json({
      message: "User registered successfully",
      user: user.toPublicJSON(),
    });
  } catch (err) {
    res.status(500).json({ message: "Register error", error: err.message });
  }
};

exports.login = async (req, res) => {
  try {
    const { email, password } = req.body;

    const user = await User.findOne({ email }).select("+password");
    if (!user) {
      return res.status(401).json({ message: "Invalid credentials" });
    }

    const isMatch = await user.comparePassword(password);
    if (!isMatch) {
      return res.status(401).json({ message: "Invalid credentials" });
    }

    const token = jwt.sign(
      { id: user._id, role: user.role },
      process.env.JWT_SECRET,
      { expiresIn: process.env.JWT_EXPIRES_IN }
    );

    res.json({
      token,
      user: user.toPublicJSON(),
    });
  } catch (err) {
    res.status(500).json({ message: "Login error", error: err.message });
  }
};
``