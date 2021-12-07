const express = require("express");
const cors = require("cors");

const app = express();
const port = 3010;
app.use(cors());

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

app.get("/", (req, res) => {
  res.json({
    success: true,
    first_name: "Anh",
    last_name: "Le",
  });
});

app.post("/", (req, res) => {
  const { first_name, last_name } = req.body;
  res.json({
    success: true,
    first_name,
    last_name,
  });
});

app.listen(port, () => {
  console.log(
    `Example app listening at http://ec2-18-188-140-131.us-east-2.compute.amazonaws.com:${port}`
  );
});
