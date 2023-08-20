# SQLD 공부

## 2과목 SQL 기본 및 활용 (SQL 활용)

#### 1. 윈도우 함수

+ **행 순서 관련 함수**
  
  | 종류          | 설명                                               |
  | ----------- | ------------------------------------------------ |
  | FIRST_VALUE | - 파티션 별 윈도우에서 가장 먼저 나오는 값 반환.<br>- MIN함수와 같은 결과. |
  | LAST_VALUE  | -가장 마지막 값을 반환. <br>- MAX함수와 같은 결과.               |
  | LAG         | -이전 행의 특정 위치 행을 반환. <br>- 기본값 = 1                |
  | LEAD        | -이후 행의 특정 위치 행 반환. <br>- 기본값 = 1                 |
  
  
  
  + FIRST_VALUE 예제
    
    ```sql
    SELECT ENAME, DEPTNO, SAL,
        RANK() OVER (PARTITION BY DEPTNO ORDER BY SAL DESC) RANK,
        FIRST_VALUE(ENAME) OVER (PARTITION BY DEPTNO 
                                 ORDER BY SAL DESC) FIRST
    //사원의 이름을 조회하기 때문에 FIRST_VALUE(인수) => 인수 자리에 ENAME.
    FROM EMP;
    //부서별 직원들의 연봉이 높은 순서로 정렬 후, 부서별 최초로 나오는 사원 이름 출력.
    //부서별 연봉이 가장 높은 사원이름 출력됨.
    ```
  
  
  
  + LAST_VALUE 예제
    
    ```sql
    SELECT EMPNO, ENAME, DEPTNO, SAL,
     LAG(SAL, 2) OVER (PARTITION BY DEPTNO ORDER BY SAL) LAG,
     //2행 앞의 SAL 조회. 음수는 입력 불가.
     LEAD(SAL, 2) OVER (PARTITION BY DEPTNO ORDER BY SAL) LEAD
     //2행 뒤의 SAL 조회. 음수 입력 불가.
    FROM EMP;
    //부서별 직원들의 SAL이 낮은 순서로 정렬 후, 2행앞과 뒤의 SAL 조회.
    //EX)한 부서의 첫번째 행의 LEAD는 그 부서3번째 행 SAL.
    //EX)한 부서의 세번째 행의 LAG는 그 부서 1번째 행 SAL.
    ```
    
    



+ **비율 관련 함수**
  
  | 종류              | 설명                                                       |
  | --------------- | -------------------------------------------------------- |
  | CUME_DIST       | - 현재 행 이하의 값에 대한 누적 백분율 조회.<br>- 누적 분포상에 위치는 0 ~ 1 사이 값. |
  | RATIO_TO_REPORT | - 파티션 내에 전체 SUM(컬럼)에 대한 행별 컬럼값의 백분율 조회.                  |
  | PERCENT_RANK    | - 파티션 내 순서별 백분율을 계산하여 0 ~ 1 값으로 조회.                      |
  | NTILE           | - 인수 값으로 등분한 결과. <br>- 균등 배분 후 남은 행은 앞에서부터 순차적으로 할당.     |
  
  
  
  + 예제
    
    ```sql
    //부서별 사원들의 집합에서 본인의 급여가 누적 순서상 몇 번째 위치쯤에 있는지
    //0과 1사이 값으로 출력.
    SELECT EMPNO, ENAME, SAL, DEPTNO,
      ROUND(CUME_DIST() OVER (PARTITION BY DEPTNO
                              ORDER BY SAL), 2) CUME_DIST
      //ROUND : 소수 둘째자리까지 출력.
      //CUME_DIST : 누적 순서상 백분율
    FROM EMP;
    //EX) 부서에 3명이 있으면 첫번째사람부터 각각 0.33, 0.67, 1표시.
    

    //JOB별로 전체 SAL에서 본인 SAL이 차지하는 비율.
    SELECT EMPNO, ENAME, JOB, SAL,
      ROUND(RATIO_TO_REPORT(SAL) OVER (PARTITION BY JOB) * 100)
                                      || '%' AS RATIO_TO_REPORT
      //ROUND : 1의 자리까지 출력.
      // * 100) || '%' : %로 표현하기 위해 100 곱하고 뒤에 % 붙임.
    FROM EMP;


    //부서별로 직원이 본인 SAL이 순서상 상위 몇 % 인지.
    SELECT EMPNO, SAL, DEPTNO,
      RANK() OVER (PARTITION BY DEPTNO
                   ORDER BY SAL) RANK,
      PERCENT_RANK() OVER (PARTITION BY DEPTNO
                           ORDER BY SAL) PERCENT
    FROM EMP;
    //EX)부서에 3명이 있다면 각각 0, 0.5, 1 출력.


    //전체 사원을 SAL내림차순으로 정렬하고 SAL 기준으로 4개 그룹으로 분류.
    SELECT EMPNO, ENAME, SAL,
      NTILE(4) OVER (ORDER BY SAL DESC) NTILE
    FROM EMP;
    //EX)만약 14명이 있다면 4, 4, 3, 3으로 나눠짐.
    //결과는 몇번 그룹인지 숫자로 출력됨.
    ```



