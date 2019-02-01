/* https://www.hackerrank.com/challenges/the-report/problem */

SELECT
CASE
    WHEN G.Grade < 8 THEN NULL
    ELSE S.Name
END,
G.Grade, S.Marks
FROM Students AS S
JOIN Grades AS G
ON S.Marks BETWEEN G.Min_Mark AND G.Max_Mark
ORDER BY G.Grade DESC, S.Name ASC;
