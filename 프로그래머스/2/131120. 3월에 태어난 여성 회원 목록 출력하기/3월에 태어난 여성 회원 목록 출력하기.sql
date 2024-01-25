-- 코드를 입력하세요
SELECT member_id,member_name,gender,to_char(date_of_birth,'yyyy-mm-dd') as DATE_OF_BIRTH
FROM MEMBER_PROFILE
WHERE to_char(DATE_OF_BIRTH,'mm') = '03' and GENDER = 'W' and TLNO is NOT NULL
order by member_id asc;