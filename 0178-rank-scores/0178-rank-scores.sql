# Write your MySQL query statement below
SELECT s.score as Score, DENSE_RANK() OVER (ORDER BY s.score DESC) as 'rank'
FROM Scores s;