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

## Advanced

### OVER()
OVER는 행의 집합을 리턴.  
OVER()는 윈도우 함수(창 함수)의 일부로 사용되며, 특히 데이터의 창(윈도우)을 정의하고 그 창 내에서 계산을 수행하는 데 사용됩니다.   

<집계 함수>(<열 또는 표현식>) OVER (  
　　　PARTITION BY <파티션 열>   
　　　ORDER BY <정렬 열>  
　　　ROWS <범위 또는 행> BETWEEN <시작 행> AND <끝 행>  
)  
+$a$) ROWS BETWEEN 1 PRECEDING AND 1 FOLLOWING은 현재 행의 이전 행과 다음 행을 포함한 3개의 연속된 행을 창으로 정의
```MySQL
SELECT SUM(sal)
FROM emp;

SELECT SUM(sal) OVER()
FROM emp;

SELECT SUM(sal) OVER(ORDER BY sal), sal
FROM emp;

SELECT SUM(sal) OVER (ORDER BY sal ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
       AS cumulative_sum, sal
FROM emp;
```

### ROW_NUMBER()
SELECT ROW_NUMBER() [OVER  PARTITION BY, ORDER BY ]	
```MySQL
SELECT ROW_NUMBER() OVER(ORDER BY ename) AS 'No.', ename    # 인덱싱용 라벨링 가능
FROM emp;

SELECT ROW_NUMBER() OVER(ORDER BY ename DESC) AS 'No.', ename   # 역순 라벨링
FROM emp
ORDER BY 1 DESC;

SELECT -1+2*ROW_NUMBER() OVER(ORDER BY ename) AS 'No.', ename   # 홀수로 라벨링
FROM emp;

SELECT ROW_NUMBER() OVER(PARTITION BY job ORDER BY ename), job, ename
FROM emp;                                   # 직업별로 그룹화한 후 번호를 매겨 출력
```

### RANK()　DENSE_RANK()　PERCENT_RANK()
SELECT RANK() OVER  (PARTITION BY,   ORDER BY)  
RANK는 중복을 고려하고, DENSE_RANK는 중복을 고려하지 않음. PERCENT_RANK는 0부터 1까지의 범위로 상대적 위치를 계산함. 전부 오름차순으로 랭킹을 매긴다.
```MySQL
SELECT RANK() OVER(ORDER BY sal DESC) AS 'rank',
        DENSE_RANK() OVER(ORDER BY sal DESC) AS 'dense rank',
        PERCENT_RANK() OVER(ORDER BY sal DESC) AS 'percent rank', sal, ename
FROM emp;                       # 월급순으로 랭킹 매기기

SELECT RANK() OVER(PARTITION BY deptno ORDER BY sal DESC) AS 'rank',
        DENSE_RANK() OVER(PARTITION BY deptno ORDER BY sal DESC) AS 'dense rank',
        PERCENT_RANK() OVER(PARTITION BY deptno ORDER BY sal DESC) AS 'percent rank', sal, deptno, ename
FROM emp;                       # 부서내에서 월급순으로 랭킹 매기기
```


날짜 string 그룹컨캣 regexp 비트연산 



