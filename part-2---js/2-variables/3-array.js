

//
// array list -> array
//

const myArray1 = [] // empty array
const myArray2 = ["hello", "world"] // array of strings
const myArray3 = [22.33, -77] // array of numbers
const myArray4 = ["hello", "world", 22.33, -77] // array of any variable







// arrays are "objects" with "methods"
// ex:

const myArray5 = [];
myArray5.push("last"); // ["last"]
myArray5.push("real-last"); // ["last", "real-last"]
myArray5.shift("first"); // ["first", "last", "real-last"]
myArray5.length; // -> 3 (3 elements)

const lastElem = myArray5.pop();  // ["first", "last"]
// lastElem -> "real-last"

myArray5.length; // -> 2 (2 elements)

const firstElem = myArray5.unshift();  // ["last"]
// firstElem -> "first"

myArray5.length; // -> 1 (1 elements)

myArray5.length = 0; // this empty the array of it's content

// it's not necessary to store the array in a variable to use it
console.log([ 3, 2, 1, "liftoff" ]); // -> [ 3, 2, 1, "liftoff" ]








myArray6_1 = [111,222,333,444,555]

console.log(myArray6_1) // -> [111,222,333,444,555]

myArray6_2 = [...myArray6_1]; // unpack all of "myArray6_1" into "myArray6_2"

console.log(myArray6_2) // -> [111,222,333,444,555]

myArray6_3 = [...myArray6_1, 666, 777]; // unpack all of "myArray6_1" into "myArray6_2" plus some values

console.log(myArray6_3) // -> [111,222,333,444,555,666,777]



