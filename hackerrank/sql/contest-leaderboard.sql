/* https://www.hackerrank.com/challenges/contest-leaderboard/problem
 */
SELECT Hackers.hacker_id, name, SUM(MaxScore)
FROM Hackers, (
    SELECT hacker_id, challenge_id, MAX(score) as MaxScore
    FROM Submissions
    WHERE score > 0
    GROUP BY hacker_id, challenge_id
) AS SubmissionsMaxScore
WHERE Hackers.hacker_id = SubmissionsMaxScore.hacker_id
GROUP BY Hackers.hacker_id, name
HAVING SUM(MaxScore) > 0
ORDER BY SUM(MaxScore) DESC, Hackers.hacker_id;