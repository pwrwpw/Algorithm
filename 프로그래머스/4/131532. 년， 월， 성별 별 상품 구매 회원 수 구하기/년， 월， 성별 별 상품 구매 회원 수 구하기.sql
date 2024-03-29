-- 코드를 입력하세요
SELECT TO_CHAR(os.SALES_DATE,'YYYY') AS YEAR, TO_NUMBER(TO_CHAR(os.SALES_DATE,'MM')) AS MONTH,us.GENDER as GENDER,COUNT(distinct os.USER_ID) AS USERS
FROM USER_INFO us,ONLINE_SALE os
WHERE us.USER_ID = os.USER_ID AND us.gender is not null
GROUP BY TO_CHAR(os.SALES_DATE, 'YYYY'),
         TO_CHAR(os.SALES_DATE, 'MM'),
         us.GENDER
ORDER BY 1,2,3