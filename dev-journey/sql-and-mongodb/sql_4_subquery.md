# 예제를 통한 실전 구문

## Subqueries
https://dev.mysql.com/doc/refman/8.0/en/subqueries.html  

서브쿼리는 메인 쿼리의 일부분으로, 데이터를 필터링하거나, 데이터를 계산하거나, 메인 쿼리에 필요한 데이터를 제공하는 데 사용됩니다.

### 서브쿼리의 특징
1) 서브쿼리는 내부 쿼리(Subqueies)와 외부 쿼리(Main query)로 구성된다.
2) 서브쿼리는 SELECT INSERT UPDATE DELETE 문에서 WHERE, HAVING, FROM, SELECT절 등 위치에 사용
3) 단일 행 또는 다중 행 결과를 반환할 수 있고, 사용되는 연산자가 달라진다
4) 일반적으로 서브쿼리는 주쿼리의 실행에 의존적이며, 외부쿼리의 컬럼을 참조할 수 있다.
5) EXISTS와 NOT EXISTS를 이용해 특정 조건이 충족되는지 여부만을 판단하는 논리적 테스트를 수행한다
6) Correlated subqueries: 서브쿼리가 외부 쿼리의 컬럼을 참조하는 경우를 말하며 서브쿼리는 외부쿼리의 각 행에 대해 반복적으로 실행된다.
7) 서브쿼리 내에서 LIMIT 절의 사용이 제한될 수 있다.

### 서브쿼리의 종류
1. 단일 행 서브쿼리: 하나의 행만 반환합니다. =, >, <, != 등과 같은 비교 연산자와 함께 사용됩니다.
2. 다중 행 서브쿼리: 여러 행을 반환합니다. IN, ANY, ALL, EXISTS 등과 같은 연산자와 함께 사용됩니다.
3. 상관 서브쿼리(Correlated Subquery): 메인 쿼리의 테이블과 상관관계를 가지는 서브쿼리입니다. 서브쿼리가 메인 쿼리의 행을 참조합니다.

### ANY　ALL
 = ANY 	 하나라도 만족하는 값이 있으면 결과를 리턴하며 IN과 동일함  
 \> ANY 	 값들 중 최소값 보다 크면 결과를 리턴  
 \>= ANY 	 값들 중 최소값 보다 크거나 같으면 결과를 리턴  
 < ANY 	 값들 중 최대값 보다 작으면 결과를 리턴  
 <= ANY 	 값들 중 최대값 보다 작거나 같으면 결과를 리턴  
 <> ANY 	 모든 값들 중 다른 값만 리턴 ,값이 하나일 때만 가능함  

 \> ALL 	 값들 중 최대값 보다 크면 결과를 리턴  
 \>= ALL 	 값들 중 최대값 보다 크거나 같으면 결과를 리턴  
 < ALL 	 값들 중 최소값 보다 작으면 결과를 리턴  
 <= ALL 	 값들 중 최소값 보다 작거나 같으면 결과를 리턴  
 = ALL 	 모든 값들과 같아야 결과를 리턴, 값이 하나일 때만 가능함  
 <> ALL 	 모든 값들과 다르면 결과를 리턴  

 ### =　IN
결과가 하나라는 것을 알고 있고, 추후에 변할 일이 없다면, = 대신 IN을 쓸 이유가 없다. IN의 cost가 더 높기 때문.
```sql
EXPLAIN FORMAT=TREE 
SELECT ename, sal 
FROM emp 
WHERE deptno IN (		
	SELECT deptno 
    FROM dept 
    WHERE loc = 'CHICAGO' 
);                          -- cost 1.6156

EXPLAIN FORMAT=TREE 
SELECT ename, sal 
FROM emp 
WHERE deptno = (		
	SELECT deptno 
    FROM dept 
    WHERE loc = 'CHICAGO' 
);                          -- cost 1.748

EXPLAIN FORMAT=TREE 
SELECT ename, sal 
FROM emp 
LEFT JOIN dept USING(deptno)
WHERE loc = 'CHICAGO';      -- cost 1.6156  대 조 인
```

<br>

