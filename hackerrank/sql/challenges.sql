/* https://www.hackerrank.com/challenges/challenges/problem
 */
SELECT Hackers.hacker_id, name, COUNT(challenge_id) as NumChallenges
FROM Hackers, Challenges
WHERE Hackers.hacker_id = Challenges.hacker_id
GROUP BY Hackers.hacker_id, name
HAVING NumChallenges = (
    SELECT COUNT(challenge_id) AS NumChallenges
    FROM Challenges
    GROUP BY hacker_id
    ORDER BY NumChallenges DESC LIMIT 1
)
OR NumChallenges NOT IN (
    SELECT COUNT(c2.challenge_id)
    FROM Challenges AS c2
    GROUP BY c2.hacker_id
    HAVING c2.hacker_id <> Hackers.hacker_id
)
ORDER BY NumChallenges DESC, Hackers.hacker_id;
