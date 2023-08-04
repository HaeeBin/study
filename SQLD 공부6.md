# SQLD 공부

## 2,과목 SQL 기본 및 활용 (SQL 기본)

#### 1. GROUP BY, HAVING 절

+ **집계 함수(Aggregate Function)**
  
  + 여러 행들의 그룹이 모여 그룹당 단 하나의 결과를 돌려주는 함수
  
  + SELECT, HAVING, ORDER BY절에 사용
  
  + DISTINCT : 같은 값을 하나의 데이터로 간주해 하나만 조회
  
  + ALL : Default 옵션이므로 생략 가능
    
    | 집계 함수                               | 설명                                       |
    | ----------------------------------- | ---------------------------------------- |
    | COUNT(*)                            | NULL값 포함한 행의 수 출력                        |
    | COUNT(컬럼 \| 표현식)                    | 컬럼이나 표현식의 값이 NULL값인 것을 제외한 행의 수 출력       |
    | SUM([DISTINCT \| ALL] 컬럼 \| 표현식)    | 컬럼이나 표현식의 NULL값을 제외한 합계 출력               |
    | AVG([DISTINCT \| ALL] 컬럼 \| 표현식)    | 컬럼이나 표현식의 NULL값 제외한 평균 출력                |
    | MAX([DISTINCT \| ALL] 컬럼 \| 표현식)    | 컬럼이나 표현식의 최대값 출력<br>(문자, 날짜, 데이터 타입도 가능) |
    | MIN([DISTINCT \| ALL] 컬럼 \| 표현식)    | 컬럼이나 표현식의 최소값 출력<br>(문자, 날짜, 데이터 타입도 가능) |
    | STDDEV([DISTINCT \| ALL] 컬럼 \| 표현식) | 컬럼이나 표현식의 표준편차 출력                        |
    | VARIAN([DISTINCT \| ALL] 컬럼 \| 표현식) | 컬럼이나 표현식의 분산 출력                          |
    | 기타 통계 함수                            | 벤더별로 다양한 통계식 제공                          |



+ **GROUP BY절, HAVING 절**
  
  + GROUP BY절은 FROM, WHERE절 뒤에 위치.
  
  + 데이터들을 작은 그룹으로 분류하여 소그룹에 대한 항목별로 통계 정보 얻을 때 사용.
    
    
  
  + HAVING 절은 GROUP BY절의 조건절.
  
  + WHERE절은 집계함수 사용 못하지만 HAVING절은 가능.
    
    
  
  + GROUP BY절을 통해 소그룹별 기준 정하고, SELECT절에 집계 함수 사용.
  
  + 집계 함수의 통계 정보는 NULL값 가진 행 제외하고 수행.
  
  + WHERE절은 전체 데이터를 그룹으로 나누기 전에 행들을 미리 제거.



+ **ORDER BY절**
  
  + 조회된 데이터들을 다양한 목적에 맞게 특정 칼럼을 기준으로 정렬하여 출력하는데 사용.
  
  + 날짜형 데이터는 오름차순 정렬 시 가장 과거부터 출력.
  
  + Oracle에서는 NULL을 가장 큰 값으로 간주. 오름차순 정렬 시 가장 마지막에 출력.
  
  + SQL Server에서는 NULL을 가장 작은 값으로 간주. 오름차순 정렬 시 가장 앞에 출력.
  
  + ASC : 오름차순 / DESC : 내림차순



+ SELECT 실행 순서
  
  |          | 작성 순서 | 실행 순서 | 설명                    |
  |:--------:|:-----:|:-----:| --------------------- |
  | SELECT   | 1     | 5     | 데이터 값을 출력, 계산         |
  | FROM     | 2     | 1     | 조회 대상 테이블 참조          |
  | WHERE    | 3     | 2     | 조회 대상 데이터가 아닌 것 제외    |
  | GROUP BY | 4     | 3     | 행들을 소그룹화              |
  | HAVING   | 5     | 4     | 소그룹화된 값의 조건에 맞는 것만 출력 |
  | ORDER BY | 6     | 6     | 데이터 정렬                |
  
  + 문장 실행 순서는 옵티마이저가 SQL문장의 SYNTAX, SEMANTIC 에러를 점검하는 순서.
  
  + FROM절에 정의되지 않은 테이블의 칼럼을 WHERE, GROUP BY, HAVING, SELECT, ORDER BY절에 사용하면 에러 발생.
  
  + ORDER BY절에는 SELECT 목록에 나타나지 않은 문자형 항목 포함될 수 있음.
  
  + SELECT DISTINCT를 지정하거나 SQL 문장에 GROUP BY절이 있거나 또는 SELECT문에 UNION 연산자가 있으면 열 정의가 SELECT 목록에 표시되어야 함.
  
  + EX1)
    
    ```sql
    SELECT JOB, SAL
    FROM EMP
    GROUP BY JOB
    HAVING COUNT(*) > 0
    ORDER BY SAL;
    ```
  
  + -> ERROR : GROUP BY절에 사용하지 않은 일반 컬럼을 SELECT에 사용할 수 없음.
    
    
  
  + EX2)
    
    ```sql
    SELECT JOB
    FROM EMP
    GROUP BY JOB
    HAVING COUNT(*) > 0
    ORDER BY SAL;
    ```
  
  + -> ERROR : GROUP BY절에 사용하지 않은 일반 컬럼을 ORDER BY절에 서용할 수 없음. 





