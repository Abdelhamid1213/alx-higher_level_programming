-- Retrieve the "score" and "name" columns from the "second_table" where the "name" is not NULL and not an empty string.
SELECT `score`, `name` FROM `second_table` WHERE `name` IS NOT NULL AND `name` != '';
