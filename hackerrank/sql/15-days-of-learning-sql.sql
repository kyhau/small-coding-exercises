/* https://www.hackerrank.com/challenges/15-days-of-learning-sql/problem
 */
SELECT
  submission_date,
  (SELECT COUNT(DISTINCT hacker_id)
   FROM Submissions S2
   WHERE S2.submission_date = S1.submission_date
   AND (
       SELECT COUNT(DISTINCT S3.submission_date)
       FROM Submissions S3
       WHERE S3.hacker_id = S2.hacker_id
       AND S3.submission_date < S1.submission_date) = DATEDIFF(S1.submission_date , '2016-03-01')
  ),
  (SELECT hacker_id
   FROM Submissions S2
   WHERE S2.submission_date = S1.submission_date
   GROUP BY hacker_id ORDER BY COUNT(submission_id) DESC, hacker_id LIMIT 1
  ) AS MaxSubmissionHackerID,
  (SELECT name FROM HACKERS WHERE hacker_id = MaxSubmissionHackerID)
FROM (SELECT DISTINCT submission_date FROM Submissions) S1
GROUP BY submission_date;
