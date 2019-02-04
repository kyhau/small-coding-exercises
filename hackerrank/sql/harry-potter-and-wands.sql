/* https://www.hackerrank.com/challenges/harry-potter-and-wands/problem
 */
SELECT id, age, MinCoinsNeeded, T.power
FROM Wands, (
    SELECT power, age, Min(coins_needed) AS MinCoinsNeeded, Wands.code
    FROM Wands, Wands_Property
    WHERE Wands.code = Wands_Property.code
    AND is_evil = 0
    GROUP BY power, age, code
) AS T
WHERE Wands.code = T.code
AND Wands.coins_needed = MinCoinsNeeded
ORDER BY T.power DESC, age DESC
