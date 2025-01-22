



console.log("hello!");


// get the current date-time
const currentTime = new Date();

// build the file name to save
const newFileName = "my_new_File_" + currentTime.toISOString() + ".txt";

// store the file content to save
const newFileContent =
  "the date at the create of this file was\n" + currentTime.toDateString() +
  " and the time was\n" + currentTime.toTimeString()



// get the FileSystem module -> fs
const fs = require('fs');

fs.writeFileSync(newFileName, newFileContent);


