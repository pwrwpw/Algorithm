-- 코드를 입력하세요
SELECT SUBSTR(PRICE,1,1) * 10000 AS PRICE_GROUP, COUNT(*) AS PRODUCETS
FROM PRODUCT
GROUP BY SUBSTR(PRICE,1,1) * 10000
ORDER BY SUBSTR(PRICE,1,1) * 10000