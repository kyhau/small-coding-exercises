/* https://www.hackerrank.com/challenges/placements/problem
 */
SELECT Students.Name
FROM Students
JOIN Friends ON Students.Id = Friends.ID
JOIN Packages AS P1 ON P1.ID = Students.ID
JOIN Packages AS P2 ON P2.ID = Friends.Friend_ID
WHERE P1.Salary < P2.Salary
ORDER BY P2.Salary