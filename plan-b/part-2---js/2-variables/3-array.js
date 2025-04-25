

//
// array list -> array
//

const myArray1 = [] // empty array
const myArray2 = ["hello", "world"] // array of strings
const myArray3 = [22.33, -77] // array of numbers
const myArray4 = ["hello", "world", 22.33, -77] // array of any variable







// arrays are "objects" with "methods"
// ex:

const myArray5 = []; // []
myArray5.push("last"); // ["last"]
myArray5.push("real-last"); // ["last", "real-last"]
myArray5.shift("first"); // ["first", "last", "real-last"]
myArray5.length; // -> 3 (3 elements)

const lastElem = myArray5.pop(); // ["first", "last"]
// lastElem -> "real-last"

myArray5.length; // -> 2 (2 elements -> ["first", "last"])

const firstElem = myArray5.unshift(); // ["last"]
// firstElem -> "first"

myArray5.length; // -> 1 (1 elements -> ["last"])

myArray5.length = 0; // this empty the array of it's content
// myArray5 -> []

// it's not necessary to store the array in a variable to use it
console.log([ 3, 2, 1, "liftoff" ]); // -> will print -> "[ 3, 2, 1, "liftoff" ]"








myArray6 = [111,222,333,444,555]

console.log(myArray6) // -> [111,222,333,444,555]

myArray7 = [...myArray6]; // "unpack" all of "myArray6" into "myArray7"

console.log(myArray7) // -> [111,222,333,444,555]

myArray8 = [-111, ...myArray6, 666, 777]; // unpack all of "myArray6" into "myArray8" plus some values

console.log(myArray8) // -> [-111,111,222,333,444,555,666,777]



