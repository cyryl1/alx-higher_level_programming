--  lists the number of records with the same score in the table of the database in your MySQL server.
SELECT score, COUNT(*) 'number'
FROM second_table
GROUP BY score
ORDER BY score DESC;
