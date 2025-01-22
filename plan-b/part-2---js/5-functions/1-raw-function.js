

function myFunc1() {
  console.log("hello world!");
}

myFunc1(); // -> print "hello world!""





function myFunc2(myParameter) {
  console.log("hello " + myParameter);
}
myFunc2("world"); // -> print "hello world"
myFunc2("007"); // -> print "hello 007"
myFunc2(123); // -> print "hello 123"






function myAddFunc(valA, valB) {
  return valA + valB;
}

console.log( myAddFunc(1, 2) ); // -> print 3




function myClampFunc(val, min, max) {
  return Math.min(max, Math.max(val, min))
}

console.log(myClampFunc(10, -1, 1)); // -> 1
console.log(myClampFunc(-10, -1, 1)); // -> -1
console.log(myClampFunc(0.5, -1, 1)); // -> 0.5









