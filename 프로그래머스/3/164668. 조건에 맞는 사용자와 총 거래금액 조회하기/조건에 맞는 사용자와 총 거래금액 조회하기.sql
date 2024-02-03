-- 코드를 입력하세요
SELECT ugu.user_id, ugu.nickname, SUM(ugb.PRICE) AS TOTAL_SALES
FROM USED_GOODS_USER ugu, used_goods_board ugb
WHERE ugb.WRITER_ID = ugu.USER_ID AND ugb.STATUS = 'DONE'
GROUP BY ugu.USER_ID, ugu.nickname
HAVING SUM(ugb.PRICE) >= 700000
ORDER BY TOTAL_SALES;
