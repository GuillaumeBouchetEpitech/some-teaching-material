
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

  remove(value: string) {
    const foundIndex = this._list.indexOf(value); // return -1 if not found

    if (foundIndex < 0) {
      return; // do nothing
    }

    this._list.splice(foundIndex, 1); // remove one value from index "foundIndex"
  }

  has(value: string) {
    const foundIndex = this._list.indexOf(value); // return -1 if not found
    if (foundIndex < 0) {
      return false;
    }
    return true;
  }

  printContent() {
    for (const value of this._list) {
      console.log('->', value)
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


