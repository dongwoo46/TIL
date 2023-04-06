-- users table 생성
CREATE TABLE users (
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    age INTEGER NOT NULL,
    country TEXT NOT NULL,
    phone TEXT NOT NULL,
    balance INTEGER NOT NULL
);

SELECT COUNT(*) FROM users;

SELECT avg(balance) FROM users;

SELECT country,avg(balance) FROM users where country="경상도";

-- 지역별 평균 balance구하기
SELECT country, avg(balance) FROM users GROUP BY country;
-- + 정렬까지
SELECT country, avg(balance) FROM users GROUP BY country ORDER BY avg(balance) DESC;

-- 나이가 30살 이상인 사람들의 평균 나이
SELECT AVG(age) FROM users WHERE age>=30;

-- 각 지역별로 몇명씩 살고있는지 조회하기
SELECT country,COUNT(*) FROM users GROUP BY country;

-- 각 성씨가 몇 명씩 있는지 조회하기
SELECT last_name, COUNT(*) FROM users GROUP BY last_name;
-- 각 성씨가 몇 명씩 있는지 조회하기 + AS 키워드로 컬럼명 임시로 변경해 조회하기
SELECT last_name, COUNT(*) AS number_of_name FROM users GROUP BY last_name;

CREATE TABLE classmates (
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    address TEXT NOT NULL
);

INSERT INTO classmates (name, age, address)
VALUES ('홍길동',23,'서울');
-- INSERT INTO classmates VALUES('홍길동',23,'서울');

INSERT INTO classmates 
VALUES 
    ('김철수', 30, '경기'),
    ('이영미', 31, '강원'),
    ('박진성', 26, '전라'),
    ('최지수', 12, '충청'),
    ('정요한', 28, '경상');

UPDATE classmates SET name='김철수한무두루미', address='제주도' WHERE rowid =2;

DELETE FROM classmates WHERE rowid=5;
-- DELETE FROM classmates WHERE name='최지수';

-- 이름에 '영'이 포함되는 데이터 삭제하기
DELETE FROM classmates WHERE name LIKE '%영%';

-- 테이블의 모든 데이터 삭제하기
DELETE FROM classmates;



