

function MyClass1() {
  this.myAttribute = 123;
}


const myObject1 = new MyClass1();

console.log(myObject1.myAttribute) // -> print 123

myObject1.myAttribute = 222;

console.log(myObject1.myAttribute) // -> print 222










// create a class (yes... it's a raw-function)
function MyClass2() {
  // the "this" keyword can be access from inside a raw-function
  this.myAttribute = 123; // this is called an "attribute"
}

// create a method
MyClass2.prototype.myMethod = function() {
  // the "this" keyword can be access from inside classes method(s)
  this.myAttribute = 123;
}



const myObject2 = new MyClass2();

console.log(myObject2.myAttribute) // -> print 123

// change the attribute value
myObject2.myAttribute = 222;

console.log(myObject2.myAttribute) // -> print 222

// call a method
myObject2.myMethod();

console.log(myObject2.myAttribute) // -> print 123









