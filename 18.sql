-- CREATE TABLE TAXITYPE (
--   TAXI_CO VARCHAR(255) PRIMARY KEY,
--   TAXITYPE VARCHAR(255),
--   PER_KM INT
-- );

-- INSERT INTO TAXITYPE (TAXI_CO, TAXITYPE, PER_KM)
-- VALUES
--   ('T01', 'TEMPO_TRAVELLER', 40),
--   ('T02', 'AC_INNOVA', 20),
--   ('T03', 'AC_ERTIGA', 15),
--   ('T04', 'AC_HATCHBACK', 10),
--   ('T05', 'AC_SEDAN', 10);

-- CREATE TABLE TRAVEL (
--   CNO INT PRIMARY KEY,
--   CNAME VARCHAR(255),
--   TRAVELDATE DATE,
--   KM INT,
--   TAXI_CODE VARCHAR(255),
--   NO_PEOPLE INT,
--   FOREIGN KEY (TAXI_CODE) REFERENCES TAXITYPE(TAXI_CO)
-- );

-- INSERT INTO TRAVEL (CNO, CNAME, TRAVELDATE, KM, TAXI_CODE, NO_PEOPLE)
-- VALUES
--   (101, 'Randeep Singh', '2018-11-07', 200, 'T01', 12),
--   (102, 'Sharad Bali', '2018-12-21', 120, 'T04', 4),
--   (105, 'Sangeeta M', '2019-04-25', 450, 'T01', 15),
--   (103, 'Manish Nagpal', '2019-01-29', 280, 'T02', 5),
--   (107, 'Veronica Masih', '2019-03-12', 365, 'T04', 2),
--   (104, 'Hoon', '2019-10-28', 290, 'T05', 4),
--   (106, 'Malik', '2019-04-06', 100, 'T01', 20);

-- To display CNO, CNAME, TRAVELDATE from the table TRAVEL in
-- descending order of CNO.
SELECT CNO, CNAME, TRAVELDATE
FROM TRAVEL
ORDER BY CNO DESC;

-- To display the CNAME of all customers from the table TRAVEL who are
-- travelling by vehicle with code T01 or T02.
SELECT CNAME
FROM TRAVEL
WHERE TAXI_CODE IN ('T01', 'T02');


-- To display the CNO and CNAME of those customers from the
--  table TRAVEL who travelled between '2019-01-06' and '2019-05-01':
SELECT CNO, CNAME
FROM TRAVEL
WHERE TRAVELDATE BETWEEN '2019-01-06' AND '2019-05-01';

-- To display all the details from table TRAVEL for the customers,
-- who have travel distance more than 250 KM in ascending order of NOP (Number of Passengers):
SELECT *
FROM TRAVEL
WHERE KM > 250
ORDER BY NO_PEOPLE ASC;

-- To drop both tables
-- DROP TABLE TRAVEL;
-- DROP TABLE TAXITYPE;