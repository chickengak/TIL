# 예제를 통한 실전 구문
```sql
DATABASE(=SCHEMA)
    TABLE
    VIEW
    PROCEDURE
    FUNCTION
```
## View
https://dev.mysql.com/doc/refman/8.0/en/sql-data-definition-statements.html  
https://dev.mysql.com/doc/refman/8.0/en/drop-view.html  

~~뷰는 클라이언트에게 원본 테이블, 엔티티를 공개하지 않고 필요로 하는 데이터만 추려서 클라이언트에게 제공하는거임. 그래서 일반적으로 뷰는 보는 옵션(Read)만 제공하는게 관례다.~~ 라고 했지만 이건 틀렸음

뷰(View)는 데이터베이스 내의 하나 이상의 테이블에서 파생된 **가상 테이블**입니다. **뷰는 실제 데이터를 저장하지 않고, 기본 테이블에서 데이터를 검색하는 SQL 쿼리에 대한 참조를 제공합니다.** 뷰는 데이터베이스의 복잡성을 감추고, 데이터 보안과 사용 편의성을 향상시키는 데 사용됩니다.

### 뷰의 기본 개념
- 가상 테이블: 뷰는 실제 데이터를 저장하지 않는 가상 테이블로, 기본 테이블의 데이터를 표시합니다.
- 쿼리 단순화: 복잡한 쿼리를 뷰로 정의하여 간소화하고 재사용할 수 있습니다.
- 보안 강화: 뷰를 사용하여 사용자에게 필요한 데이터만 제공함으로써 데이터베이스의 보안을 강화할 수 있습니다.

### 뷰의 장단점
- 장점: 복잡성 감소, 보안 향상, 데이터 독립성
- 단점: 성능 저하(복잡한 뷰는 쿼리 처리를 늦출 수 있다), 갱신 제한(일부 뷰는 갱신을 제한할 수도)

### 뷰의 갱신
- 뷰는 갱신 가능한 경우도 있고, 아닌 경우도 있습니다.
- 갱신 가능 여부는 뷰가 생성될 때의 쿼리와 관련된 기본 테이블, 그리고 데이터베이스 시스템에 따라 다릅니다.
```sql
/* 갱신가능한 뷰 */
CREATE VIEW SimpleEmployeeView AS
SELECT empno, ename FROM emp;
-- 이 뷰에 있는 모든 열은 기본 테이블에 직접 매핑됐기 때문에 사용자는 뷰를 통해 정보를 갱신할 수 있음.

/*갱신 불가능한 뷰*/
CREATE VIEW EmployeeStatisticsView AS
SELECT deptno, COUNT(*) AS NumEmployees, AVG(sal) AS AvgSalary
FROM emp
GROUP BY deptno;
-- 이러한 뷰는 집계 함수를 사용하고 있기 때문에 갱신이 불가능하다. 이 외에도 조인, 서브쿼리 등 복잡한 쿼리를 포함하는 뷰는 갱신이 불가능.
```

### 만약 읽기 전용 뷰를 만들고 싶다면
사용자 권한 관리를 이용한다. 특정 사용자에게는 뷰에 대한 'SELECT' 권한만 부여하고, 'INSERT', 'UPDATE', 'DELETE' 권한은 부여하지 않으면 해결 가능.
```sql
/*관련 예시*/
CREATE VIEW ReadOnlyEmpView AS
SELECT empno, ename, deptno
FROM emp;


-- 사용자 생성 (예시: 사용자 이름이 'clientUser')
CREATE USER 'clientUser'@'localhost' IDENTIFIED BY 'password';

-- ReadOnlyEmpView에 대한 SELECT 권한 부여
GRANT SELECT ON ReadOnlyEmpView TO 'clientUser'@'localhost';


-- clientUser로 로그인 후 실행
SELECT * FROM ReadOnlyEmployeeView;
INSERT INTO ReadOnlyEmployeeView VALUES (1111, 'New Employee', 123); -- Error
```
<br>

### CREATE VIEW
https://dev.mysql.com/doc/refman/8.0/en/create-view.html 
```sql
CREATE
    [OR REPLACE]
    [ALGORITHM = {UNDEFINED | MERGE | TEMPTABLE}]
    [DEFINER = user]
    [SQL SECURITY { DEFINER | INVOKER }]
    VIEW view_name [(column_list)]
    AS select_statement
    [WITH [CASCADED | LOCAL] CHECK OPTION]      -- CASCADED 옵션도 있다
```

