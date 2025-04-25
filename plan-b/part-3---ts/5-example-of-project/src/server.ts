
import express from 'express'

import {MyDataBase, DataEntry} from './MyDataBase'



const app = express();
const port = 5000;


const myDataBase = new MyDataBase();

// middleware
// -> log the request
app.use((req, res, next) => {
  console.log((new Date()).toISOString(), 'new request', req.path);

  // -> much smarter stuff can happen here:
  // ----> actual logging
  // ----> authentication
  // ----> etc.

  next(); // we're done here, let's keep going
});


// middleware
// -> expose the public folder's content
app.use(express.static('./public'));

// middleware
// -> this will parse the json request body of the requests POST/PUT/DELETE
app.use(express.json());


// handle request
app.get('/list-all', async (req, res) => {

  let startIndex = 0;
  if (req.query.startIndex !== undefined) {
    startIndex = parseInt(`${req.query.startIndex}`, 10);
  }

  let maxSize = 10;
  if (req.query.maxSize !== undefined) {
    maxSize = parseInt(`${req.query.maxSize}`, 10);
  }

  const allData: DataEntry[] = await myDataBase.list(startIndex, maxSize);

  // 200 -> success
  res.status(200).json({ allData });
});

// handle request
app.post('/add-new', async (req, res) => {

  //
  // firstName
  //

  if (req.body.firstName === undefined) {
    // 400 -> bad request
    res.status(400).json({ status: 400, message: "firstName is missing" });
    return; // we stop now
  }
  if (typeof(req.body.firstName) !== 'string') {
    // 400 -> bad request
    res.status(400).json({ status: 400, message: "firstName is not a string" });
    return; // we stop now
  }
  if (req.body.firstName.length === 0) {
    // 400 -> bad request
    res.status(400).json({ status: 400, message: "firstName is an empty string" });
    return; // we stop now
  }

  //
  // lastName
  //

  if (req.body.lastName === undefined) {
    // 400 -> bad request
    res.status(400).json({ status: 400, message: "lastName is missing" });
    return; // we stop now
  }
  if (typeof(req.body.lastName) !== 'string') {
    // 400 -> bad request
    res.status(400).json({ status: 400, message: "lastName is not a string" });
    return; // we stop now
  }
  if (req.body.lastName.length === 0) {
    // 400 -> bad request
    res.status(400).json({ status: 400, message: "lastName is an empty string" });
    return; // we stop now
  }

  //
  // age
  //

  if (req.body.age === undefined) {
    // 400 -> bad request
    res.status(400).json({ status: 400, message: "age is missing" });
    return; // we stop now
  }
  if (typeof(req.body.age) !== 'number' || isNaN(req.body.age)) {
    // 400 -> bad request
    res.status(400).json({ status: 400, message: "age is not a number" });
    return; // we stop now
  }
  if (req.body.age < 0) {
    // 400 -> bad request
    res.status(400).json({ status: 400, message: "age cannot be negative" });
    return; // we stop now
  }

  //
  //
  //

  await myDataBase.insert({
    firstName: req.body.firstName,
    lastName: req.body.lastName,
    age: req.body.age
  });

  // 201 -> success -? created
  res.status(201).end();
});

// handle request
app.delete('/delete-existing', async (req, res) => {

  // validate rowId
  if (req.body.rowId === undefined) {
    // 400 -> bad request
    res.status(400).json({ status: 400, message: "rowId is missing" });
    return; // we stop now
  }
  if (typeof(req.body.rowId) !== 'number') {
    // 400 -> bad request
    res.status(400).json({ status: 400, message: "rowId is not a number" });
    return; // we stop now
  }

  await myDataBase.remove(req.body.rowId);

  // 204 -> success -> deleted
  res.status(204).end();
});



const start = async () => {

  await myDataBase.initialize();

  // await myDataBase.insert({
  //   firstName: 'john',
  //   lastName: 'doe',
  //   age: 40
  // });

  app.listen(port, () => {
    console.log(`Example app listening on port ${port}`);
  });

};
start();

