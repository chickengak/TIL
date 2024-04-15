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

**Q 2-2.** 홍길동의 봉급을 KING과 같이 바꾸자.
```sql
UPDATE my_emp
SET sal =(
    SELECT temp.sal
    FROM (
        SELECT sal
        FROM my_emp
        WHERE ename = 'KING'
    ) temp
)
WHERE ename = '홍길동';
```

<br>

**Q 3.**  WARD 와 같은 직업을 가진 삭제.
```sql
DELETE FROM my_emp
WHERE job = (
    SELECT temp.job
    FROM (
        SELECT job
        FROM my_emp
        WHERE ename = 'WARD'
    ) temp
);
```

**Q 4-1.**  WARD의 월급을 SMITH의 월급과 같게 수정하자
```sql
```

**Q 4-2.**  'KING'의 직업을 'SMITH'와 같게 바꿔라
```sql
```

**Q 4-3.**  사원번호가 7499번인 사원과 같은 직업을 가진 사원들의 입사일을 오늘 날짜로 변경.
```sql
UPDATE my_emp
SET hiredate = CURDATE()
WHERE job = (
    SELECT temp.job
    FROM (
        SELECT job
        FROM my_emp
        WHERE empno = 7499
    ) temp
);
```


**Q 5-1.** 제약조건 추가해보기
```sql
ALTER TABLE my_emp ADD CONSTRAINT PRIMARY KEY (empno);
ALTER TABLE my_dept ADD CONSTRAINT PRIMARY KEY (deptno);

ALTER TABLE my_emp ADD CONSTRAINT myfk_emp_dpet FOREIGN KEY (deptno) REFERENCES my_dept(deptno) ON DELETE CASCADE ON UPDATE CASCADE;
-- 제약조건 이름은 다른 테이블이더라도 디비기준으로 중복될 수 없다.
```

**Q 5-2.** FK 적용시키기
```sql
DELETE FROM my_dept
WHERE deptno = 10;

SELECT * FROM my_emp;
```
```sql
UPDATE my_emp
SET deptno = 200
WHERE deptno = 20;

SELECT * FROM my_emp;
```
```sql
INSERT INTO my_emp VALUES(1234, '홍길동', 'CLERK', 7783, NOW(), 500, NULL, NULL);

SELECT *
FROM my_emp
LEFT JOIN my_dept USING(deptno);
-- deptno는 dept에서나 PK지, emp에서는 not null도 아니고 PK도 아니니까 null을 넣을 수 있다. 대신 참조는 불가. 참조를 못해서 dname, loc 다 null로 나온다.
```

**Q 5-3.** ON DELETE　CASCADE / RESTRICT / NO ACTION  
SQL에서 FOREIGN KEY 제약조건에 사용되는 ON DELETE 옵션은 참조되는 테이블의 행이 삭제될 때, 참조하는 테이블의 해당 행을 어떻게 처리할지 정의합니다.
> 1. CASCADE: ON DELETE CASCADE 옵션은 참조되는 테이블의 행이 삭제될 때, 그것을 참조하는 모든 행도 함께 삭제합니다. 이 옵션은 관련된 데이터가 완전히 삭제되어야 할 때 유용합니다.
> 2. NO ACTION: 기본적으로, ON DELETE NO ACTION은 참조 무결성을 유지하기 위해 참조되는 행의 삭제를 막습니다. 만약 참조되는 테이블의 행이 삭제되려고 하면, SQL 시스템은 오류를 발생시켜 삭제 작업을 방지합니다.
> 3. RESTRICT: ON DELETE RESTRICT 옵션은 NO ACTION과 유사하게, 참조되는 행이 삭제되는 것을 방지합니다. 하지만, RESTRICT는 명시적으로 삭제를 막는 데 사용되며, 데이터베이스에 따라 NO ACTION과 동작이 다를 수 있습니다.      
-- NO ACTION(트랜잭션이 종료될 때 오류 발생함), RESTRICT(즉시 오류 발생함). 즉, 기능은 같으나 오류 발생시점이 다름.
> 4. SET NULL: ON DELETE SET NULL 옵션은 참조되는 테이블의 행이 삭제될 때, 참조하는 테이블의 외래 키 값을 NULL로 설정합니다. 이는 참조 무결성을 유지하면서도, 참조 관계를 끊을 수 있는 방법입니다.
> 5. SET DEFAULT: ON DELETE SET DEFAULT 옵션은 참조되는 테이블의 행이 삭제될 때, 참조하는 테이블의 외래 키 값을 해당 컬럼의 기본값으로 설정합니다.

