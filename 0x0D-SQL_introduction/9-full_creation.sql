-- creates a table in the database in your MySQL server and add multiples rows.
CREATE TABLE IF NOT EXISTS `second_table`(
	id INT NOT NULL,
	name VARCHAR(256),
	score INT NOT NULL
);
INSERT INTO second_table VALUES
('1', 'John', '10'),
('2', 'Alex', '3'),
('3', 'Bob', '14'),
('4', 'George', '8');
