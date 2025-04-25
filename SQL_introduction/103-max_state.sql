-- This script displays the maximum temperature of each state

-- This command achieves the task
SELECT state, MAX(temperature) AS max_temp
FROM temperature
GROUP BY state
ORDER BY state;
