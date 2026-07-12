
DROP TABLE IF EXISTS Employees;
DROP TABLE IF EXISTS Departments;

CREATE TABLE Departments (
    DepartmentID INTEGER PRIMARY KEY,
    DepartmentName VARCHAR(50),
    Location VARCHAR(50)
);

INSERT INTO Departments
    (DepartmentID, DepartmentName, Location)
VALUES
    (1, 'HR', 'London'),
    (2, 'Finance', 'Frankfurt'),
    (3, 'IT', 'Berlin'),
    (4, 'Sales', 'Paris'),
    (5, 'Marketing', 'Madrid');
    
    SELECT * FROM Departments;
    
    CREATE TABLE Employees (
    EmployeeID INTEGER PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Gender VARCHAR(10),
    Age INTEGER,
    DepartmentID INTEGER,
    City VARCHAR(50),
    Salary INTEGER,
    FOREIGN KEY (DepartmentID)
        REFERENCES Departments(DepartmentID)
);

INSERT INTO Employees
    (
        EmployeeID,
        FirstName,
        LastName,
        Gender,
        Age,
        DepartmentID,
        City,
        Salary
    )
VALUES
    (101, 'Emma', 'Wilson', 'Female', 28, 1, 'London', 45000),
    (102, 'Liam', 'Smith', 'Male', 35, 2, 'Manchester', 62000),
    (103, 'Sophia', 'Brown', 'Female', 31, 3, 'Berlin', 70000),
    (104, 'Noah', 'Taylor', 'Male', 42, 4, 'Paris', 68000),
    (105, 'Olivia', 'Martin', 'Female', 26, 5, 'Madrid', 48000),
    (106, 'Lucas', 'Muller', 'Male', 38, 3, 'Munich', 82000),
    (107, 'Isabella', 'Garcia', 'Female', 30, 2, 'Barcelona', 61000),
    (108, 'Ethan', 'Johnson', 'Male', 45, 1, 'Dublin', 75000),
    (109, 'Mia', 'Anderson', 'Female', 27, 4, 'Amsterdam', 52000),
    (110, 'James', 'Thomas', 'Male', 33, 3, 'London', 73000);
    
    
   -- =====================================================
-- QUESTION 1: Display all employees
-- SELECT means: show me data
-- * means: show every column
-- FROM Employees means: get the data from the Employees table
-- ===================================================== 
    SELECT * FROM Employees;
    
    
    
   -- =====================================================
-- QUESTION 2: Display only employee names and salaries
-- We select only the columns we want to see
-- FirstName and LastName show the employee's name
-- Salary shows how much the employee earns
-- ===================================================== 
    SELECT FirstName, LastName, Salary
FROM Employees;

-- =====================================================
-- QUESTION 3: Count the total number of employees
-- COUNT(*) counts all rows in the Employees table
-- Each row represents one employee
-- AS TotalEmployees gives the answer column a clear name
-- =====================================================
SELECT COUNT(*) AS TotalEmployees
FROM Employees;

-- Question 4: Show every city only once
SELECT DISTINCT City
FROM Employees;

-- =====================================================
-- QUESTION 5: Display all unique department IDs
-- DISTINCT removes repeated DepartmentID values
-- =====================================================

SELECT DISTINCT DepartmentID
FROM Employees;


-- =====================================================
-- QUESTION 6: Find employees older than 30
-- WHERE filters the rows
-- > means greater than
-- =====================================================

SELECT *
FROM Employees
WHERE Age > 30;


-- =====================================================
-- QUESTION 7: Find employees earning more than 60,000
-- Only employees with a Salary above 60000 are shown
-- =====================================================

SELECT *
FROM Employees
WHERE Salary > 60000;


-- =====================================================
-- QUESTION 8: Display employees from London
-- Text values such as London must be inside quotes
-- =====================================================

SELECT *
FROM Employees
WHERE City = 'London';


-- =====================================================
-- QUESTION 9: Find employees earning between 50,000 and 75,000
-- BETWEEN includes both 50000 and 75000
-- =====================================================

SELECT *
FROM Employees
WHERE Salary BETWEEN 50000 AND 75000;


-- =====================================================
-- QUESTION 10: Display employees whose first name starts with L
-- LIKE searches for a text pattern
-- L% means: starts with L, followed by anything
-- =====================================================

SELECT *
FROM Employees
WHERE FirstName LIKE 'L%';


-- =====================================================
-- QUESTION 11: Display employees younger than 35
-- < means less than
-- =====================================================

SELECT *
FROM Employees
WHERE Age < 35;


-- =====================================================
-- QUESTION 12: Sort employees by salary, highest first
-- ORDER BY sorts the results
-- DESC means highest to lowest
-- =====================================================

SELECT *
FROM Employees
ORDER BY Salary DESC;


-- =====================================================
-- QUESTION 13: Sort employees by age, youngest first
-- ASC means lowest to highest
-- =====================================================

SELECT *
FROM Employees
ORDER BY Age ASC;


-- =====================================================
-- QUESTION 14: Sort employees by city and then salary
-- SQL sorts by City first
-- Then it sorts salaries inside the same city
-- =====================================================

SELECT *
FROM Employees
ORDER BY City ASC, Salary ASC;


-- =====================================================
-- QUESTION 15: Find the average salary
-- AVG() calculates the average
-- AS gives the result column a readable name
-- =====================================================

SELECT AVG(Salary) AS AverageSalary
FROM Employees;


-- =====================================================
-- QUESTION 16: Find the highest salary
-- MAX() finds the largest value
-- =====================================================

