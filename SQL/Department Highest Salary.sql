Select MaxSalary.Department, CombinedTable.Employee, CombinedTable.Salary
FROM
    (SELECT e.Salary,e.Name AS Employee,d.Name AS Department
    FROM Employee e
    JOIN Department d
    ON d.Id = e.DepartmentId) CombinedTable 
JOIN
    (SELECT d.Name AS Department, MAX(e.Salary) AS Salary
    FROM Employee e
    JOIN Department d
    ON d.Id = e.DepartmentId 
    GROUP BY d.Name) MaxSalary
ON CombinedTable.Department = MaxSalary.Department
WHERE CombinedTable.Salary = MaxSalary.Salary
