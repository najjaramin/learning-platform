const mongoose = require("mongoose");
const Redis = require("ioredis");

let redisClient;

const connectMongo = async () => {
  await mongoose.connect(process.env.MONGO_URI);
  console.log("✅ MongoDB connected");
};

const connectRedis = async () => {
  redisClient = new Redis({
    host: process.env.REDIS_HOST,
    port: process.env.REDIS_PORT,
    password: process.env.REDIS_PASSWORD,
  });
  console.log("✅ Redis connected");
};

module.exports = { connectMongo, connectRedis, redisClient };