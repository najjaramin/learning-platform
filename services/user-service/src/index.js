require("dotenv").config()
const express = require("express")
const cors = require("cors")
const { connectMongo } = require("./config/db")

const authRoutes = require("./routes/auth.routes")
const userRoutes = require("./routes/user.routes")

const app = express()
app.use(cors())
app.use(express.json())

app.use("/api/auth", authRoutes)
app.use("/api/users", userRoutes)

app.get("/health", (_, res) => res.json({ status: "ok" }))

connectMongo().then(() => {
  app.listen(8002, () =>
    console.log("✅ User Service running on port 8002")
  )
})
``