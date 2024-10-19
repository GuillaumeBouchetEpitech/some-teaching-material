
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

      // SQL query to create a new table in the database
      const sqlQuery = `

        CREATE TABLE IF NOT EXISTS my_table (
          firstName TEXT,
          lastName TEXT,
          age INT
        )

      `;

      // the "!" is to shutdown an unwanted warning
      this._db!.run(sqlQuery, (err) => {
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

      // SQL query to insert a new value in the database table "my_table"
      const sqlQuery = `

        INSERT INTO
          my_table
        VALUES (
          "${newData.firstName}",
          "${newData.lastName}",
          ${newData.age}
        );

      `;

      this._db.run(sqlQuery, (err) => {
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

      // SQL query to list all the values in the database table "my_table"
      const sqlQuery = `

        SELECT
          *
        FROM
          my_table

      `;

      this._db.all<DataEntry>(sqlQuery, (err, rows) => {
        if (err) {
          return reject(err);
        }
        resolve(rows);
      });

    })
  }
}


