




// typed parameters
// typed returned value
const myAddFunction = (paramA: number, paramB: number): number => {
  return paramA + paramB;
}

console.log(`1 + 2 = ${myAddFunction(1,2)}`);




// typed for return is "void", nothing is returned
const myLogArrayFunction = (myArray: number[]): void => {
  console.log("myArray.length", myArray.length)
  for (let ii = 0; ii < myArray.length; ++ii) {
    console.log(` -> [${ii}] -> ${myArray[ii]}`)
  }
};


myLogArrayFunction([]);
// -> myArray.length 0

myLogArrayFunction([111,222,333,444,555]);
//> myArray.length 5
//>  -> [0] -> 111
//>  -> [1] -> 222
//>  -> [2] -> 333
//>  -> [3] -> 444
//>  -> [4] -> 555