#### 2. 절차형 SQL
+ 개념
  + 절차형 SQL을 이용하면 SQL문의 연속적 실행이나 조건에 따른 분기처리를 이용해 특정 기능을 수행하는 저장 모듈을 생성할 수 있다.
 
+ **PL/SQL**
  + BLOCK구조.
  + BLOCK내에는 DML문장과 QUERY문장, 절차형 언어(IF, LOOP) 등 사용 가능.
  + 절차적 프로그래밍을 가능하게 하는 트랜잭션 언어.
  + PL/SQL문장을 데이터베이스 서버에 저장하여 사용자와 애플리케이션 사이에서 공유할 수 있도록 만든 SQL 컴포넌트 프로그램.
 
  + PL/SQL 특징
    + 각 기능별로 모듈화 가능.
    + 변수, 상수 등 선언하여 SQL문장 간 값 교환.
    + DBMS 정의 에러나 사용자 정의 에러를 정의하여 사용 가능.
    + 응용 프로그램의 성능을 향상 시킴.
   
  + PL/SQL 구조
    + DECLARE : BEGIN ~ END절에서 사용될 변수와 인수에 대한 정의 및 데이터 타입을 선언하는 선언부.
    + BEGIN ~ END : 개발자가 처리하고자 하는 SQL문과 여러 비교문, 제어문을 이용해 필요 로직 처리하는 실행부.
    + EXCEPTION : BEGIN ~ END 절에서 실행되는 SQL문이 에러발생하면 그 에러를 어떻게 처리할 것인지 정의하는 예외 처리부.

   
+ **T-SQL**
  + T-SQL은 근본적으로 SQL Server를 제어하기 위한 언어.

 
  + T-SQL의 프로그래밍 기능
    + @@이라는 전역변수(시스템함수)와 @이라는 지역변수가 있다.
    + 지역변수 : 사용자가 연결 시간 동안만 사용하기 위해 만들어지는 변수.
    + 전역변수 : SQL서버에 내장된 값.
    + 데이터 유형 제공.
    + 연산자 사용 가능.
    + IF-ELSE, WHILE, CASE-THEN 사용 가능.(흐름 제어 기능)
    + -- : 한 줄 주석
    + /* 내용 */ : 여러 줄 주석.

   
  + T-SQL 구조
    + DECLARE, BEGIN, ERROR 처리, END => PL/SQL과 유사.

   
+ **Trigger**
  + 특정 테이블에 INSERT, UPDATE, DELETE와 같은 DML문이 수행될 때, 데이터베이스에서 자동으로 동작하도록 작성된 프로그램.
  + 사용자가 직접 호출X.
  + 테이블과 뷰, 데이터베이스 작업을 대상으로 정의 가능.

 
+ **프로시저와 트리거 차이점**
  | 프로시저 | 트리거 |
  | -------- | -------- |
  | CREATE Procedure 문법 사용 | CREATE Trigger 문법 사용 |
  | EXECUTE 명령어로 실행 | 생성 후 자동 실행 |
  | COMMIT, ROLLBACK 가능 | COMMIT, ROLLBACK 실행 안됨 |
