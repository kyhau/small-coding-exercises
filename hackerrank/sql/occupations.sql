/* https://www.hackerrank.com/challenges/occupations/problem
 */

SET @n1=0, @n2=0, @n3=0, @n4=0;
SELECT MIN(Doctor), MIN(Professor), MIN(Singer), MIN(Actor)
FROM (
    SELECT
      CASE Occupation
        WHEN 'Doctor' THEN @n1:=@n1+1
        WHEN 'Professor' THEN @n2:=@n2+1
        WHEN 'Singer' THEN @n3:=@n3+1
        WHEN 'Actor' THEN @n4:=@n4+1
      END AS RowIndex,
      CASE WHEN Occupation = 'Doctor' THEN Name END AS Doctor,
      CASE WHEN Occupation = 'Professor' THEN Name END AS Professor,
      CASE WHEN Occupation = 'Singer' THEN Name END AS Singer,
      CASE WHEN Occupation = 'Actor' THEN Name END AS Actor
    FROM OCCUPATIONS ORDER BY Name
) AS NewPivotTable
GROUP BY RowIndex;