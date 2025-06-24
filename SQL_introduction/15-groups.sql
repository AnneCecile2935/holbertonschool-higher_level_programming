-- requete records by row, couont lines display score and sorted by
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY Score
ORDER BY number DESC
