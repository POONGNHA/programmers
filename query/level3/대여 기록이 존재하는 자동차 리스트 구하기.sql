-- 문제 설명
-- 다음은 어느 자동차 대여 회사에서 대여 중인 자동차들의 정보를 담은 CAR_RENTAL_COMPANY_CAR 테이블과 자동차 대여 기록 정보를 담은 CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블입니다. CAR_RENTAL_COMPANY_CAR 테이블은 아래와 같은 구조로 되어있으며, CAR_ID, CAR_TYPE, DAILY_FEE, OPTIONS 는 각각 자동차 ID, 자동차 종류, 일일 대여 요금(원), 자동차 옵션 리스트를 나타냅니다.

-- Column name	Type	Nullable
-- CAR_ID	INTEGER	FALSE
-- CAR_TYPE	VARCHAR(255)	FALSE
-- DAILY_FEE	INTEGER	FALSE
-- OPTIONS	VARCHAR(255)	FALSE
-- 자동차 종류는 '세단', 'SUV', '승합차', '트럭', '리무진' 이 있습니다. 자동차 옵션 리스트는 콤마(',')로 구분된 키워드 리스트(예: '열선시트', '스마트키', '주차감지센서')로 되어있으며, 키워드 종류는 '주차감지센서', '스마트키', '네비게이션', '통풍시트', '열선시트', '후방카메라', '가죽시트' 가 있습니다.

-- CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블은 아래와 같은 구조로 되어있으며, HISTORY_ID, CAR_ID, START_DATE, END_DATE 는 각각 자동차 대여 기록 ID, 자동차 ID, 대여 시작일, 대여 종료일을 나타냅니다.

-- Column name	Type	Nullable
-- HISTORY_ID	INTEGER	FALSE
-- CAR_ID	INTEGER	FALSE
-- START_DATE	DATE	FALSE
-- END_DATE	DATE	FALSE
-- 문제
-- CAR_RENTAL_COMPANY_CAR 테이블과 CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블에서 자동차 종류가 '세단'인 자동차들 중 10월에 대여를 시작한 기록이 있는 자동차 ID 리스트를 출력하는 SQL문을 작성해주세요. 자동차 ID 리스트는 중복이 없어야 하며, 자동차 ID를 기준으로 내림차순 정렬해주세요.

-- 예시
-- 예를 들어 CAR_RENTAL_COMPANY_CAR 테이블이 다음과 같고

-- CAR_ID	CAR_TYPE	DAILY_FEE	OPTIONS
-- 1	세단	16000	가죽시트,열선시트,후방카메라
-- 2	SUV	14000	스마트키,네비게이션,열선시트
-- 3	세단	22000	주차감지센서,후방카메라,가죽시트
-- 4	세단	12000	주차감지센서
-- CAR_RENTAL_COMPANY_RENTAL_HISTORY 테이블이 다음과 같다면

-- HISTORY_ID	CAR_ID	START_DATE	END_DATE
-- 1	4	2022-09-27	2022-09-27
-- 2	3	2022-10-03	2022-10-04
-- 3	2	2022-10-05	2022-10-05
-- 4	1	2022-10-11	2022-10-14
-- 5	3	2022-10-13	2022-10-15
-- 10월에 대여를 시작한 기록이 있는 '세단' 종류의 자동차는 자동차 ID가 1, 3 인 자동차이고, 자동차 ID를 기준으로 내림차순 정렬하면 다음과 같이 나와야 합니다.

-- CAR_ID
-- 3
-- 1

-- 나의 코드
SELECT CAR_RENTAL_COMPANY_CAR.CAR_ID
from CAR_RENTAL_COMPANY_CAR 
join CAR_RENTAL_COMPANY_RENTAL_HISTORY 
on CAR_RENTAL_COMPANY_RENTAL_HISTORY.CAR_ID = CAR_RENTAL_COMPANY_CAR.CAR_ID
where CAR_TYPE = '세단' and CAR_RENTAL_COMPANY_RENTAL_HISTORY.START_DATE like '%2022-10%'
group by CAR_ID
order by CAR_ID desc