-- Table Creations

CREATE TABLE CONFERENCE (
    ConferenceID INT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL
);

CREATE TABLE HEAD_COACH (
    CoachID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    ExperienceYears INT
);

CREATE TABLE TEAM (
    TeamID INT PRIMARY KEY,
    Name VARCHAR(50),
    City VARCHAR(50),
    Wins INT,
    Losses INT,
    ConferenceID INT,
    CoachID INT,
    FOREIGN KEY (ConferenceID) REFERENCES CONFERENCE(ConferenceID),
    FOREIGN KEY (CoachID) REFERENCES HEAD_COACH(CoachID)
);

CREATE TABLE PLAYER (
    PlayerID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Position VARCHAR(20),
    JerseyNumber INT,
    Points INT,
    Rebounds INT,
    Assists INT,
    Blocks INT,
    ThreePTAttempts INT,
    ThreePTMakes INT,
    FTAttempts INT,
    FTMakes INT,
    GamesPlayed INT,
    TeamID INT,
    FOREIGN KEY (TeamID) REFERENCES TEAM(TeamID)
);


-- Part 2 Data Insertions
-- Insert into CONFERENCE
INSERT INTO CONFERENCE VALUES (1, 'Eastern');
INSERT INTO CONFERENCE VALUES (2, 'Western');

-- Insert into HEAD_COACH
INSERT INTO HEAD_COACH VALUES (1, 'Steve', 'Kerr', 12);
INSERT INTO HEAD_COACH VALUES (2, 'Erik', 'Spoelstra', 15);
INSERT INTO HEAD_COACH VALUES (3, 'Mike', 'Brown', 10);
INSERT INTO HEAD_COACH VALUES (4, 'Gregg', 'Popovich', 27);
INSERT INTO HEAD_COACH VALUES (5, 'Doc', 'Rivers', 22);

-- Insert into TEAM
INSERT INTO TEAM VALUES (1, 'Warriors', 'San Francisco', 44, 38, 2, 1);
INSERT INTO TEAM VALUES (2, 'Heat', 'Miami', 48, 34, 1, 2);
INSERT INTO TEAM VALUES (3, 'Kings', 'Sacramento', 46, 36, 2, 3);
INSERT INTO TEAM VALUES (4, 'Spurs', 'San Antonio', 34, 48, 2, 4);
INSERT INTO TEAM VALUES (5, '76ers', 'Philadelphia', 49, 33, 1, 5);

-- Insert into PLAYER
INSERT INTO PLAYER VALUES (1, 'Stephen', 'Curry', 'Guard', 30, 2010, 400, 450, 50, 600, 280, 200, 180, 82, 1);
INSERT INTO PLAYER VALUES (2, 'Jimmy', 'Butler', 'Forward', 22, 1650, 300, 500, 60, 200, 80, 160, 120, 80, 2);
INSERT INTO PLAYER VALUES (3, 'Domantas', 'Sabonis', 'Center', 10, 1400, 800, 450, 70, 50, 15, 110, 95, 80, 3);
INSERT INTO PLAYER VALUES (4, 'Victor', 'Wembanyama', 'Center', 1, 1200, 700, 200, 120, 100, 35, 90, 70, 75, 4);
INSERT INTO PLAYER VALUES (5, 'Joel', 'Embiid', 'Center', 21, 2200, 900, 300, 85, 60, 20, 200, 160, 78, 5);

-- Part 3 Queries

-- Update Statements

UPDATE TEAM SET Wins = Wins + 1 WHERE TeamID = 1;
UPDATE PLAYER SET Points = Points + 50 WHERE PlayerID = 5;

-- Group By

SELECT Position, AVG(Points) AS AvgPoints
FROM PLAYER
GROUP BY Position;

SELECT TeamID, AVG(Points) AS AvgPoints
FROM PLAYER
GROUP BY TeamID
HAVING AVG(Points) > 1500;

-- Join Queries

-- Join player and team
SELECT P.FirstName, P.LastName, T.Name AS TeamName
FROM PLAYER P
JOIN TEAM T ON P.TeamID = T.TeamID;

-- Player and Conference
SELECT P.FirstName, P.LastName, C.Name AS Conference
FROM PLAYER P
JOIN TEAM T ON P.TeamID = T.TeamID
JOIN CONFERENCE C ON T.ConferenceID = C.ConferenceID;

-- Coach and team
SELECT HC.FirstName, HC.LastName, T.Name AS Team
FROM HEAD_COACH HC
JOIN TEAM T ON HC.CoachID = T.CoachID;

-- All player stats with coach info
SELECT P.FirstName, P.LastName, HC.FirstName AS CoachFirst, HC.LastName AS CoachLast
FROM PLAYER P
JOIN TEAM T ON P.TeamID = T.TeamID
JOIN HEAD_COACH HC ON T.CoachID = HC.CoachID;

-- Query with Subquery

SELECT FirstName, LastName, Points
FROM PLAYER
WHERE Points = (SELECT MAX(Points) FROM PLAYER);

-- Dynamic View

CREATE VIEW PlayerPerformance AS
SELECT FirstName, LastName, Points, Assists, Rebounds,
       ROUND(CAST(ThreePTMakes AS FLOAT)/ThreePTAttempts * 100, 2) AS ThreePT_PCT,
       ROUND(CAST(FTMakes AS FLOAT)/FTAttempts * 100, 2) AS FT_PCT
FROM PLAYER;