<br>

```sql
CREATE VIEW v AS SELECT qty, price, qty*price AS value FROM t;
```
이런 뷰 매우 옳지 않다. 왜냐하면 VIEW에서 qty*price같이 계산을 할 경우, DB에서 qty나 price가 바뀔 때마다 VIEW단에서 계산을 해야하기 때문임. 이럴 때 VIEW를 1000명이 보고 있다면? qty\*price를 1000번이나 계산하는 비효율이 발생한다.

<br>

```sql
CREATE VIEW `my_test` AS
SELECT * FROM emp;

CREATE 
    ALGORITHM = UNDEFINED -- 최적화 알고리즘을 자동으로 사용하겠다.
        -- MERGE: 뷰에 정의된 쿼리가 기본 테이블의 쿼리와 결합되어 단일 쿼리처럼 처리됨. 집계연산x 패턴x 오직 간단히 Read만 할 때 적합.
        -- TEMPTABLE: 뷰 결과가 임시 테이블에 저장됨. 복잡한 뷰에 적합. GROUPY BY, DISTINCT ...
    DEFINER = `root`@`localhost`  -- 뷰를 생성한 USER. 생성+관리
    SQL SECURITY DEFINER   -- 뷰 사용할 때 권한
VIEW `my_test` AS
    SELECT 
        `emp`.`empno` AS `empno`,
        `emp`.`ename` AS `ename`,
        `emp`.`job` AS `job`,
        `emp`.`mgr` AS `mgr`,
        `emp`.`hiredate` AS `hiredate`,
        `emp`.`sal` AS `sal`,
        `emp`.`comm` AS `comm`,
        `emp`.`deptno` AS `deptno`
    FROM
        `emp`

SELECT * FROM my_emp.my_test;
DESC my_emp.my_test;    -- 키나 제약조건은 안 가져오는 것을 확인할 수 있다.
```

### ALTER VIEW
https://dev.mysql.com/doc/refman/8.0/en/alter-view.html 
```sql
ALTER
    [ALGORITHM = {UNDEFINED | MERGE | TEMPTABLE}]
    [DEFINER = user]
    [SQL SECURITY { DEFINER | INVOKER }]
    VIEW view_name [(column_list)]
    AS select_statement
    [WITH [CASCADED | LOCAL] CHECK OPTION]
```

<br>
<br>

## Exam

```sql
-- Q1. VIEW 생성 후 수정해보기

CREATE VIEW emp_view
AS
SELECT * FROM my_emp;

SELECT COUNT(*)
FROM emp_view;


-- Q1-1. 데이터를 삭제한 후 원본과 비교 하자.

DELETE FROM emp_VIEW
WHERE empno = 7499;                 -- 원본 삭제됨. (VIEW에 권한을 다 줘서)


-- Q1-2. 원본삭제 후 뷰 확인

DELETE FROM my_emp
WHERE empno = 7369;                 -- 같이 삭제됨.

-- Q1-3 조인 안 된 뷰에는 잘 들어간다.

INSERT INTO emp_view(empno, ename) VALUES(1111, 'ABC');
SELECT * FROM my_emp;                       -- 원본까지 추가됐다.


-- Q3. 조인된 VIEW를 만들고 데이터를 추가한 후 각 테이블의 업데이트를 확인하자. (모든 수정이 안 됨)
-- Q3-1. 조인된 VIEW 생성

CREATE VIEW join_emp
AS
SELECT deptno, dname, ename
FROM my_emp
JOIN my_dept USING(deptno);

-- Q3-2. 확인

SELECT * FROM join_emp;

-- Q3-3. 데이터 추가

INSERT INTO join_emp(deptno, dname, ename) VALUES(50, '서울', '홍길동');
-- Error Code: 1393. Can not modify more than one base table through a join view 'my_emp.join_emp'

-- Q3-4. 데이터 삭제
DELETE FROM join_emp
WHERE ename = 'KING';
-- Error Code: 1395. Can not delete from join view 'my_emp.join_emp'


-- Q3-5. VIEW의 제약 조건을 확인하자
SELECT *
FROM INFORMATION_SCHEMA.VIEWS
WHERE TABLE_SCHEMA = 'join_emp' AND TABLE_NAME = 'join_emp';
-- CHECK OPTION(VIEW를 통해 데이터를 수정, 삽입), YES(수정)
-- IS_UPDATABLE


아니 왜 가르치다가 런치냐

```