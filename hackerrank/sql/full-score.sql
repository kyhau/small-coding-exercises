/* https://www.hackerrank.com/challenges/full-score/problem
 */
SELECT Hackers.hacker_id, name
FROM Hackers, (
    SELECT hacker_id, COUNT(Submissions.challenge_id) as ChallengeCounts
    FROM Submissions, (
        SELECT challenge_id, score
        FROM Challenges, Difficulty
        WHERE Challenges.difficulty_level = Difficulty.difficulty_level
    ) AS FullScore
    WHERE Submissions.challenge_id = FullScore.challenge_id
    AND Submissions.score = FullScore.score
    GROUP BY hacker_id
    HAVING ChallengeCounts > 1
) AS T
WHERE Hackers.hacker_id = T.hacker_id
ORDER BY T.ChallengeCounts DESC, Hackers.hacker_id;
