-- This script prints the full description of the table first_table
-- from the database hbtn_0c_0, without using DESCRIBE or EXPLAIN

-- -- These commands achieve the task
SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_DEFAULT, EXTRA
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'first_table' AND TABLE_SCHEMA = 'hbtn_0c_0';
