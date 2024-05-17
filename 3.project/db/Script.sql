-- MYSQL의 데이터 형식
-- 데이터 형식은 크게 숫자형, 문자형, 날짜형이 있음

-- 실제로 저장될 데이터의 형태가 다양하기 때문에 이를 효율적으로 저장하기 위해 위의 데이터 형식에서 
-- 세부적으로 다시 여러 데이터 형식으로 나뉨
-- > 예) 사람의 이름을 저장하기 위해 100글자를 저장할 칸을 준비하는 것은 비효율적임

-- 정수형
-- -- TINYINT (숫자 범위 : -128 ~ 127)
-- -- SMALLINT (숫자 범위 : -32768 ~ 32767)
-- -- INT (숫자 범위 : 약 -21억 ~ 21억)
-- -- BIGINT (숫자 범위 : 약 -900경 ~ 900경)

CREATE TABLE tbl_type(
	tinyint_col TINYINT,
	smallint_col SMALLINT,
	int_col INT,
	bigint_col BIGINT
	);
	
-- 각 열의 최댓값까지는 이상 없이 입력 가능
INSERT INTO tbl_type VALUES (127, 32767, 2147483647, 9000000000000000000);
SELECT * FROM tbl_type;

-- 최댓값에 0을 더 붙여서 입력해보기
INSERT INTO tbl_type VALUES (1270, 327670, 21474836470, 90000000000000000000);
-- Out of range 에러는 입력값의 범위를 벗어났다는 뜻

-- 문자형
-- > 문자형은 글자를 저장하기 위해 사용
-- > 입력할 최대 글자의 개수를 지정해야 함
-- -- CHAR(개수)
-- -- VARCHAR(개수)

-- CHAR는 Character의 약자로, 고정길이 문자형이라고 부름
-- > 자릿수가 고정됨
-- > 예) CHAR(10) 에 "가나다" 3글자만 저장해도 10자리를 모두 확보한 후에 앞의 3자리만 사용하고 뒤의 7자리는 낭비하게 됨
-- VARCHAR는 가변길이 문자형으로, "가나다" 3글자를 저장하면 3자리만 사용함(Variable Character)

-- VARCHAR가 CHAR보다 공간을 더 효율적으로 사용할 수 있지만 MYSQL의 처리속도는 CHAR가 더 빠름
-- 예) 거주지역 컬럼에 데이터가 서울/경기/부산/경북/전남 과 같이 모두 2글자로 일정한 경우에는
-- > CHAR(2) 로 설정하는 것이 더 좋음
-- > 반면에 가수 이름은 글자 수가 다양하기 때문에 VARCHAR로 설정하는 것이 더 좋을 수 있음

-- 위에서 배운 내용을 바탕으로 member 테이블 생성 코드를 다시 작성한다면
CREATE TABLE member -- 회원 테이블
(mem_id 	CHAR(8) NOT NULL PRIMARY KEY, -- 사용자 아이디(PK)
 mem_name	VARCHAR(10) NOT NULL,	-- 이름
 mem_number TINYINT NOT NULL, -- 인원 수
 addr		CHAR(2) NOT NULL, -- 지역(경기, 서울, 경남 처럼 2글자만 입력)
 phnoe1		CHAR(3), -- 연락처의 국번(02, 031, 051 등)
 phone2 	CHAR(8), -- 연락처의 나머지 전화번호(하이픈 제외)
 height 	TINYINT UNSIGNED, -- 평균 키 : UNSIGNED = 부호 제거(음수 제거)
 debut_date DATE -- 데뷔 일자
 );
 
-- 전화번호는 숫자로서의 의미가 없기 때문에 문자열로 지정
-- > 숫자로서의 의미를 가지기 위해서는
-- --> 더하기/빼기 등의 연산에 의미가 있다
-- --> 크다/작다 또는 순서에 의미가 있다

-- 대량의 데이터 형식
-- > CHAR는 최대 255까지, VARCHAR는 최대 16383자 까지 지정이 가능
-- > 즉, 더 큰 값을 가지는 데이터는 저장할 수 없음

-- 대량 데이터의 형식
-- -- TEXT (최대 65535자)
-- -- LONGTEXT (약 42억자)
-- -- > 소설이나 영화 대본 등의 대량의 내용을 자장할 때 사용

-- -- BLOB
-- -- > Binary Long Object의 약자
-- -- > 이미지, 동영상 등의 데이터(이진 데이터)를 저장할 때 사용
-- -- LONGBLOB
-- -- > LONGTEXT 및 LONGBLOB는 최대 4GB까지 입력 가능

-- 넷플릭스 같은 동영상을 다루는 사이트의 테이블 구성
CREATE DATABASE netflix_db;
USE netflix_db;
CREATE TABLE movie
(movie_id 		INT,
 movie_title 	VARCHAR(30),
 movie_director VARCHAR(20),
 movie_star 	VARCHAR(20),
 movie_script	LONGTEXT,
 movie_film 	LONGBLOB
 );

-- 실수형
-- > 소수점이 있는 숫자를 저장할 때 사용
-- -- FLOAT (소수점 아래 7자리 까지 표현)
-- -- DOUBLE (소수점 아래 15자리까지 표현)

-- 날짜형
-- > 날짜 및 시간을 저장할 때 사용
-- DATE (날짜만 저장, YYYY-MM-DD)형식으로 사용
-- TIME (시간만 저장, HH:MM:SS) 형식으로 사용
-- DATETIME (날짜 및 시간을 저장, YYYY-MM-DD HH:MM:SS) 형식으로 사용