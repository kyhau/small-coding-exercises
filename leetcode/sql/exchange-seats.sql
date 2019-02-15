/* https://leetcode.com/problems/exchange-seats
 */

SELECT
	CASE
		WHEN seat.id % 2 <> 0 AND seat.id = (SELECT COUNT(*) FROM seat) THEN seat.id
		WHEN seat.id % 2 = 0 THEN seat.id - 1
		ELSE
			seat.id + 1
	END as id,
	student
FROM seat
ORDER BY id;

/* Option 2 */
SELECT IF (id % 2 <> 0, IF (id <> (SELECT MAX(id) FROM seat), id+1, id), id-1) id, student
FROM seat
ORDER BY id;