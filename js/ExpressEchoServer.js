const express = require("express");
const app = express(); // be sure to use the variable `app`

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

app.get("/", (req, res) => {
  const message = req.query.message;
  if (message === undefined) {
    return res.status(422).json({ error: "'message' was not provided" });
  }

  if (typeof message !== 'string') {
    return res.status(422).json({ error: "'message' was not a string" });
  }

  res.status(200).json({ message });
});

app.post("/", (req, res) => {
  const message = req.body.message;
  
  if (message === undefined) {
    return res.status(422).json({ error: "'message' was not provided" });
  }
  
  if (typeof message !== 'string') {
    return res.status(422).json({ error: "'message' was not a string" });
  }
  
  res.status(200).json({ message });
});
