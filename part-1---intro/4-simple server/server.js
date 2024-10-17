
const express = require('express')
const app = express()
const port = 3000


let counter = 1;

app.get('/', (req, res) => {
  res.send(`Hello World! (${counter})`);
  counter += 1;
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});