### Exam
```sql
-- Q1. JONES의 월급보다 더 많이 받는 사원의 이름과 봉급을 출력하자
SELECT ename, sal
FROM emp
WHERE sal (
    SELECT sal
    FROM emp
    WHERE ename = 'JONES'
);

-- Q2. 직업이 'SALESMAN'인 사원과 같은 월급을 받는 사원의 이름과 월급을 출력
SELECT ename, sal
FROM emp
WHERE sal IN (
    SELECT sal
    FROM emp
    WHERE job = 'SALESMAN'
);

-- Q3. 부서번호가 10번인 사원들과 같은 월급을 받는 사원의 이름과 월급을 출력
SELECT ename, sal
FROM emp
WHERE sal IN (
    SELECT sal
    FROM emp
    WHERE deptno = 10
);

-- Q4. 직업이 CLERK인 사원과 같은 부서에서 근무하는 사원의 이름, 월급, 부서번호를 출력
SELECT ename, sal, deptno
FROM emp
WHERE deptno IN (
    SELECT deptno
    FROM emp
    WHERE job = 'CLERK'
);

-- Q5. 부하직원이 있는 사원의 사원번호와 이름을 출력하자.      ★
SELECT empno, ename
FROM emp
WHERE empno IN (
    SELECT DISTINCT mgr
    FROM emp
);                                      -- cost 10.349

SELECT DISTINCT m.empno, m.ename 
FROM emp e
JOIN emp m ON (e.mgr = m.empno);        -- cost 6.549


-- Q6. 부하직원이 없는 사원의 사원 번호와 이름을 출력하자.      ★
SELECT empno, ename
FROM emp
WHERE empno NOT IN (                -- 아무것도 출력 안됨
    SELECT DISTINCT mgr
    FROM emp
);
-- SQL의 NOT IN 절은 NULL 값을 포함하는 서브쿼리와 함께 사용될 때 예상치 못한 동작을 할 수 있다. SQL에서 NULL은 "알 수 없는 값(unknown)"을 의미하며, NULL과의 비교는 항상 NULL(즉, 알 수 없음)을 반환하기 때문.
-- IN 절에서는 서브쿼리의 결과 중 하나라도 메인 쿼리의 열 값과 일치하면 해당 행이 결과로 선택된다. 그래서 NULL 값이 서브쿼리 결과에 포함되어 있다고 해도, 다른 일치하는 값이 존재하면 그 행은 여전히 결과에 포함된다.

SELECT empno, ename
FROM emp
WHERE empno NOT IN(
	SELECT IFNULL(mgr, 0)
	FROM emp
);

SELECT empno, ename
FROM emp
WHERE empno !=ALL(
	SELECT IFNULL(mgr, 0)
	FROM emp
);

-- Q7. KING 에게 보고하는 사원의 이름과 월급을 구하자.
SELECT ename, sal
FROM emp
WHERE mgr = (
    SELECT empno
    FROM emp
    WHERE ename = 'KING'
);

-- Q8. 20번 부서의 사원 중 가장 많은 월급을 받는 사원들 보다 더 많은 월급을 받는 사원들의 이름과 월급을 출력. (집계연산자, any, all 선택사용)
SELECT ename, sal
FROM emp
WHERE sal > (
    SELECT MAX(sal)
    FROM emp
    WHERE deptno = 20
);

SELECT ename, sal
FROM emp
WHERE sal > ALL(
    SELECT sal
    FROM emp
    WHERE deptno = 20
);

-- Q9. 20번 부서의 사원 중 가장 적은 월급을 받는 사원들보다 더 많은 월급을 받는 사원의 이름과 월급을 출력해보자 (집계연산자, any, all 선택사용)
SELECT ename, sal
FROM emp
WHERE sal > ANY(
    SELECT sal
    FROM emp
    WHERE deptno = 20
);

-- Q10. 직업이 'SALESMAN'인 사원 중 가장 적은 월급을 받는 사원보다 더 적은 월급을 받는 사원들의 이름과 월급을 출력. (min, max 금지)
SELECT ename, sal
FROM emp
WHERE sal < ALL(
    SELECT sal
    FROM emp
    WHERE job = 'SALESMAN'
);
```

