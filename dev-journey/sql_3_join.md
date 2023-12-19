# 예제를 통한 실전 구문
my_emp
| empno | ename  | job       | mgr  | hiredate   | sal     | comm    | deptno |
|-------|--------|-----------|------|------------|---------|---------|--------|
| 7369  | SMITH  | CLERK     | 7902 | 1980-12-17 | 800.00  |         | 20     |
| 7499  | ALLEN  | SALESMAN  | 7698 | 1981-02-20 | 1600.00 | 300.00  | 30     |
| 7521  | WARD   | SALESMAN  | 7698 | 1981-02-22 | 1250.00 | 500.00  | 30     |
| 7566  | JONES  | MANAGER   | 7839 | 1981-04-02 | 2975.00 |         | 20     |
| 7654  | MARTIN | SALESMAN  | 7698 | 1981-09-28 | 1250.00 | 1400.00 | 30     |
| 7698  | BLAKE  | MANAGER   | 7839 | 1981-05-01 | 2850.00 |         | 30     |
| 7782  | CLARK  | MANAGER   | 7839 | 1981-06-09 | 2450.00 |         | 10     |
| 7788  | SCOTT  | ANALYST   | 7566 | 1987-04-19 | 3000.00 |         | 20     |
| 7839  | KING   | PRESIDENT |      | 1981-11-17 | 5000.00 |         | 10     |
| 7844  | TURNER | SALESMAN  | 7698 | 1981-09-08 | 1500.00 | 0.00    | 30     |
| 7876  | ADAMS  | CLERK     | 7788 | 1987-05-23 | 1100.00 |         | 20     |
| 7900  | JAMES  | CLERK     | 7698 | 1981-12-03 | 950.00  |         | 30     |
| 7902  | FORD   | ANALYST   | 7566 | 1981-12-03 | 3000.00 |         | 20     |
| 7934  | MILLER | CLERK     | 7782 | 1982-01-23 | 1300.00 |         | 10     |
<br>

dept
| deptno | dname      | loc       |
|--------|------------|-----------|
| 10     | ACCOUNTING | NEW YORK  |
| 20     | RESEARCH   | DALLAS    |
| 30     | SALES      | CHICAGO   |
| 40     | OPERATIONS | BOSTON    |
<br>

salgrade
| grade | losal | hisal |
|-------|-------|-------|
| 1     | 700   | 1200  |
| 2     | 1201  | 1400  |
| 3     | 1401  | 2000  |
| 4     | 2001  | 3000  |
| 5     | 3001  | 9000  |
<br>

X
| productid | inventory |
|-----------|-----------|
| A         | 5         |
| E         | 7         |
<br>

Y
| productid | inventory |
|-----------|-----------|
| A         | 1         |
| B         | 2         |
| C         | 3         |
|           | 1         |
```
CREATE TABLE X(
	productid VARCHAR(5),
    inventory INT4
);

CREATE TABLE Y(
	productid VARCHAR(5),
    inventory INT4
);

INSERT INTO X SET productid = 'A', inventory = 5; 
INSERT INTO X SET productid = 'E', inventory = 7; 
INSERT INTO Y values('A', 1); 
INSERT INTO Y values('B', 2); 
INSERT INTO Y values('C', 3); 
INSERT INTO Y SET  inventory = 1; 

CREATE TABLE salgrade(
	grade INT,
    losal INT,
    hisal INT
);

INSERT INTO salgrade SET grade = 1, losal = 700, hisal = 1200;
INSERT INTO salgrade values(2, 1201, 1400);
INSERT INTO salgrade values(3, 1401, 2000);
INSERT INTO salgrade values(4, 2001, 3000);
INSERT INTO salgrade values(5, 3001, 9000);
```
<br>

## JOIN
### INNER JOIN 
```
SELECT * FROM x
INNER JOIN y ON x.productid = y.productid;      # A 5 A 1


SELECT *
FROM emp
JOIN dept USING(deptno);     # USING을 쓰면 deptno가 앞으로 가고 deptno 컬럼은 하나만 출력

SELECT *
FROM emp e
INNER JOIN dept d ON e.deptno = d.deptno;       # ON을 쓰면 deptno가 두번 나온다.

SELECT *
FROM emp e, dept d
WHERE e.deptno = d.deptno;                      # WHERE도 두번 나옴.
```

### OUTHER JOIN
```
SELECT *                                            # A    5    A    1
FROM x                                              # null null B    2
RIGHT OUTER JOIN y ON x.productid = y.productid;    # null null C    3
                                                    # null null null 1
                                                    # null null null 1
SELECT *                                        
FROM x                                              # A    5    A    1
LEFT OUTER JOIN y ON x.productid = y.productid;     # E    7    null null
```

### UNION
UNION (중복항목 x 자동으로 제거함)  
UNION ALL (중복항목 O 중복도 출력한다)

### FULL OUTHER JOIN
right outer join + left outer join느낌. 해당 명령은 없어진 곳이 많으니 UNION 해야함.  
union은 전체 테이블을 탐색하기 때문에 비용이 많이 든다. 혹시라도 full outer join을 지원하면 그걸 쓰자.
```
SELECT *
FROM x                                              # A    5    A    1
RIGHT JOIN y ON x.productid = y.productid           # null null B    2
UNION                                               # null null C    3
SELECT *                                            # null null null 1
FROM x                                              # E    7    null null
LEFT JOIN y ON x.productid = y.productid;
```

### SELF JOIN
한 테이블의 같은 값을 가진 컬럼을 조인하는 것. 테이블에 별칭을 줘야한다.
```
SELECT e.empno, e.ename, e.mgr, m.ename     # 사원의 매니저번호 mgr을 이용해서
FROM emp e                                  # 매니저 이름까지 출력하기
JOIN emp m ON e.mgr = m.empno;              # 허나 KING의 mgr은 null이라서 문제발생

SELECT e.empno, e.ename, e.mgr, m.ename
FROM emp e
LEFT JOIN emp m ON e.mgr = m.empno;
```

### NATURAL JOIN
두 테이블에서 동일한 이름을 가진 열을 기준으로 자동 조인한다.  
모든 데이터에 대해 알아야 오류가 없다고 보장할 수 있기 때문에 권장되지 않는 조인.
```

```

### CROSS JOIN
```

```

