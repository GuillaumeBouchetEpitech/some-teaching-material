

class MyClass1 {

  constructor() {
    this.myAttribute = 123;
  }
}

const myObject1 = new MyClass1();

console.log(myObject1.myAttribute) // -> print 123

myObject1.myAttribute = 222;

console.log(myObject1.myAttribute) // -> print 222













class MyClass2 {

  constructor() {
    this.myAttribute = 123;
  }

  myMethod() {
    this.myAttribute = 123;
  }
}


const myObject2 = new MyClass2();

console.log(myObject2.myAttribute) // -> print 123

// change the attribute value
myObject2.myAttribute = 222;

console.log(myObject2.myAttribute) // -> print 222

// call a method
myObject2.myMethod();

console.log(myObject2.myAttribute) // -> print 123















