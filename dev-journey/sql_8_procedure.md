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
CREATE PROCEDURE `ptable01` (input_empno INT, input_ename VARCHAR(20))
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
CREATE PROCEDURE `ptable02` (input_empno INT)
BEGIN
	DELETE FROM ptable WHERE empno = input_empno;
END

CALL ptable02(1234);
```

### Procedure로 데이터 수정
```sql
CREATE PROCEDURE `ptable03` (input_empno INT, input_sal DECIMAL(7,2))
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
CREATE PROCEDURE `ptable04` (input_ename VARCHAR(20))
BEGIN
    SELECT *
    FROM ptable
    WHERE ename = input_ename;
END

CALL ptable04('FORD');
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

###
https://dev.mysql.com/doc/refman/8.0/en/cursors.html  
