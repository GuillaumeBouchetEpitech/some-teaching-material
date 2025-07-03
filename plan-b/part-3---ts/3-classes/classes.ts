
class MyDatabase {

  private _list: string[] = [];
  private _maxLength: number;

  constructor(maxLength: number) {
    this._maxLength = maxLength;
  }

  add(value: string) {

    if (this._list.length >= this._maxLength) {
      return; // do nothing
    }

    this._list.push(value);
  }

  remove(toFind: string) {
    // foundIndex is of value -1 if not found
    const foundIndex = this._list.findIndex((value) => {
      return value == toFind;
    });

    if (foundIndex < 0) {
      return; // do nothing
    }

    // remove one value from index "foundIndex"
    this._list.splice(foundIndex, 1);
  }

  has(toFind: string) {
    // foundIndex is of value -1 if not found
    const foundIndex = this._list.findIndex((value) => {
      return value == toFind;
    });
    if (foundIndex < 0) {
      return false; // not found
    }
    return true; // found
  }

  printContent() {
    console.log(`size ${this._list.length}`);
    for (const value of this._list) {
      console.log(`-> ${value}`);
    }
  }

}


const myDatabase = new MyDatabase(3);

myDatabase.add('hello1');
myDatabase.add('hello2');
myDatabase.add('hello3');
myDatabase.add('hello4');
myDatabase.printContent(); // -> hello1,hello2,hello3

myDatabase.has('hello4'); // -> false
myDatabase.has('hello2'); // -> true

myDatabase.remove('hello2');
myDatabase.printContent(); // -> hello1,hello3

myDatabase.add('hello4');
myDatabase.printContent(); // -> hello1,hello3,hello4


