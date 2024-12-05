-- CREATE TABLE HOSPITAL (
--     No INT PRIMARY KEY,
--     Name VARCHAR(255),
--     Age INT,
--     Department VARCHAR(255),
--     Dateofadm DATE,
--     charges INT,
--     sex CHAR(1)
-- );

-- INSERT INTO HOSPITAL (No, Name, Age, Department, Dateofadm, charges, sex)
-- VALUES
--     (1, 'Hariprasath', 65, 'Surgery', '2022-02-23', 30000, 'M'),
--     (2, 'Ravina', 24, 'Orthopedic', '2022-01-20', 20000, 'F'),
--     (3, 'Sumith', 45, 'Orthopedic', '2022-02-19', 20000, 'M'),
--     (4, 'Boopathi', 12, 'Surgery', '2022-01-01', 30000, 'M'),
--     (5, 'Ajayswamy', 36, 'ENT', '2022-02-12', 25000, 'M'),
--     (6, 'Ranjani', 16, 'ENT', '2022-02-24', 30000, 'F'),
--     (7, 'Lalithasri', 29, 'Cardiology','2022-02-20', 80000, 'F'),
--     (8, 'Lakshmi', 45, 'Gynecology', '2022-02-22', 30000, 'F'),
--     (9, 'Hariharan M', 19, 'Cardiology', '2022-01-13', 80000, 'M'),
--     (10, 'Hariharan K', 31, 'Nuclear Medicine', '2022-02-19', 40000, 'M');

--  a. To show all information about the patients of cardiology department:

SELECT *
FROM HOSPITAL
WHERE Department = "Cardiology";

-- b. To list the names of female patients who are in orthopedic dept:

SELECT Name
FROM HOSPITAL
WHERE Department = "Orthopedic" AND Sex = "F";

-- c. To list names of all patients with their date of admission in ascending order:

SELECT Name, Dateofadm
FROM HOSPITAL
ORDER BY Dateofadm ASC;

-- d. To display Patient’s Name, Charges, age for male patients only:

SELECT Name, Charges, Age
FROM HOSPITAL
WHERE Sex = "M";

-- e. To count the number of patients with age > 20:

SELECT COUNT(*)
FROM HOSPITAL
WHERE Age > 20;

-- f. To insert a new row in the HOSPITAL table

INSERT INTO HOSPITAL (No, Name, Age, Department, Dateofadm, Charges, Sex)
VALUES (11, 'Sivaprakasam', 37, 'ENT', '2022-02-14', 25000, 'M');