

// callbacks way
// -> a lot of javascript code use callback function

setTimeout(() => {

  console.log("hello");

}, 500);



// "callback HELL"

setTimeout(() => {

  // after 500ms

  console.log("hello");

  setTimeout(() => {

    // after 500ms

    console.log("world");

    setTimeout(() => {

      // after 500ms

      console.log("what");

      setTimeout(() => {

        // after 500ms

        console.log("a beautiful");

        setTimeout(() => {

          // after 500ms

          console.log("day");

        }, 500);

      }, 500);

    }, 500);

  }, 500);

}, 500);



// promises class to the rescue


const myAsyncSleep = (delay: number): Promise<void> => {
  return new Promise<void>((resolve) => {

    setTimeout(() => {

      resolve();

    }, delay);
  })
};

const asyncFunc = async () => {

  console.log("hello");
  await myAsyncSleep(500);
  console.log("world"); // after 500ms
  await myAsyncSleep(500);
  console.log("what"); // after 500ms
  await myAsyncSleep(500);
  console.log("a beautiful"); // after 500ms
  await myAsyncSleep(500);
  console.log("day"); // after 500ms

};
asyncFunc();








// concrete example

import * as fs from "fs"

const asyncReadFile = (filename: string) => {
  return new Promise<string>((resolve, reject) => {
    fs.readFile(filename, 'utf8', (err, data) => {
      if (err) {
        return reject(err);
      }
      resolve(data);
    });

  });
}








