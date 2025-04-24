-- This script creates a table and columns

-- This command creates a new table
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(50),
    score INT
);

-- This command adds new records
INSERT INTO second_table VALUES (1, 'John', 10);
INSERT INTO second_table VALUES (2, 'Alex', 3);
INSERT INTO second_table VALUES (3, 'Bob', 14);
INSERT INTO second_table VALUES (4, 'George', 8);
