# 예제를 통한 실전 구문

## Table CRUD

### DB 만들기
```sql
CREATE DATABASE students;

USE students;
```

### 테이블 만들기, 드랍하기, 정보보기
```sql
DROP TABLE students;

CREATE TABLE students(
    student_id      INT,
    student_number  VARCHAR(10) NOT NULL,       # 여기 붙는 NOT NULL 같은 걸
    first_name      VARCHAR(50) NOT NULL,       # "열 제약 조건" (Column Constraints)
    last_name       VARCHAR(50) NOT NULL,       # "열 옵션" (Column Options) 이라고 한다
    birthday        DATE,
    gender          ENUM('M', 'F'),
    paid_flag       BOOL,

    PRIMARY KEY (student_id)    # PK를 줬기 때문에 자동으로 NOT NULL 및 중복 불가가 적용됨
);

DESC students;
```
```sql
INSERT INTO students VALUES(1, 123, 'FN', 'LN', NOW(), 'M', True);
INSERT INTO students VALUES(2, 123, 'FN', 'LN', NOW(), 'f', 0);
    # 성별 enum 대소문자 상관없음. BOOL에 True, False 대신 1, 0도 가능.
INSERT INTO students VALUES(3, 123, 'FN', 'LN', NOW(), NULL, True);
    # 성별 enum NOT NULL이 아니라서 NULL 들어감. 
INSERT INTO students VALUES(3, 123, 'FN', 'LN', NOW(), 'A', True);
    # 당연히 PK 중복은 불가능. 심지어 enum에 A가 들어감.

SELECT * FROM students;     # 현재 MySQL에서는 PK순으로 정렬되어 나오지만 모든 디비가 그렇지는 않다고 함. 오히려 기본은 입력된 데이터 순으로 출력이라고 함.
```

### 복합키
Primary Key는 테이블의 각 행을 고유하게 식별하는 데 사용되기 때문에, 한 테이블에는 오직 하나의 Primary Key만 설정할 수 있다.  
그러나, 다중 열(composite key)의 조합으로 고유성을 판단할 수 있는 경우 여러 열에 PK를 줄 수 있고 이게 복합키다. 테이블을 살펴보다가 PK가 두 개 이상이라면 복합키인 것이다.

```sql
CREATE TABLE students03(
	student_id 		INT ,
    student_number 	VARCHAR(10),

    PRIMARY KEY (student_id, student_number)			
);
```
```sql
INSERT INTO students03 VALUES(1, 1);
INSERT INTO students03 VALUES(1, 2);
INSERT INTO students03 VALUES(2, 2);
INSERT INTO students03 VALUES(2, 2);        # 복합키가 중복되니까 에러.
INSERT INTO students03 VALUES(NULL, 3);     # student_id가 PK의 일종인 복합키니까 null 불가.
INSERT INTO students03 VALUES(3, NULL);     # 마찬가지
```

### AUTO_INCREMENT
```sql
CREATE TABLE students04(
    student_id      INT AUTO_INCREMENT,
    student_number  VARCHAR(10) NOT NULL,

    PRIMARY KEY (student_id)
);
```
```sql
INSERT INTO students04 VALUES(1, 1);
INSERT INTO students04 VALUES(2, 2);
INSERT INTO students04(student_number) VALUES(10);   # 3, 10
INSERT INTO students04(student_number) VALUES(20);   # 4, 20
INSERT INTO students04 VALUES(5);       # Error
    # 앞에 AUTO_INCREMENT가 있고 뒤에 NOT NULL이 있으니까 값을 하나만 넣으면 유연하게 자동증가하면서 뒤에 값이 들어가지 않을까? 하고 생각할 수 있는데. 응 어림없죠?

INSERT INTO students04 VALUES(100, 50);
INSERT INTO students04(student_number) VALUES(60);   # 101, 60
    # 앞에서 student_id에 100을 주면서 건너 뛰었기 때문에 101로 AUTO_INCREMENT한다.

ALTER TABLE students04 AUTO_INCREMENT = 30;     # AUTO_INCREMENT 시작점을 지정
    # 근데 여기서 30으로 지정해도 30부터 AUTO_INCREMENT 하지 않는다. 왜냐하면 앞에서 101을 마지막으로 끝났기 때문에 102보다 큰 수를 주지 않는한, 102부터 시작한다.
```

### DEFAULT

