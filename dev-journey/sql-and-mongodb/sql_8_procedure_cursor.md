# 예제를 통한 실전 구문

## Procedure
프로시저는 일련의 SQL 명령문들을 하나의 실행 가능한 단위로 묶은 것으로, 데이터베이스 내에서 반복적으로 수행되는 작업들을 자동화하는 데 사용됩니다.

프로시저의 특징
1. 재사용 가능: 한 번 생성되면 여러 번 호출될 수 있습니다.
2. 효율적인 성능: DBMS가 프로시저를 최적화하여 실행할 수 있습니다.
3. 보안: 사용자가 데이터에 직접 접근하는 것을 제한하고 프로시저를 통해서만 데이터를 조작할 수 있도록 함으로써 보안을 강화할 수 있습니다.
4. 유지보수: 중앙 집중식 코드 관리가 가능하여 유지보수가 용이합니다.
5. 에러 감소: 일관된 방법으로 데이터를 처리하므로 오류의 가능성을 줄일 수 있습니다.


```sql
-- 연습할 ptable 생성
CREATE TABLE ptable
AS
SELECT * FROM emp;
```

### Procedure로 데이터 넣기
```sql
CREATE PROCEDURE `ptable01` (IN input_empno INT, IN input_ename VARCHAR(20))
BEGIN
	INSERT INTO ptable(empno, ename) VALUES(input_empno, input_ename);
END

call ptable01(1234, 'hong');

SELECT * FROM ptable;


CREATE DEFINER=`root`@`localhost` PROCEDURE `ptable01`(input_empno INT, input_ename VARCHAR(20))
BEGIN
	INSERT INTO ptable(empno, ename) VALUES(input_empno, input_ename);
END
```
**DEFINER의 역할**
1. 소유권 지정: 프로시저나 뷰 등을 생성한 사용자를 명시적으로 지정합니다.
2. 보안 관리: 해당 프로시저를 실행할 때 DEFINER의 권한으로 실행됩니다. 이는 데이터베이스의 보안과 접근 제어에 중요한 역할을 합니다. 데이터베이스의 무결성과 보안 정책을 유지하는 데 도움이 됩니다.
3. 권한 위임: 다른 사용자가 프로시저를 실행하더라도, DEFINER에 지정된 사용자의 권한으로 실행됩니다. 이를 통해 데이터베이스 관리자는 특정 작업에 대해 제한된 권한을 가진 사용자들에게 더 넓은 권한을 부여할 수 있습니다.

**INVOKER 권한**
1. 정의: INVOKER 권한을 사용하면, 저장된 프로시저나 뷰는 그것을 호출하는 사용자의 권한으로 실행됩니다.
2. 사용 사례: 이 옵션은 호출자의 권한에 따라 다르게 작동해야 하는 경우에 적합합니다.
3. 보안 측면: INVOKER 권한을 갖는 객체는 호출하는 사용자의 권한에 제한되므로, 보안이 더 엄격하게 관리될 수 있습니다.

### Procedure로 데이터 삭제
```sql
CREATE PROCEDURE `ptable02` (IN input_empno INT)
BEGIN
	DELETE FROM ptable WHERE empno = input_empno;
END

CALL ptable02(1234);
```

### Procedure로 데이터 수정
```sql
CREATE PROCEDURE `ptable03` (IN input_empno INT, IN input_sal DECIMAL(7,2))
BEGIN
    UPDATE ptable
    SET sal = input_sal
    WHERE empno = input_empno;
END

CALL ptable03(7499, 4000);
```

### Procedure로 데이터 추출
```sql
-- FORD의 모든 정보를 추출하는 프로시저를 만들자
CREATE PROCEDURE `ptable04` (IN input_ename VARCHAR(20))
BEGIN
    SELECT *
    FROM ptable
    WHERE ename = input_ename;
END

CALL ptable04('FORD');

SET @temp = 'FORD';
CALL ptable04(@temp);
```

### Procedure로 카운트하기
```sql
CREATE PROCEDURE `ptable05` (OUT input_variable INT)
BEGIN
    SELECT COUNT(*) INTO input_variable
    FROM ptable;
END

CALL ptable05(@temp_variable);
SELECT @temp_variable;
```

