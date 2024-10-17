


//
// Special Mentions: "Map"
//

const myMap1 = new Map();

myMap1.set("key", "value");

console.log(myMap1.get("key")); // -> "value"

console.log(myMap1.has("key")); // -> true
console.log(myMap1.has("not found key")); // -> false

myMap1.delete("key"); // remove the key from the map

// Map that is initialized with values
const myMap2 = new Map([
  ["key1", "value1"],
  ["key2", "value2"],
  ["key3", "value3"],
]);


// Why "Map"?
// -> it's MUCH faster than an object if there is a large number of element (ex: 300+)
// -> alternatively it's slower than an object if there is a small number of element (ex: 2-3)

// usually used for "caching" things
// ex of problem: an array of 1000+ users, but you need to find each user per firstName
// ex of solution: use a Map of user objects with their first name as the key

const allUsers = [
  { firstName: "john1", lastName: "Doe1", age: 40, address: "..." },
  { firstName: "john2", lastName: "Doe2", age: 40, address: "..." },
  { firstName: "john3", lastName: "Doe3", age: 40, address: "..." },
  { firstName: "john4", lastName: "Doe4", age: 40, address: "..." },
  // let's assume some 10k users here
];

// slow
const mySlowUser = allUsers.find(function (user) { return user.firstName === "John6000"; })

// ...
// now with a Map used as a cache

const myUserCache = new Map();
myUserCache.set(allUsers[0].firstElem, allUsers[0]);
myUserCache.set(allUsers[1].firstElem, allUsers[1]);
myUserCache.set(allUsers[2].firstElem, allUsers[2]);
myUserCache.set(allUsers[3].firstElem, allUsers[3]);
// let's assume all users here (...there are much smarter ways to achieve that)

const myFastUser = myUserCache.get("John6000");








//
// Special Mentions: "Set"
//

const mySet1 = new Set();

console.log(mySet1.has("my unique value 1")); // -> false

mySet1.add("my unique value 1"); // is added

console.log(mySet1.has("my unique value 1")); // -> true

mySet1.delete("my unique value 1"); // is removed

console.log(mySet1.has("my unique value 1")); // -> false



// most common use of the type Set:

const myDuplicatedValuesArray = [111,111, 222,222,222,222, 333, 444,444, 555];
const myUniqueValuesArray = [...new Set(myDuplicatedValuesArray)];
console.log(myUniqueValuesArray); // -> [111,222,333,444,555]
