
//
// Objects
//

const myObject1 = {} // empty object



// object with one entry
// the entry is key="hello" with the value "world"
const myObject2 = { hello: "world" }

// we can access the value, it's very fast
console.log(myObject2.hello); // -> "world"

// we can add a value
myObject2.someNumbers = 123;

// console logging will show the content of the object
console.log(myObject2); // -> { hello: "world", someNumbers: 123 }






// it's not necessary to store the object in a variable to use it
console.log({ someKey: "some value" }); // -> { someKey: "some value" }





// object entries can have complex keys name
const myObject3 = { "I'm a key": "world" }

console.log(myObject3["I'm a key"]); // -> "world"

myObject3["I'm a key"] = "mad world"

console.log(myObject3["I'm a key"]); // -> "mad world"

console.log(myObject3); // -> { "I'm a key": "mad world" }






const myObject4 = {
  key1: "value1",
  key2: "value2",
  key3: "value3",
};
console.log(myObject4); // -> { key1: "value1", key2: "value2", key3: "value3" }

delete myObject4.key2; // remove key2

console.log(myObject4); // -> { key1: "value1", key3: "value3" }






const myObject5_1 = { hello: "world" };
console.log(myObject5_1); // -> { hello: "world" }

const myObject5_2 = { ...myObject5_1 }; // unpack all of "myObject5_1" into "myObject5_2"
console.log(myObject5_2); // -> { hello: "world" }

const myObject5_3 = { ...myObject5_1, test: 666 }; // same as before, but with an extra field
console.log(myObject5_3); // -> { hello: "world", test: 666 }





// some more ex:

const user1 = {
  firstName: "James",
  lastName: "Bond",
  age: 40,
  address: "Somewhere in the world",
  profession: "Spy",
};



