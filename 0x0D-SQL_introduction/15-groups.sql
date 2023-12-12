-- Retrieve the "score" and the count of occurrences ("number") from the "second_table," grouped by the "score" column, and ordered in descending order based on the count.
SELECT score, COUNT(score) AS `number` FROM second_table GROUP BY score ORDER BY `number` DESC;
