/* https://www.hackerrank.com/challenges/interviews/problem
 */

SELECT Contests.contest_id, hacker_id, name,
  SUM(total_submissions),
  SUM(total_accepted_submissions),
  SUM(total_views),
  SUM(total_unique_views)
FROM Contests
JOIN Colleges ON Contests.contest_id = Colleges.contest_id
JOIN Challenges ON Colleges.college_id = Challenges.college_id
LEFT JOIN (
    SELECT challenge_id, SUM(total_submissions) AS total_submissions,
      SUM(total_accepted_submissions) AS total_accepted_submissions
    FROM Submission_Stats
    GROUP BY challenge_id
) AS SG ON Challenges.challenge_id = SG.challenge_id
LEFT JOIN (
    SELECT challenge_id, SUM(total_views) AS total_views,
      SUM(total_unique_views) AS total_unique_views
    FROM View_Stats
    GROUP BY challenge_id
) AS VG ON Challenges.challenge_id = VG.challenge_id
GROUP BY Contests.contest_id, Contests.hacker_id, Contests.name
HAVING SUM(SG.total_submissions) +
       SUM(SG.total_accepted_submissions) +
       SUM(VG.total_views) +
       SUM(VG.total_unique_views) > 0
ORDER BY Contests.contest_id;
