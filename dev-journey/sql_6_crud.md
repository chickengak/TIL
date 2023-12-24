# 예제를 통한 실전 구문

```sql
-- 복제
CREATE TABLE my_emp
AS SELECT * FROM emp;

CREATE TABLE my_dept
AS SELECT * FROM dept;
```

<br>

### UPDATE
```sql
UPDATE my_emp
SET sal = 4000
WHERE empno = 7499;
```

### autocommit
autocommit이 켜져 있으면 다음의 TRANSACTION, COMMIT, ROLLBACK을 할 수 없다.
```sql
SET GLOBAL autocommit = 1;
SET autocommit = 0;
SELECT @@global.autocommit;
SELECT @@autocommit;
```

### TRANSACTION　COMMIT　ROLLBACK
```sql
START TRANSACTION;

UPDATE my_emp
SET sal = 9999
WHERE empno = 7499;

ROLLBACK;


START TRANSACTION;

UPDATE my_emp
SET sal = 3000
WHERE empno = 7499;

COMMIT;
ROLLBACK;
```

### UPDATE　INSERT　DELETE
```sql
UPDATE my_emp
SET sal = 1800, deptno = 10
WHERE job = 'SALESMAN';

INSERT INTO my_dept VALUES(50, 'RESEARCH', 'BOSTON');

DELETE FROM my_dept WHERE deptno = 50;
```
<br>

## Advanced
**Q 1.** 사원번호 7499의 부서를 사원번호 7698의 부서로 바꾸자.
```sql
UPDATE my_emp
SET deptno = (
    SELECT deptno
    FROM emp
    WHERE empno = 7698
)
WHERE empno = 7499;
```
뭔가 이상함을 느꼈을거다. 서브쿼리안에서 emp 테이블을 참조하고 있다. 왜 my_emp를 참조하지 않고 원본테이블을 참조할까? CRUD할 때, 자기 자신 테이블을 참조하면 Error Code: 1093(직접 참조할 때 발생하는 오류) 에러가 발생한다. 즉, 하나의 테이블에서 동시에 읽고 쓸 경우 무결성을 위배하기 때문에 발생하는 에러라고 보면 된다.  
https://dev.mysql.com/doc/refman/8.0/en/update.html  
이를 해결해보자.
```sql
-- 인라인 뷰로 해결
UPDATE my_emp
SET deptno = (
    SELECT temp.deptno
    FROM (
        SELECT deptno
        FROM my_emp
        WHERE empno = 7698
    ) temp
)
WHERE empno = 7499;
```
```sql
-- 변수로 해결
SET @deptno_7698 = (
    SELECT deptno
    FROM my_emp
    WHERE empno = 7698
);

UPDATE my_emp
SET deptno = @deptno_7698
WHERE empno = 7499;

SET @deptno_7698 = null;
```
SQL의 변수는 세션 동안 유효합니다. 즉, 데이터베이스 연결이 끊어지기 전까지 해당 변수는 존재하게 됩니다. 그러나, 명시적으로 변수를 '제거'하고 싶다면, 일반적으로는 변수를 NULL 또는 빈 값으로 설정하는 방법을 사용합니다.  
여기서 '세션'이란 사용자가 데이터베이스에 연결되어 있는 기간을 의미합니다. 

> 세션의 생명주기
> 1. 세션 시작: 사용자가 데이터베이스에 로그인하거나 연결을 시작할 때, 새로운 세션이 시작됩니다. 이때, 사용자별로 고유한 세션이 생성되며, 이 세션은 사용자의 데이터베이스 작업과 상태를 유지합니다.
> 2. 세션 동안의 작업: 세션 동안 사용자는 데이터를 조회하거나 조작할 수 있고, 세션 변수를 설정하여 사용할 수 있습니다. 이 변수들은 세션 동안에만 유효하며, 세션 내에서만 접근 가능합니다.
> 3. 세션 종료: 사용자가 로그아웃하거나 데이터베이스 연결이 끊어지면 세션이 종료됩니다. 세션 종료 시, 해당 세션에 설정된 모든 변수와 임시 데이터는 자동으로 사라집니다.

> 데이터베이스의 세션 관리
> 1. 자원 할당과 관리: 각 세션은 독립적인 메모리 공간과 실행 컨텍스트를 할당받습니다. 데이터베이스 시스템은 이러한 세션들을 관리하여, 각 사용자가 동시에 데이터베이스에 접근할 때 발생할 수 있는 충돌을 방지합니다.
> 2. 변수와 상태의 유지: 세션 내에서 설정된 변수들과 사용자의 작업 상태는 그 세션 내에서만 유지됩니다. 이는 데이터의 일관성과 보안을 유지하는 데 중요한 역할을 합니다.
> 3. 효율적인 연결 관리: 데이터베이스는 세션을 통해 다수의 사용자 연결을 효율적으로 관리합니다. 이는 서버 자원을 최적화하고, 시스템의 부하를 분산하는 데 도움이 됩니다.

**세션 관리는 데이터베이스의 성능, 보안, 그리고 데이터 일관성을 유지하는 데 필수적인 요소입니다. 이를 통해 각 사용자는 안정적이고 독립적인 환경에서 데이터베이스 작업을 수행할 수 있습니다.**

<br>

**Q 2.** 다음을 입력하고, 홍길동의 직업을 SALESMAN으로 부서를 20번으로 바꿔라
```sql
INSERT INTO my_emp VALUES(1234, '홍길동', 'CLERK', 7783, NOW(), 500, NULL, 10);
INSERT INTO my_emp VALUES(2345, '김길동', 'CLERK', 7784, NOW(), 510, NULL, 10);
INSERT INTO my_emp VALUES(3456, '홍길동', 'CLERK', 7785, NOW(), 520, NULL, 10);

UPDATE my_emp
SET job = 'SALESMAN', deptno = 20
WHERE ename = '홍길동';                 -- 여러개면 같이 바뀐다!
```

<br>

**Q 2-1.** 사원번호가 2345이고 매니저가 7784인 사원을 삭제하자.
```sql
DELETE FROM my_emp
WHERE empno = 2345 AND mgr = 7784;
```

**Q 2-1.** 홍길동의  봉급을 KING과 같이 바꾸자.
```sql

```

**Q 2-2.**  홍길동의 매니저가 7785인 사원의 봉급을  0으로 바꾸자.  
