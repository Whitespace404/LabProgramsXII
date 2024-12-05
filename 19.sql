-- CREATE TABLE WORKERS (
--     W_ID INT PRIMARY KEY,
--     FIRSTNAME VARCHAR(50),
--     LASTNAME VARCHAR(50),
--     GENDER CHAR(1),
--     ADDRESS VARCHAR(100),
--     CITY VARCHAR(50)
-- );

-- INSERT INTO WORKERS (W_ID, FIRSTNAME, LASTNAME, GENDER, ADDRESS, CITY)
-- VALUES
--     (102, 'Sam', 'Tones', 'M', '33 Elm St', 'Paris'),
--     (105, 'Sarah', 'Ackerman', 'F', 'U.S. 110', 'New York'),
--     (144, 'Manila', 'Sengupta', 'F', '24 Friends Street', 'New Delhi'),
--     (210, 'George', 'Smith', 'M', '83 Frist Howard Street', 'Losantiville'),
--     (255, 'Mary', 'Jones', 'F', '842,Vine Ave.', 'Washington'),
--     (300, 'Robert', 'Samuel', 'M', '9 Fifth Cross', 'Boston'),
--     (335, 'Henry', 'Williams', 'M', '12 Moore Street', 'Boston'),
--     (403, 'Ronny', 'Lee', 'M', '121Harrison St.', 'New York'),
--     (451, 'Pat', 'Thompson', 'M', '11 Red Road', 'Paris');

-- CREATE TABLE DESIG (
--     W_ID INT PRIMARY KEY,
--     SALARY INT,
--     BENEFITS INT,
--     DESIGNATION VARCHAR(50)
-- );

-- INSERT INTO DESIG (W_ID, SALARY, BENEFITS, DESIGNATION)
-- VALUES
--     (102, 75000, 15000, 'Manager'),
--     (105, 85000, 25000, 'Director'),
--     (144, 70000, 15000, 'Manager'),
--     (210, 75000, 12500, 'Manager'),
--     (255, 50000, 12000, 'Clerk'),
--     (300, 45000, 10000, 'Clerk'),
--     (335, 40000, 10000, 'Clerk'),
--     (400, 32000, 7500, 'Salesman'),
--     (451, 28000, 7500, 'Salesman');

-- To display the content of WORKERS table in ascending order of LASTNAME:

SELECT *
FROM WORKERS
ORDER BY LASTNAME ASC;

-- To display First Name, Worker ID and Address of male Workers only:

SELECT FIRSTNAME, W_ID, ADDRESS
FROM WORKERS
WHERE GENDER = 'M';

-- To display the Minimum salary among Managers and Clerks from the table DESIG:

SELECT MIN(SALARY)
FROM DESIG
WHERE DESIGNATION IN ('Manager', 'Clerk');

-- To display First Name and Salary from Workers and Designation Table for each worker:

SELECT W.FIRSTNAME, D.SALARY
FROM WORKERS W
JOIN DESIG D ON W.W_ID = D.W_ID;

-- To view all the databases:

SHOW DATABASES;