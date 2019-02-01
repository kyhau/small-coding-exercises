/* https://www.hackerrank.com/challenges/weather-observation-station-20/problem
 */

SET @rowindex := -1;

SELECT ROUND(AVG(s.lat_n), 4)
FROM (
    SELECT @rowindex:=@rowindex + 1 AS rowindex, lat_n
    FROM station
    ORDER BY lat_n
) AS s
WHERE
s.rowindex IN (FLOOR(@rowindex / 2) , CEIL(@rowindex / 2));