```sql
-- Q11. salesman인 사원과 같은 부서에서 근무하고 같은 월급을 받는 사원들의 이름, 월급, 부서번호를 출력
SELECT ename, sal, deptno
FROM emp
WHERE deptno IN(
    SELECT deptno
    FROM emp
    WHERE job = 'SALESMAN'
) AND sal IN (
    SELECT sal
    FROM emp
    WHERE job = 'SALESMAN'
);

-- Q12. 30번부서 사원들과 같은 월급과 커미션을 받는 사원들의 이름, 월급, 커미션을 출력
SELECT ename, sal, comm
FROM emp
WHERE sal = ANY(
    SELECT sal
    FROM emp
    WHERE deptno = 30
) AND comm = ANY(
    SELECT comm
    FROM emp
    WHERE deptno = 30
);


-- Q13. 각 사원의 봉급이 사원이 속한 부서의 평균 급여보다 얼마나 높은지 출력해보자.
SELECT ename, sal, sal - avgsal                     
FROM emp e
JOIN (
    SELECT deptno, AVG(sal) AS avgsal
    FROM emp
    GROUP BY deptno                         -- cost 13.098
) a ON(e.deptno = a.deptno);            -- using은 안되고 on만 됨.

SELECT ename, sal, sal - (
    SELECT AVG(sal)
    FROM emp
    WHERE deptno = e.deptno
)
FROM emp e;                           -- cost 15.168 SELECT절 서브 쿼리 ★

-- Q14. EXISTS를 사용해서 부서에 사원이 존재하는 지 확인해보자.
SELECT deptno, dname
FROM dept d
WHERE  EXISTS(
    SELECT 1
    FROM emp
    WHERE deptno = d.deptno
);


-- Q15. 각 부서에서 가장 높은 급여를 받는 사원의 모든 내용을 출력하자
SELECT *
FROM emp e
WHERE empno IN (
    SELECT empno
    FROM emp, (
        SELECT deptno, MAX(sal) AS maxsal
        FROM emp
        GROUP BY deptno
    ) m
    WHERE e.deptno = m.deptno AND sal = m.maxsal
);                                          -- cost 17.998

SELECT *
FROM emp e, (
        SELECT deptno, MAX(sal) AS maxsal
        FROM emp
        GROUP BY deptno
    ) m
WHERE e.deptno = m.deptno AND sal = m.maxsal; -- cost 13.098 응 내가 코스트 더 줄임

SELECT *
FROM emp e
LEFT JOIN (
        SELECT deptno, MAX(sal) AS maxsal
        FROM emp
        GROUP BY deptno
) m USING(deptno)
WHERE sal = m.maxsal;                      -- cost 13.098 조인써봤는데 똑같네

SELECT *
FROM emp e
WHERE sal = (
	SELECT MAX(sal)
    FROM emp m
    WHERE e.deptno = m.deptno
);                                  -- cost 15.168 Correlated subqueries ★


-- Q16. 각부서에서 봉급이 가장 높은 상위 3명의 사원번호, 이름, 봉급, 부서번호를 출력
SELECT e1.empno, e1.ename, e1.sal, e1.deptno
FROM emp e1
WHERE (
    SELECT count(*)
    FROM emp e2
    WHERE e2.sal > e1.sal AND e2.deptno = e1.deptno
) < 3
ORDER BY e1.deptno, e1.sal DESC;                    -- cost 29.168    ★
/*
풀이: 먼저 각 부서별로 급여가 높은 순으로 정렬된 사원의 목록을 만든다 > 상위 3명 추출
1. 주 쿼리는 emp 테이블의 모든 내용을 스캔한다.
2. 서브쿼리는 같은 부서내에서 각 사원의 급여보다(e.sal) 더 높은 급여를 받는 사원 수를 계산
3. 계산결과 3명 이내인 경우 해당 사원의 결과를 리턴
4. 결과는 각 부서내에서 급여가 높은 순으로 정렬.
*/

-- Q17. 각 부서에 최근 입사한 사원 2명씩의 사원번호, 이름, 입사일, 부서번호를 출력하자.
SELECT empno, ename, hiredate, deptno
FROM emp e1
WHERE (
    SELECT COUNT(*)
    FROM emp e2
    WHERE e1.deptno = e2.deptno AND e2.hiredate > e1.hiredate
) < 2
ORDER BY deptno, hiredate DESC;                   -- cost 29.168    ★


-- Q18. 평균 급여가 전체 평균보다 더 높은 부서를 찾아보자.
SELECT deptno, AVG(sal) AS avgsal
FROM emp
WHERE avgsal > (
    SELECT AVG(sal)
    FROM emp
)
GROUP BY deptno;                        -- 안됨. group by의 조건은 having

SELECT deptno, AVG(sal)
FROM emp
GROUP BY deptno
HAVING AVG(sal) > (
    SELECT AVG(sal)
    FROM emp
);

-- Q19. 부서별로 사원수가 전체 사원수의 평균보다 많은 부서를 찾아 부서번호, 직원수를 출력하자.
SELECT deptno, COUNT(empno)
FROM emp
GROUP BY deptno
HAVING COUNT(empno) > (
    SELECT AVG(temp.cnt)
    FROM (
        SELECT COUNT(empno) AS cnt
    FROM emp
    GROUP BY deptno
    ) temp
);

```


### 서브쿼리로 테이블 만들기
```sql
CREATE TABLE test
AS 
SELECT * FROM emp;

CREATE TABLE test02
AS
SELECT empno, ename, sal FROM emp;

CREATE TABLE test03 (ename VARCHAR(50))
AS
SELECT ename, empno, sal FROM emp;

CREATE TABLE test04 (myname VARCHAR(50))
AS
SELECT empno, ename AS myname, sal FROM emp;        -- 컬럼명, 타입 다 바꿀 수 있다

-- CHICAGO에서 근무하는 사원들과 부서에서 근무하는 사원의 이름과 월급으로 새 테이블을 만들어보자.

CREATE TABLE test05 (emp_name VARCHAR(50), sal DECIMAL(10,2))
AS
SELECT empno, ename AS emp_name, sal
FROM emp
WHERE deptno IN (
    SELECT deptno
    FROM dept
    WHERE loc = 'CHICAGO'
);

```

