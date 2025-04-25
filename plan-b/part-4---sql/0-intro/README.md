
# SQL - Syntax Query Language

CRUD - Create Read Update Delete

## Create Database

```sql
CREATE DATABASE database_name;
```

## Create Database Table

```sql
CREATE TABLE user_table (
  user_id int NOT NULL,
  last_name TEXT NOT NULL,
  first_name TEXT NOT NULL,
  age int  TEXT NULL,
  address TEXT NULL,
  PRIMARY KEY (user_id)
);
```

## Create Database Table row

```sql
INSERT INTO user_table
  (first_name, last_name, age)
VALUES
  ("John", "Doe", 30),
  ("Jane", "Doe", 40),
  ("Clark", "Kent", 50)
;
```

## Read Database Table row

```sql
SELECT * FROM user_table;
```

## Update Database Table row

```sql
UPDATE user_table
SET
  age = 35
WHERE
  first_name = "John"
  AND last_name = "Doe"
;
```

## Delete Database Table row

```sql
DELETE FROM user_table
WHERE
  first_name = "Jane"
  AND last_name = "Doe"
;
```

## SQL Injection Attack

