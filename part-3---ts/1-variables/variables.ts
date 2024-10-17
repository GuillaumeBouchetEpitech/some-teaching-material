


const myBoolean1: boolean = false;

const myNumber1: number = 666;
const myNumber2: number = 123.456;

const myString1: string = "hello";

const myObject1: {hello: string} = { hello: 'world' }

const myArray1: number[] = [11,22,33,44,55];





let myBoolean2: boolean = false;
myBoolean2 = true; // can reassign if boolean value


let myNumber3: number = 333;
myNumber3 = 444; // can reassign if number value





let myString2: string = "Bonjour Monde!";
myString2 = "hello world!"; // can reassign if string value




const myObject2: {hello: string} = {
  hello: 'world'
}



interface MyInterface {
  hello: string;
};
const myObject3: MyInterface = {
  hello: 'world'
}




// concrete example: list of users

interface IUser {
  firstName: string;
  lastName: string;
  age: number;
};

const allUsers: IUser[] = [];

allUsers.push({
  firstName: 'john',
  lastName: 'doe',
  age: 35
});


for (const user of allUsers) {
  console.log(`the user named ${user.firstName} ${user.lastName} is ${user.age} years old`);
}





