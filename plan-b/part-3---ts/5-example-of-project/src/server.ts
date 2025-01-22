
import express from 'express'

import {MyDataBase, DataEntry} from './MyDataBase'



const app = express();
const port = 3000;


const myDataBase = new MyDataBase();



// middleware
app.use((req, res, next) => {
  // log the request
  console.log('new request', req.path);

  // -> much smarter stuff can happen here:
  // ----> actual logging
  // ----> authentication
  // ----> etc.

  next(); // we're done here, let's keep going
});


// expose the public folder's content
app.use(express.static('./public'));


app.get('/list', async (req, res) => {

  const allData: DataEntry[] = await myDataBase.list();

  res.json({ allData });

});

app.get('/add-new', async (req, res) => {

  await myDataBase.insert({
    firstName: 'john',
    lastName: 'doe',
    age: 40
  });

  res.writeHead(200); // 200 -> success
  res.end();

});



const start = async () => {

  await myDataBase.initialize();

  await myDataBase.insert({
    firstName: 'john',
    lastName: 'doe',
    age: 40
  });

  app.listen(port, () => {
    console.log(`Example app listening on port ${port}`);
  });

};
start();

