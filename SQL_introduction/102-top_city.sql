-- average temp by city rodered by temp desc
SELECT city, AVG(value) as avg_temp
FROM temperatures
WHERE month IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
