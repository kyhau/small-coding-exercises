/* https://www.hackerrank.com/challenges/the-company/problem
 */

SELECT Company.company_code, Company.founder, LMCounts, SMCOunts, MCounts, ECounts
FROM Company,
(
    SELECT company_code, COUNT(DISTINCT lead_manager_code) as LMCounts
    FROM Lead_Manager
    GROUP BY company_code
) AS LeadManagers,
(
    SELECT company_code, COUNT(DISTINCT senior_manager_code) as SMCounts
    FROM Senior_Manager
    GROUP BY company_code
) AS SeniorManagers,
(
    SELECT company_code, COUNT(DISTINCT manager_code) as MCounts
    FROM Manager
    GROUP BY company_code
) AS Managers,
(
    SELECT company_code, COUNT(DISTINCT employee_code) as ECounts
    FROM Employee
    GROUP BY company_code
) AS Employees
WHERE Company.company_code = LeadManagers.company_code
AND Company.company_code = SeniorManagers.company_code
AND Company.company_code = Managers.company_code
AND Company.company_code = Employees.company_code
ORDER BY Company.company_code