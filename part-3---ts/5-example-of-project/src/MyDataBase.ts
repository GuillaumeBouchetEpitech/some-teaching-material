
import sqlite3 from 'sqlite3'


export interface DataEntry {
  firstName: string;
  lastName: string;
  age: number;
}

export class MyDataBase {

  private _db?: sqlite3.Database;

  constructor() {
  }

  async initialize(): Promise<void> {

    if (this._db) {
      throw new Error(`the db is already initialized`)
    }
    // this._db = new sqlite3.Database(':memory:');
    this._db = new sqlite3.Database('./database.sqlite');

    return new Promise<void>((resolve, reject) => {

      // the "!" is to shutdown an unwanted warning
      this._db!.run(`

        CREATE TABLE my_table (
          firstName TEXT,
          lastName TEXT,
          age INT
        )

      `, (err) => {
        if (err) {
          return reject(err);
        }
        return resolve()
      });
    });
  }

  async insert(newData: DataEntry): Promise<void> {

    return new Promise<void>((resolve, reject) => {

      if (!this._db) {
        return reject(new Error(`the db is not already initialized`));
      }

      this._db.run(`

        INSERT INTO
          my_table
        VALUES (
          "${newData.firstName}",
          "${newData.lastName}",
          ${newData.age}
        );

      `, (err) => {
        if (err) {
          return reject(err);
        }
        resolve();
      });

    });
  }

  async list(): Promise<DataEntry[]> {
    return new Promise<DataEntry[]>((resolve, reject) => {

      if (!this._db) {
        return reject(new Error(`the db is not already initialized`));
      }

      this._db.all<DataEntry>(`

        SELECT
          *
        FROM
          my_table

      `, (err, rows) => {
        if (err) {
          return reject(err);
        }
        resolve(rows);
      });

    })
  }
}


