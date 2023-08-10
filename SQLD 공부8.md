# SQLD 공부

## 2,과목 SQL 기본 및 활용 (SQL 활용)

#### 1. 집합 연산자

+ **집합 연산자(SET OPERATOR)의 개념**
  
  + 집합 연산자를 사용하면 두 개 이상의 테이블에서 조인을 사용하지 않고 연관된 데이터를 조회할 수 있다.
  
  + 두 개 이상의 질의 결과를 하나의 결과로 만들어 준다.
  
  + SELECT절의 칼럼 수가 동일하고, SELECT절의 동일 위치에 존재하는 컬럼의 데이터 타입이 상호 호환가능해야 한다.(반드시 동일한 데이터 타입일 필요는 없음.)



+ **집합 연산자(SET OPERATOR)의 종류**
  
  |              | 설명                                                                                                                      |
  | ------------ | ----------------------------------------------------------------------------------------------------------------------- |
  | UNION        | 여러 개의 SQL문의 결과에 대한 합집합. 결과에서 모든 중복된 행은 하나의 행으로 표시                                                                       |
  | UNION ALL    | - 여러 개의 SQL문의 결과에 대한 합집합. 결과에서 모든 중복된 행은 그대로 결과로 표시<br>- 개별 SQL문의 결과가 서로 중복되지 않는 경우, UNION과 결과가 동일.(정렬 순서는 차이가 있을 수 있음) |
  | INTERSECT    | 여러 개의 SQL문의 결과에 대한 교집합. 중복된 행은 하나의 행으로 표시                                                                               |
  | MINUS/EXCEPT | 선행 SQL문의 결과에서 후행 SQL문의 결과에 대한 차집합. MINUS는 Oracle에서 사용.                                                                  |
  
  
  
  + UNION
    
    + 마지막 SELECT문에 정수 표현법으로 ORDER BY 사용 가능.
      
      ```sql
      SELECT * FROM 테이블1
      UNION 
      SELECT * FROM 테이블2
      ORDER BY 정수;     //정수는 컬럼위치를 의미함.
      ```
    
    
  
  + UNION ALL
    
    + 마지막 SELECT문에 정수 표현법으로 ORDER BY 사용 가능.
    
    + 중복 제거 및 정렬 작업이 없어서 UNION보다 성능상 유리함.
      
      ```sql
      SELECT * FROM 테이블1
      UNION ALL
      SELECT * 테이블2
      ORDER BY 정수;    //정수는 컬럼위치를 의미함.
      ```
    
    
  
  + INTERSECT
    
    + 마지막 SELECT문에 정수 표현법으로 ORDER BY 사용 가능.
      
      ```sql
      SELECT * FROM 테이블1
      INTERSECT
      SELECT * FROM 테이블2
      ORDER BY 정수;    //정수는 컬럼위치를 의미함.
      ```
    
    
  
  + MINUS
    
    + 마지막 SELECT문에 정수 표현법으로 ORDER BY 사용 가능.
      
      ```sql
      SELECT * FROM 테이블1
      MINUS
      SELECT * FROM 테이블2
      ORDER BY 정수;    //정수는 컬럼위치를 의미함.
      ```





#### 2. 계층형 질의

+ **계층형 질의**
  
  + 계층형 데이터란 동일 테이블에 계층적으로 상위와 하위 데이터가 포함된 데이터.
  
  + 테이블에 계층형 데이터가 존재하는 경우 데이터 조회 위해 계층형 질의 사용.



+ **계층형 질의 문법**
  
  + START WITH 절은 계층 구조 전개의 시작 위치를 지정하는 구문. 즉, 루트 데이터 지정.
  
  + CONNECT BY절은 다음에 전개될 자식 데이터를 지정하는 구문.
    
    ```sql
    SELECT *
    FROM 테이블
    WHERE 조건절    //모든 전개를 수행한 후 지정된 조건을 만족하는 데이터만 추출
    START WITH 조건  //계층 구조의 시작 위치 결정
    CONNECT BY [NOCYCLE] 조건 
    //PRIOR를 이용해 부모와 자식 데이터의 관계 정의(순방향, 역방향)
    //PRIOR 자식 : 부모->자식    PRIOR 부모 : 자식->부모
    //NOCYCLE : 사이클이 발생한 이후의 데이터는 전개하지 않음.
    [ORDER SIBLINGS BY 컬럼명] //형제 노드에서 정렬 수행
    ```



+ **계층형 질의 가상 컬럼, 함수**
  
  + 계층형 질의 가상 컬럼에는 LEVEL, CONNECT_BY_ISLEAF, CONNECT_BY_ISCYCLE이 있다.
  
  + 계층형 질의 함수에는 SYS_CONNECT_BY_PATH, CONNECT_BY_ROOT가 있다.
    
    |                     | 설명                                                                 |
    | ------------------- | ------------------------------------------------------------------ |
    | LEVEL               | 루트 데이터의 LEVEL은 1, 하위 데이터는 리프 데이터까지 1씩 증가                           |
    | CONNECT_BY_ISLEAF   | 전개 과정에서 해당 데이터가 리프 데이터면 1, 아니면 0                                   |
    | CONNECT_BY_ISCYCLE  | CYCLE이 존재하면 1, 아니면 0. CYCLE옵션을 사용했을 때만 사용                          |
    | SYS_CONNECT_BY_PATH | 루트 데이터에서 현재 전개할 데이터까지의 경로 표시<br>`SYS_CONNECT_BY_PATH(컬럼명, 경로분리기호)` |
    | CONNECT_BY_ROOT     | 현재 전개할 데이터의 루트 데이터 표시<br>`CONNECT_BY_ROOT(컬럼명)`                    |



+ **순방향 계층형 질의**
  
  + 순방향 계층형 질의는 계층형 데이터를 상위에서 하위로 전개하는 질의.
  
  + PRIOR 자식 = 부모 형태 사용.
  
  + 예제1
    
    ```sql
    SELECT EMPNO, ENAME, JOB, MGR, SAL, LEVEL
    //MGR이 NULL인 열의 LEVEL이 1.
    FROM EMP
    WHERE SAL <= 2000 //급여 2000이하인 사원만 출력
    START WITH MGR IS NULL //MGR이 NULL인 데이터부터 시작.
    CONNECT BY PRIOR EMPNO = MGR; //순방향 전개
    //    =>최상위 관리자부터 상위 직원 순으로 출력. 
    //    출력 결과 : LEVEL 숫자가 큰 사원부터 출력됨
    ```
  
  + 예제2
    
    ```sql
    SELECT EMPNO, ENAME, MGR, LEVEL, 
    SYS_CONNECT_BY_PATH(EMPNO, '/') PATH
    FROM EMP
    START WITH MGR IS NULL
    CONNECT BY PRIOR EMPNO = MGR
    ORDER SIBLINGS BY EMPNO;
    ```
  
  + 
  
  + 
  
  + 
  
  + 
  
  + 
  
  + 
  
  + 
  
  + 
  
  + 