SELECT MAX(Salary) AS HighestSalary
FROM Employees;


-- =====================================================
-- QUESTION 17: Find the minimum salary
-- MIN() finds the smallest value
-- =====================================================

SELECT MIN(Salary) AS MinimumSalary
FROM Employees;


-- =====================================================
-- QUESTION 18: Find the average employee age
-- AVG() calculates the average age
-- =====================================================

SELECT AVG(Age) AS AverageAge
FROM Employees;


-- =====================================================
-- QUESTION 19: Count employees in each department
-- GROUP BY creates one group for each DepartmentID
-- COUNT(*) counts employees inside each group
-- =====================================================

SELECT
    DepartmentID,
    COUNT(*) AS NumberOfEmployees
FROM Employees
GROUP BY DepartmentID;


-- =====================================================
-- QUESTION 20: Find the average salary in each department
-- Each department gets its own average salary
-- =====================================================

SELECT
    DepartmentID,
    AVG(Salary) AS AverageSalary
FROM Employees
GROUP BY DepartmentID;


-- =====================================================
-- QUESTION 21: Find the highest salary in each department
-- MAX() finds the highest salary inside each department
-- =====================================================

SELECT
    DepartmentID,
    MAX(Salary) AS HighestSalary
FROM Employees
GROUP BY DepartmentID;


-- =====================================================
-- QUESTION 22: Show departments having more than one employee
-- HAVING filters groups after GROUP BY
-- =====================================================

SELECT
    DepartmentID,
    COUNT(*) AS NumberOfEmployees
FROM Employees
GROUP BY DepartmentID
HAVING COUNT(*) > 1;


-- =====================================================
-- QUESTION 26: Display each employee with department name
-- JOIN connects Employees and Departments
-- ON tells SQL how the tables match
-- =====================================================

SELECT
    Employees.EmployeeID,
    Employees.FirstName,
    Employees.LastName,
    Departments.DepartmentName
FROM Employees
JOIN Departments
    ON Employees.DepartmentID = Departments.DepartmentID;


-- =====================================================
-- QUESTION 27:
-- Display employee name, department name and location
-- =====================================================

SELECT
    Employees.FirstName,
    Employees.LastName,
    Departments.DepartmentName,
    Departments.Location
FROM Employees
JOIN Departments
    ON Employees.DepartmentID = Departments.DepartmentID;


-- =====================================================
-- QUESTION 28:
-- Count employees in each department using a JOIN
-- =====================================================

SELECT
    Departments.DepartmentName,
    COUNT(Employees.EmployeeID) AS NumberOfEmployees
FROM Departments
JOIN Employees
    ON Departments.DepartmentID = Employees.DepartmentID
GROUP BY
    Departments.DepartmentID,
    Departments.DepartmentName;


-- =====================================================
-- QUESTION 29:
-- Display all departments, even without employees
-- LEFT JOIN keeps every department
-- =====================================================

SELECT
    Departments.DepartmentID,
    Departments.DepartmentName,
    Departments.Location,
    Employees.FirstName,
    Employees.LastName
FROM Departments
LEFT JOIN Employees
    ON Departments.DepartmentID = Employees.DepartmentID;


-- =====================================================
-- QUESTION 30:
-- Find average salary for each department using a JOIN
-- =====================================================

SELECT
    Departments.DepartmentName,
    AVG(Employees.Salary) AS AverageSalary
FROM Departments
LEFT JOIN Employees
    ON Departments.DepartmentID = Employees.DepartmentID
GROUP BY
    Departments.DepartmentID,
    Departments.DepartmentName;


-- =====================================================
-- QUESTION 31:
-- Display employees working in departments in Berlin
-- =====================================================

SELECT
    Employees.EmployeeID,
    Employees.FirstName,
    Employees.LastName,
    Departments.DepartmentName,
    Departments.Location
FROM Employees
JOIN Departments
    ON Employees.DepartmentID = Departments.DepartmentID
WHERE Departments.Location = 'Berlin';


-- =====================================================
-- QUESTION 32:
-- Display employees working in the IT department
-- Use a JOIN instead of filtering by DepartmentID
-- =====================================================

SELECT
    Employees.EmployeeID,
    Employees.FirstName,
    Employees.LastName,
    Employees.Salary,
    Departments.DepartmentName
FROM Employees
JOIN Departments
    ON Employees.DepartmentID = Departments.DepartmentID
WHERE Departments.DepartmentName = 'IT';

-- =====================================================
-- QUESTION 23: Increase salaries of IT employees by 5%
-- IT has DepartmentID 3
-- Salary * 1.05 adds 5%
-- =====================================================

UPDATE Employees
SET Salary = ROUND(Salary * 1.05)
WHERE DepartmentID = 3;

-- Check the changed IT salaries
SELECT *
FROM Employees
WHERE DepartmentID = 3;


-- =====================================================
-- QUESTION 24: Change EmployeeID 109's city to Brussels
-- UPDATE changes existing data
-- SET gives the new value
-- WHERE chooses the correct employee
-- =====================================================

UPDATE Employees
SET City = 'Brussels'
WHERE EmployeeID = 109;

-- Check EmployeeID 109
SELECT *
FROM Employees
WHERE EmployeeID = 109;


-- =====================================================
-- QUESTION 25: Delete employees earning below 48,000
-- DELETE FROM removes complete rows
-- Salary exactly 48,000 is not deleted
-- =====================================================

DELETE FROM Employees
WHERE Salary < 48000;

-- Check the remaining employees
SELECT *
FROM Employees;

