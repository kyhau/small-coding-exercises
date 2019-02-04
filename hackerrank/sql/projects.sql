/* https://www.hackerrank.com/challenges/projects/problem
 */

SELECT Start_Date, Min(End_Date)
FROM
(SELECT Start_Date FROM Projects WHERE Start_Date NOT IN (SELECT End_Date FROM Projects)) AS T1,
(SELECT End_Date FROM Projects WHERE End_Date NOT IN (SELECT Start_Date FROM Projects)) AS T2
WHERE Start_Date < End_Date
GROUP BY Start_Date
ORDER BY DATEDIFF(Min(End_Date), Start_Date), Start_Date