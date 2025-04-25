-- This script displays all the records
-- Records will be displayed by descending order of score

-- This command achieves the task
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
