-- displays the max temperature of each state
SELECT state, MAX(value) AS avg_temp FROM temperatures GROUP BY state ORDER BY state LIMIT 3;
