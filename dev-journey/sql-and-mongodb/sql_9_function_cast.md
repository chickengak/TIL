# 예제를 통한 실전 구문
### Procedure와 Function의 차이
Procedure는 리턴이 없고 Function은 리턴이 있다. 물론 Procedure도 변수로 OUT 받으면 비슷하게 구현은 가능하나 명시적 RETURN은 없다.

## Function

```sql
-- Q1. 문자열의 길이를 리턴하는 사용자 함수

CREATE FUNCTION `Func01` (input_string VARCHAR(100))
RETURNS INTEGER
DETERMINISTIC
BEGIN
    RETURN CHAR_LENGTH(input_string);
END

SELECT Func01('ABCDEFG');
```
### DETERMINISTIC
- 정의: DETERMINISTIC 키워드는 함수가 동일한 입력값에 대해 항상 동일한 결과를 반환한다는 것을 나타냅니다.
- 역할: 이 키워드는 데이터베이스 최적화 프로세스에서 중요한 역할을 합니다. 데이터베이스 시스템은 DETERMINISTIC 함수의 결과를 캐시하고, 동일한 입력에 대해 함수를 다시 호출할 필요 없이 이전 결과를 재사용할 수 있습니다.
- 선택 기준: 수학적 계산이나 문자열 변환 같이 항상 같은 입력에 대해 동일한 결과를 반환할 때 DETERMINISTIC. 함수의 결과가 입력값 뿐만 아니라 다른 요소(예: 시스템 시간, 데이터베이스의 다른 행의 상태)에 따라 달라질 수 있을 때 NOT DETERMINISTIC.

### DETERMINISTIC 이외의 옵션
- **NOT DETERMINISTIC**: 함수가 동일한 입력에 대해 다른 결과를 반환할 수 있음을 나타냅니다.
- **READS SQL DATA**: 함수가 데이터를 읽기만 하고 변경하지 않음을 나타냅니다. 주로 조회 목적의 함수에 사용.
- **MODIFIES SQL DATA**: 함수가 데이터를 변경할 수 있음을 나타냅니다. 삽입, 갱신, 삭제 등 데이터를 수정하는 로직이 포함된 함수에 적합.
- **NO SQL**: 함수가 SQL 문을 전혀 사용하지 않음을 나타냅니다.

<br>

```sql
-- Q2. 문자열을 첫글자만 대문자인 문자열로 반환

CREATE FUNCTION `Func02`(input_string VARCHAR(100))
RETURNS VARCHAR(100)
DETERMINISTIC
BEGIN
	RETURN CONCAT(UPPER(SUBSTR(input_string, 1, 1)),LOWER(SUBSTR(input_string, 2)));
END

SELECT Func02('abcdeFG');


-- Q3. 두 숫자의 합을 리턴하는 함수

CREATE FUNCTION `Func03` (input1 DECIMAL(10,2), input2 DECIMAL(10,2))
RETURNS DECIMAL(10,2)
DETERMINISTIC
BEGIN
    RETURN input1 + input2;
END

SELECT Func03(4325, 321);


-- Q4. 최대값 리턴 함수

CREATE FUNCTION `Func04` (input1 DECIMAL(10,2), input2 DECIMAL(10,2))
RETURNS DECIMAL(10,2)
DETERMINISTIC
BEGIN
    RETURN GREATEST(input1, input2);
END

SELECT Func03(4325, 321);


-- Q5. 연도별 나이 계산 함수

CREATE FUNCTION `Func05` (input_date DATE)
RETURNS INT
DETERMINISTIC
BEGIN
    RETURN YEAR(NOW()) - YEAR(input_date);
END

SELECT Func05('2012-02-01');


-- Q6. 문자열 반전 함수

CREATE FUNCTION `Func06` (input_string VARCHAR(100))
RETURNS VARCHAR(100)
DETERMINISTIC
BEGIN
    RETURN REVERSE(input_string);
END

SELECT Func06('ABCDEFG');

```

<br>

## CAST　CONVERT
https://dev.mysql.com/doc/refman/8.0/en/cast-functions.html  

CAST(expr AS type [ARRAY])  
CAST(timestamp_value AT TIME ZONE timezone_specifier AS DATETIME[(precision)])  

CONVERT(expr,type)  
CONVERT(expr USING transcoding_name)  

```sql
-- 문자열을 부호있는 정수로

SELECT CAST ('123' AS SIGNED INTEGER);


-- 실수 문자열을 부호없는 정수로

SELECT CAST ('123.45' AS UNSIGNED INTEGER);


-- 날짜 문자열을 날짜로

SELECT CAST ('2020-1-23' AS DATE);


-- 숫자를 문자열로

SELECT CAST (1234 AS CHAR);


-- 문자열을 실수로

SELECT CAST ('1234.56' AS DECIMAL(10,2));
SELECT CAST ('1234.56' AS DECIMAL(5,2));            # 999.99 오버플로우


-- 날짜를 문자열로 변환

SELECT CAST('2023-12-25' AS CHAR);


-- 십진수를 이진수로 변환

SELECT CAST(15 AS BINARY);


-- 이진수를 십진수로 변환

SELECT CAST(b'1010' AS SIGNED INT);





-- 날짜를 다른 날짜/시간 포맷으로 변환

SELECT CONVERT('2023-12-31 12:34:56', DATE);


-- 문자열을 바이너리 타입으로 변환

SELECT CONVERT('hello' USING BINARY);


-- 변수를 바이너리 변환

SET @my_string = 'hello';
SELECT CONVERT(@my_string USING BINARY);


-- 테이블의 컬럼을 바이너리로 변환

SELECT CONVERT(ename USING BINARY)          # 압축
FROM emp;


```


