CREATE TABLE GAMES (
    GCode INT PRIMARY KEY,
    GameName VARCHAR(50),
    Type VARCHAR(20),
    Number INT,
    PrizeMoney INT
);

INSERT INTO GAMES (GCode, GameName, Type, Number, PrizeMoney) VALUES
(101, 'CarromBoard', 'Indoor', 2, 5000),
(102, 'Badminton', 'Outdoor', 2, 12000),
(103, 'TableTennis', 'Indoor', 4, NULL),
(104, 'Chess', 'Indoor', 2, 9000),
(105, 'LawnTennis', 'Outdoor', 4, 25000);

CREATE TABLE PLAYERS (
    PCode INT PRIMARY KEY,
    Name VARCHAR(50),
    GCode INT,
    FOREIGN KEY (GCode) REFERENCES GAMES(GCode)
);

INSERT INTO PLAYERS (PCode, Name, GCode) VALUES
(1, 'NabiAhmad', 101),
(2, 'RaviSahai', 104),
(3, 'Jatin', 101),
(4, 'Nazneen', 103);

SELECT Type, AVG(Number) FROM GAMES GROUP BY Type;
SELECT PrizeMoney FROM GAMES ORDER BY PrizeMoney DESC;
SELECT G.PrizeMoney, G.GameName, P.Name FROM GAMES G, PLAYERS P WHERE G.GCode=P.GCode;
ALTER TABLE PLAYERS ADD AGE Integer;
SELECT UCASE(GameName),PrizeMoney from GAMES WHERE PrizeMoney IS NOT NULL;
