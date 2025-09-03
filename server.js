const express = require("express");
const axios = require("axios");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(express.json()); // So we can handle JSON bodies

// Test route
app.get("/", (req, res) => {
  res.send("Frontend is running!");
});

// Fetch data from backend
app.get("/fetch-backend", async (req, res) => {
  try {
    const response = await axios.get("http://backend:5000/api/data");
    res.json(response.data);
  } catch (error) {
    res.status(500).json({ error: "Backend not reachable" });
  }
});

// Send data to backend
app.post("/send-to-backend", async (req, res) => {
  try {
    const response = await axios.post("http://backend:5000/submit", req.body);
    res.json(response.data);
  } catch (error) {
    res.status(500).json({ error: "Error sending data to backend" });
  }
});

app.listen(3000, () => {
  console.log("Frontend listening on port 3000");
});
