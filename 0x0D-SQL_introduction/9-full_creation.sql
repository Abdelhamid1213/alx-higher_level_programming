-- Create a table named "second_table" with columns "id" of type INT, "name" of type VARCHAR(256), and "score" of type INT if it does not already exist.
CREATE TABLE IF NOT EXISTS `second_table` (
    id INT,
    name VARCHAR(256),
    score INT
);
-- Insert records into "second_table" with values (1, 'John', 10), (2, 'Alex', 3), (3, 'Bob', 14), and (4, 'George', 8).
INSERT INTO `second_table`
    (id, name, score) 
VALUES 
    (1, 'John', 10),
    (2, 'Alex', 3),
    (3, 'Bob', 14),
    (4, 'George', 8);
