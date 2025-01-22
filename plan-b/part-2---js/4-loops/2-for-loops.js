




for (let counter = 0; counter < 10; counter = counter + 1) {
  // will run 10 times
}


// for (;;) {
//   // will run forever (infinite loop!!! -> this is bad)
// }









// ex: common use



// most common syntaxes
for (let ii = 0; ii < 10; ++ii) {
  console.log(ii) // -> 0,1,2,3,4,5,6,7,8,9
}



// loop over the values of an array
const myArray1 = [11,22,33,44,55];
for (let counter = 0; counter < myArray1.length; counter = counter + 1) {
  // will run 5 times

  console.log(myArray1[counter]); // -> 11 -> 22 -> 33 -> 44 -> 55
}



// most common syntaxes
const myArray2 = [11,22,33,44,55];
for (const val of myArray2) {
  console.log(val) // -> 0,1,2,3,4,5,6,7,8,9
}














