CREATE DATABASE if not exists Family_Details;
USE Family_Details;
CREATE TABLE if not exists Basic_Details(nameofmembers VarChar(50), age int, gender Varchar(6), dob DATE);
INSERT INTO Basic_Details VALUES("Abhinav Satheesh", 15, "Male", "2007-07-06");
INSERT INTO Basic_Details VALUES("Anu Satheesh", 40, "Female", "1982-12-26");
INSERT INTO Basic_Details VALUES("Satheesh Bharathan", 47, "Male", "1975-06-24");