-- This script imports another table in "temperatures.sql" in the database
-- Then calculates the average temperature in Fahrenheit

-- This command achieves the task
SELECT city, AVG(value) AS average_temperature FROM temperatures GROUP BY city ORDER BY average_temperature DESC;
