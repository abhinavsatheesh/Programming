CREATE TABLE Nobel(Winner_id Integer, Year Char(4), Subject VarChar(20), Winner VarChar(30), Country VarChar(10), Category VarChar(20));
ALTER TABLE Nobel ADD Primary Key(Winner_ID);
INSERT INTO Nobel VALUES
(1001, 1970, 'Physics', 'Hannes Alfven', 'Sweden', 'Scientist'),
(1002, 1970, 'Physiology', 'Bernard Katz', NULL, 'Scientist'),
(1003, 1970, 'Literature', 'Aleksandr Solzhenitsyn', 'Russia', 'Linguist'),
(1004, 1971, 'Chemistry', 'Gerhard Herzberg', 'Germany', 'Scientist'),
(1005, 1978, 'Peace', 'Menachem Begin', 'Israel', 'Prime Minister'),
(1006, 1987, 'Economics', 'Robert Solow', 'USA', 'Economist'),
(1007, 1994, 'Literature', 'Kenzaburo Oe', 'Japan', 'Linguist');
SELECT Winner FROM Nobel WHERE Subject="Literature" and YEAR=1970;
SELECT Subject, Category FROM Nobel WHERE Country IS NULL;
SELECT * FROM Nobel WHERE Category="Scientist";
SELECT Winner FROM Nobel WHERE Winner LIKE "%berg%";
SELECT RIGHT(Winner,2) FROM Nobel WHERE Category="Scientist";
SELECT Country FROM Nobel WHERE Year>1971;
SELECT LCASE(Winner),LENGTH(Winner) FROM Nobel;
SELECT Winner FROM Nobel WHERE LENGTH(Winner)=12;
SELECT LEFT(Winner,4) FROM Nobel;
SELECT * FROM Nobel WHERE Year BETWEEN 1970 and 1980;
DELETE FROM Nobel WHERE Winner_ID=1003;
ALTER TABLE Nobel ADD Age Integer;
SELECT LEFT(Winner,3) FROM Nobel;
SELECT Winner FROM Nobel WHERE Subject="Physics" and YEAR=1970;
SELECT Winner FROM Nobel WHERE Country IN ("Sweden","USA");
SELECT RIGHT(Winner,3) FROM Nobel WHERE Year>1975;
