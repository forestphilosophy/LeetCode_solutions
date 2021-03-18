SELECT Employee
FROM
    (SELECT t1.Name AS Manager, t1.Salary AS Manager_Salary, t2.Name AS Employee, t2.Salary AS Employee_Salary
    FROM Employee t1
    LEFT JOIN Employee t2
    ON t2.ManagerId = t1.Id
    WHERE t1.Salary IS NOT NULL
    AND t2.Name IS NOT NULL) AS Result
    
WHERE Manager_Salary < Employee_Salary;
