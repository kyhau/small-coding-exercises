/* https://www.hackerrank.com/challenges/symmetric-pairs/problem
 */

SELECT A.X, A.Y
FROM Functions AS A, Functions AS B
WHERE A.X = B.Y AND B.X = A.Y AND A.X < A.Y
UNION
SELECT X, Y
FROM Functions
WHERE X = Y
GROUP BY X, Y
HAVING Count(X) > 1
ORDER BY X