#### 2. DCL(Data Control Language)

+ **DCL의 개념**
  
  + DCL(Data Control Language)은 유저를 생성하고 권한을 제어하는 명령어.
  
  + 대부분의 데이터베이스는 데이터의 보호와 보안을 위해 유저와 권한 관리.
    
    | Oracle에서 제공하는 유저 | 역할                                                      |
    | ---------------- | ------------------------------------------------------- |
    | SYS              | DBA 역할을 부여받은 유저                                         |
    | SYSTEM           | 데이터베이스의 모든 시스템 권한을 부여받은 DBA 유저 (Oracle 설치 완료 시 패스워드 설정) |



+ DCL 명령어
  
  | 명령어    | 설명                                                                       |
  | ------ | ------------------------------------------------------------------------ |
  | GRANT  | 권한을 부여하는 명령어<br>ex)GRANT CREATE SESSION TO SQLD;<br>(SQLD 시스템 권한 부여)     |
  | REVOKE | 주어진 권한을 회수하는 명령어<br>ex)REVOKE CREATE SESSION FROM SQLD;<br>(SQLD의 권한 취소) |



+ 오브젝트 권한(Objact Privilege)
  
  + 권한(Privilege)
    
    | 권한         | 설명                                                 |
    | ---------- | -------------------------------------------------- |
    | ALTER      | 지정된 테이블에 대해서 수정할 수 있는 권한 부여<br>(테이블, SEQUENCE)     |
    | DELETE     | 지정된 테이블에 대해서 DELETE권한 부여<br>(테이블, VIEWS)           |
    | ALL        | 테이블에 대한 모든 권한 부여                                   |
    | INDEX      | 지정된 테이블에 대해서 인덱스를 생성할 수 있는 권한 부여<br>(테이블)          |
    | INSERT     | 지정된 테이블에 대해서 INSERT권한 부여<br>(테이블, VIEWS)           |
    | REFERENCES | 지정된 테이블을 참조하는 제약조건을 생성하는 권한 부여<br>(테이블)            |
    | SELECT     | 지정된 테이블에 대해서 SELECT권한 부여<br>(테이블, VIEWS, SEQUENCE) |
    | UPDATE     | 지정된 테이블에 대해서 UPDATE권한 부여<br>(테이블, VIEWS)           |



+ **Role을 이용한 권한 부여**
  
  + ROLE은 많은 데이터베이스에서 유저들과 권한들 사이에서 중개 역할을 함.
  
  + ROLE은 유저에게 직접 부여될 수 있고, 다른 ROLE에 포함하여 유저에게 부여될 수 있음.
  
  + EX1)
    
    ```sql
    CONN SYSTEM/MANAGER; //연결
    
    CREATE ROLE LOGIN_TABLE; //롤 생성
    
    GRANT CREATE SESSION, CREATE TABLE TO LOGIN_TABLE; //권한 부여
    
    GRANT LOGIN_TABLE TO SQLD; // 권한 부여
    
    CONN SQLD/1234; //연결
    
    CREATE TABLE MENU2(PRICE NUMBER NOT NULL, TITLE VARCHAR2(10)); 
    //테이블 생성
    ```
  
  + -> 권한 취소할 때는 REVOKE 사용
  
  
  
  

#### 3. TCL(Transaction Control Language)

+ **트랜잭션(Transaction)**
  
  + 데이터베이스의 논리적 연산단위
  
  + 하나의 트랜잭션에는 하나 이상의 SQL문장 포함.
  
  + 트랜잭션은 분할 할 수 없는 최소의 단위.
    
    -> 전부 적용하거나 전부 취소.
    
    | 특성                   | 설명                                                                           |
    | -------------------- | ---------------------------------------------------------------------------- |
    | 원자성<br>(Atomicity)   | 트랜잭션에서 정의된 연산들은 모두 성공적으로 실행되던지 아니면 실행되지 않은 상태여야 함.                           |
    | 일관성<br>(Consistency) | 트랜잭션이 실행되기 전의 데이터베이스 내용이 잘못 되어 있지 않다면 트랜잭션이 실행된 이후에도 데이터베이스의 내용에 잘못이 있으면 안됨. |
    | 고립성<br>(Isolation)   | 트랜잭션이 실행되는 도중에 다른 트랜잭션이 접근할 수 없음.                                            |
    | 영속성<br>(Durability)  | 트랜잭션이 성공적으로 수행되면 그 트랜잭션이 갱신한 데이터베이스의 내용은 영구적으로 저장됨.                          |
    
    

+ **TCL**
  
  + 트랜잭션을 제어하는 명령어.
    
    | 명령어       | 설명                                                                   |
    | --------- | -------------------------------------------------------------------- |
    | COMMIT    | -DML(INSERT, UPDATE, DELETE)로 변경한 데이터를 데이터베이스에 반영하는 명령어              |
    | ROLLBACK  | -트랜잭션을 취소하는 명령어.<br>-마지막 COMMIT지점으로 돌아간다.                            |
    | SAVEPOINT | -ROLLBACK시 돌아가는 저장포인트를 지정하는 명령어<br>-하나의 트랜잭션에 여러 개의 SAVEPOINT 지정 가능. |





#### 4. JOIN

+ **조인(JOIN) 개념**
  
  + 