### Procedure의 바람직한 IN, OUT 예시
```sql
CREATE PROCEDURE citycount (IN country CHAR(3), OUT cities INT)
BEGIN
    SELECT COUNT(*) INTO cities FROM world.city
    WHERE CountryCode = country;
END

CALL citycount('JPN', @cities);
SELECT @cities;
```


### CURSOR
https://dev.mysql.com/doc/refman/8.0/en/cursors.html  
Cursor = DataSet = ResultSet 다 같은걸 의미. 한 줄이상의 엔티티 결과가 있다.

SQL에서의 커서(Cursor)는 쿼리 결과의 각 행에 순차적으로 접근할 수 있게 해주는 데이터베이스 객체입니다. 커서를 사용하면 쿼리로 반환된 데이터 세트를 한 번에 한 행씩 처리할 수 있습니다. 이는 대량의 데이터를 처리하거나 복잡한 로직을 구현할 때 유용합니다.

커서의 기본 작동 원리
1. 선언(Declare): 커서를 정의하고 SQL 쿼리를 연결합니다.
2. 열기(Open): 커서를 열어 쿼리를 실행하고 결과 집합을 준비합니다.
3. 패치(Fetch): 커서를 사용하여 결과 집합의 다음 행을 가져옵니다.
4. 닫기(Close): 커서를 닫고 관련된 리소스를 해제합니다.

커서 사용시 고려사항
- 성능: 커서는 일반적으로 성능이 떨어질 수 있으므로, 가능한 경우 세트 기반의 접근 방식을 우선 고려해야 합니다.
- 리소스 사용: 커서는 메모리와 CPU 리소스를 상당량 사용할 수 있습니다.
- 복잡성: 커서는 로직이 복잡하거나, 행 단위의 처리가 필요한 경우에만 사용하는 것이 좋습니다.

커서의 유형
- 정적(Static) 커서: 쿼리 실행 시점의 데이터 스냅샷을 기반으로 합니다. 데이터 변경이 반영되지 않습니다.
- 동적(Dynamic) 커서: 데이터 변경이 실시간으로 반영됩니다. 다른 사용자의 데이터 변경도 볼 수 있습니다.
- 키셋(Keyset) 커서: 정적 커서와 유사하지만, 일부 변경(삭제나 삽입)을 반영할 수 있습니다.
- 읽기 전용(Read-only) 커서: 데이터를 변경할 수 없는 커서입니다.



```sql
CREATE PROCEDURE `ptable07` () -- empno, ename, sal 를 추출해서 봉급 등급도 구현하자
BEGIN
    DECLARE finished INT DEFAULT FALSE;  -- 제어 변수
    -- 리턴받을 변수 선언
    DECLARE v_empno INT;
    DECLARE v_ename VARCHAR(100);
    DECLARE v_sal   DECIMAL(10,2);
    DECLARE v_grade VARCHAR(100);
  
    -- ptable 테이블에서 추출할 쿼리를 담을 커서 생성
    DECLARE emp_cursor CURSOR FOR SELECT empno, ename, sal FROM ptable;

    -- 커서가 더이상 가져올 데이터가 없을 때 즉, 행이 없을 경우 발생하는 NOT FOUND 상황을 알리는 값을 받을 변수 선언
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET finished = TRUE;  -- 만약에 데이터 없으면 finished에 True 넣어줘

    -- 1. 커서 열기
	OPEN emp_cursor;

    -- 2. Fetch를 사용해서 테이블의 모든 행을 탐색
	read_loop: LOOP
		FETCH emp_cursor INTO v_empno, v_ename, v_sal;
        IF finished THEN
			LEAVE read_loop;
        END IF;
    
		SET v_grade = CASE				
						  WHEN v_sal < 2000 THEN 'Low'
						  WHEN v_sal BETWEEN 2000 AND 4000 THEN 'Medium'
						  ELSE 'High'
                      END;
		-- 각 행의 추출한 데이터와 급여 등급을 출력하자. 커서가 작동하는지 확인용
        SELECT v_empno, v_ename, v_sal, v_grade;
	END LOOP;

    -- 3. 커서 닫기
	CLOSE emp_cursor;
END


```

