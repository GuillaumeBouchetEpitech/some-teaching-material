
import sqlite3 from 'sqlite3'


export interface DataEntry {
  firstName: string;
  lastName: string;
  age: number;
}

// defined an interface, a "contract" that the class must respect
export interface IMyDataBase {

  initialize(): Promise<void>;

  insert(newData: DataEntry): Promise<void>;

  list(startIndex: number, maxSize: number): Promise<DataEntry[]>;

};

export class MyDataBase implements IMyDataBase {

  private _db?: sqlite3.Database;

  constructor() {
  }

  async initialize(): Promise<void> {

    if (this._db) {
      throw new Error(`the db is already initialized`)
    }
    // this._db = new sqlite3.Database(':memory:');
    this._db = new sqlite3.Database('./database.sqlite');

    await this._executeAsyncRun(`

      CREATE TABLE IF NOT EXISTS my_table (
        rowId INTEGER PRIMARY KEY,
        firstName TEXT,
        lastName TEXT,
        age INT
      )

    `);
  }

  async insert(newData: DataEntry): Promise<void> {

    // SQL query to insert a new value in the database table "my_table"
    await this._executeAsyncRun(`

      INSERT INTO
        my_table (firstName, lastName, age)
      VALUES
        ("${newData.firstName}", "${newData.lastName}", ${newData.age})
      ;

    `);
  }

  async remove(rowId: number): Promise<void> {
    // SQL query to delete an existing value in the database table "my_table"
    await this._executeAsyncRun(`

      DELETE FROM
        my_table
      WHERE
        rowId = ${rowId}
      ;

    `);
  }

  async list(startIndex: number, maxSize: number): Promise<DataEntry[]> {
    return new Promise<DataEntry[]>((resolve, reject) => {

      if (!this._db) {
        return reject(new Error(`the db is not already initialized`));
      }

      // SQL query to list all the values in the database table "my_table"
      const sqlQuery = `

        SELECT
          *
        FROM
          my_table
        LIMIT
          ${maxSize}
        OFFSET
          ${startIndex}

      `;

      this._db.all<DataEntry>(sqlQuery, (err, rows) => {
        if (err) {
          return reject(err);
        }
        resolve(rows);
      });

    })
  }

  // helper method
  private async _executeAsyncRun(sqlQuery: string): Promise<void> {

    return new Promise<void>((resolve, reject) => {

      if (!this._db) {
        return reject(new Error(`the db is not already initialized`));
      }

      this._db.run(sqlQuery, (err) => {
        if (err) {
          return reject(err);
        }
        resolve();
      });

    });
  }

}


