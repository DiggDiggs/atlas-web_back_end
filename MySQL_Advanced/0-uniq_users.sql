/* 
    This SQL statement creates a table named "users".
    If the table already exists, it will not cause an error.
    The "users" table has three columns: "id", "email", and "name".
    The "id" column is an auto-incrementing primary key.
    The "email" column is a unique non-null VARCHAR(255).
    The "name" column is a VARCHAR(255) allowing NULL values.
*/
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
