CREATE TABLE employee (
    EMP_ID INT PRIMARY KEY,
    NAME VARCHAR(50),
    DOB DATE,
    DESIG VARCHAR(50),
    SALARY INT
);

INSERT INTO employee (EMP_ID, NAME, DOB, DESIG, SALARY)
VALUES
    (120, 'Alisha', '1978-01-23', 'D001 Manager', 75000),
    (123, 'Nitin', '1977-10-10', 'D002 AO', 59000),
    (129, 'Navjot', '1971-07-12', 'D003 Supervisor', 40000),
    (130, 'Jimmy', '1980-12-30', 'D004 Sales Rep', NULL),
    (131, 'Faiz', '1984-04-06', 'D001 Dep Manager', 65000);

CREATE TABLE DEPARTMENT (
    DEPTID VARCHAR(255) PRIMARY KEY,
    DEPTNAM VARCHAR(255),
    FLOORNO INT
);

INSERT INTO DEPARTMENT (DEPTID, DEPTNAM, FLOORNO)
VALUES
    ('D001', 'Personal', 4),
    ('D002', 'Admin', 10),
    ('D003', 'Production', 1),
    ('D004', 'Sales', 3);

-- To display the average salary of all employees, department wise.
SELECT
  d.DEPTNAM,
  AVG(e.SALARY) AS AVERAGE_SALARY
FROM
  employee e
JOIN department d ON SUBSTRING(e.DESIG, 1, 4) = d.DEPTID
GROUP BY
  d.DEPTNAM;

-- To display name and respective department name of each employee whose salary is more than 50000.
SELECT
  e.NAME,
  d.DEPTNAM
FROM
  employee e
JOIN department d ON SUBSTRING(e.DESIG, 1, 4) = d.DEPTID
WHERE
  e.SALARY > 50000;

-- To display the names of employees whose salary is not known, in alphabetical order.
SELECT name FROM employee WHERE SALARY IS NULL ORDER BY NAME;

-- To display DEPTID from the table EMPLOYEE without repetition.
SELECT DISTINCT SUBSTRING(DESIG, 1, 4) AS DEPTID
FROM EMPLOYEE;

-- Display the complete details of employee who have born after 1978.
SELECT *
FROM EMPLOYEE
WHERE DOB > '1978-12-31';