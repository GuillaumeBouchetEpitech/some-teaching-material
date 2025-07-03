
# Python vs JavaScript

---
---
---

## Variables


### Python
```python
my_number = 123
my_string = "hello"
my_list = []
my_dict = { "hello": 123 }
```

### JavaScript
```js
let my_number = 123;
let my_string = "hello";
let my_array = [];
let my_object = { "hello": 123 };
```

### TypeScript
```ts
let my_number: number = 123;
let my_string: string = "hello";
let my_array: number[] = [];
let my_object: Record<string, number> = { "hello": 123 };
```

---
---
---

## Str/String


### Python
```python
my_string = "Hello"
my_string2 = my_string.upper() # HELLO
my_string3 = my_string.lower() # hello
```

### JavaScript
```js
myString = "Hello"
myString2 = myString.toUpperCase() // HELLO
myString3 = myString.toLowerCase() // hello
```

### TypeScript
```ts
myString: string = "Hello"
myString2: string = myString.toUpperCase() // HELLO
myString3: string = myString.toLowerCase() // hello
```

---
---
---

## Functions

### Python
```python
def my_function(arg_a, arg_b):
  result = arg_a + arg_b
  return result

print(f"result is {result}")
```

### JavaScript
```js
function my_function(arg_a, arg_b) {
  let result = arg_a + arg_b;
  return result;
}

console.log(`result is ${result}`)
```

### TypeScript
```ts
function my_function(arg_a: number, arg_b: number): number {
  let result = arg_a + arg_b;
  return result;
}

console.log(`result is ${result}`)
```

---
---
---

## Classes

### Python
```python
class my_class:

  def __init__(self, arg_a):
    self._my_attribute = arg_a

  def my_method(self, arg_a):
    self._my_attribute = arg_a

my_object = my_class(123)

print(f"my_attribute is {my_object._my_attribute}") # 123

my_object.my_method(456)

print(f"my_attribute is {my_object._my_attribute}") # 456
```

### JavaScript
```js
class MyClass {

  constructor(argA) {
    this._myAttribute = argA;
  }

  myMethod(argA) {
    this._myAttribute = argA;
  }

};

my_object = new MyClass()

console.log(`myAttribute is ${my_object._myAttribute}`) // 123

my_object.myMethod(456)

console.log(`myAttribute is ${my_object._myAttribute}`) // 456
```

### TypeScript
```ts
class MyClass {

  public _myAttribute: number;

  constructor(argA: number) {
    this._myAttribute = argA;
  }

  myMethod(argA: number): void {
    this._myAttribute = argA;
  }

};

my_object: MyClass = new MyClass();

console.log(`myAttribute is ${my_object._myAttribute}`); // 123

my_object.myMethod(456);

console.log(`myAttribute is ${my_object._myAttribute}`); // 456
```

---
---
---

## Lists/Arrays


### Python
```python
my_list = [1, 2, 3]
my_list.append(4)
my_list.append(5)
my_list.append(6)

# remove element at index 3 (which is the value 4)
del my_list[3]

print(my_list) # [1, 2, 3, 5, 6]
```

### JavaScript
```js
let my_array = [1, 2, 3];
my_array.push(4, 5, 6);

// remove 1 element at index 3 (which is the value 4)
my_array.splice(3, 1);

console.log(my_array) // [1, 2, 3, 5, 6]
```

### TypeScript
```ts
let my_array: number[] = [1, 2, 3]; // only difference
my_array.push(4, 5, 6);

// remove 1 element at index 3 (which is the value 4)
my_array.splice(3, 1);

console.log(my_array) // [1, 2, 3, 5, 6]
```

---
---
---

## Dict/Object


### Python
```python
my_dict = { "hello": 123 }

if hasattr(my_dict, "hello"):
  print("has the 'hello' attribute")
else:
  print("hasn't got the 'hello' attribute")

value = my_dict.get("hello", None)
# value is 123
print(f"the 'hello' attribute: {value}")

print(my_dict) # { 'hello': 123 }

del my_dict["hello"]

print(my_dict) # {}
```

### JavaScript
```js
let myObject = { "hello": 123 };

if (myObject["hello"] != undefined) {
  console.log("has the 'hello' attribute");
} else {
  console.log("hasn't got the 'hello' attribute");
}

value = myObject["hello"];
// value is 123
console.log(`the 'hello' attribute: ${value}`);

console.log(myObject); // { 'hello': 123 }

delete myObject["hello"];

console.log(myObject); // {}
```

### TypeScript
```ts
// only difference:
let myObject: Record<string, number> = { "hello": 123 };

if (myObject["hello"] != undefined) {
  console.log("has the 'hello' attribute");
} else {
  console.log("hasn't got the 'hello' attribute");
}

value = myObject["hello"];
// value is 123
console.log(`the 'hello' attribute: ${value}`);

console.log(myObject); // { 'hello': 123 }

delete myObject["hello"];

console.log(myObject); // {}
```

---
---
---

## Branching


### Python
```python
my_value = 5

if my_value < 3:
  print("value is low") # nope
elif my_value < 6:
  print("value is mid") # yup
else:
  print("value is high") # nope
```

### JavaScript
```js
let myValue = 5;

if (myValue < 3) {
  console.log("value is low") // nope
} else if (myValue < 6) {
  console.log("value is mid") // yup
} else {
  console.log("value is high") // nope
}
```

### TypeScript
```ts
let myValue: number = 5; // <- only difference

if (myValue < 3) {
  console.log("value is low") // nope
} else if (myValue < 6) {
  console.log("value is mid") // yup
} else {
  console.log("value is high") // nope
}
```



---
---
---

## Loops


### Python
```python
for i in range(0, 10):
  print(f"step {i}") # step 0, step 1, ... step 9

my_list = [1,2,3,4,5]
for value in my_list:
  print(f"step {value}") # step 1, step 2, ... step 5

i = 0
while i < 5:
  print(i) # 0,1,2,3,4
  i += 1
```

### JavaScript
```js
// loop in 3 parts -> for (INIT; CONDITION; STEP)
for (let i = 0; i < 10; i += 1)
  console.log(`step ${i}`) // step 0, step 1, ... step 9

let myList = [1,2,3,4,5]
for (let value of myList)
  console.log(`step ${value}`) // step 1, step 2, ... step 5

let i = 0;
while (i < 5) {
  console.log(i); // 0,1,2,3,4
  i += 1;
}
```

### TypeScript
```ts
for (let i = 0; i < 10; i += 1)
  console.log(`step ${i}`) // step 0, step 1, ... step 9

let myList: number[] = [1,2,3,4,5]
for (let value of myList)
  console.log(`step ${value}`) // step 1, step 2, ... step 5

let i: number = 0;
while (i < 5) {
  console.log(i); // 0,1,2,3,4
  i += 1;
}
```


