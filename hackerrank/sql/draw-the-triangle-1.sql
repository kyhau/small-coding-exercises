/* https://www.hackerrank.com/challenges/draw-the-triangle-1/problem

* * * * *
* * * *
* * *
* *
*

 */

SET @number = 21;
SELECT REPEAT('* ', @number := @number - 1)
FROM information_schema.tables
LIMIT 20;