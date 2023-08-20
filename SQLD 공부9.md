# SQLD 공부

## 2과목 SQL 기본 및 활용 (SQL 활용)

#### 1.  서브쿼리

+ **서브쿼리(Subquery)의 개념**
  
  + 서브쿼리는 하나의 SQL문안에 포함되어 있는 또 다른 SQL문 의미.
  
  + 서브쿼리는 단일 행 또는 복수 행 비교 연산자와 함께 사용 가능.
  
  + 단일 행 비교 연산자는 서브쿼리의 결과가 반드시 1건 이하.
  
  + 복수 행 비교 연산자는 서브쿼리의 결과 건수와 상관 없음.
  
  + 서브쿼리에서는 ORDER BY 사용 불가. ORDER BY절은 메인쿼리의 마지막 문장에 위치해야 함.
  
  + 서브쿼리 사용 가능 : SELECT, FROM, WHERE, HAVING, ORDER BY, UPDATE문의 SET, INSERT문의 VALUES절


+ **서브쿼리의 분류**
  
  + 데이터 형태에 따른 서브쿼리 분류
    
    | 서브쿼리 종류                               | 설명                                                                         |
    | ------------------------------------- | -------------------------------------------------------------------------- |
    | 단일 행 서브쿼리<br>(Single Row Subquery)    | - 서브쿼리의 실행 결과가 항상 1건 이하인 서브쿼리<br>- 단일 행 비교 연산자와 함께 사용(=, <, <=, >, >=, <>) |
    | 다중 행 서브쿼리<br>(Multi Row Subquery)     | - 서브쿼리의 실행 결과가 1건 이상인 서브쿼리<br>- 다중 행 비교 연산자와 함께 사용(IN, ALL, ANY, EXISTS)   |
    | 다중 컬럼 서브쿼리<br>(Multi Column Subquery) | - 서브쿼리의 실행 결과로 여러 컬럼 반환.<br>- 메인쿼리의 조건절에 여러 컬럼을 동시 비교.                     |


+ 동작하는 방식에 따른 서브쿼리 분류
  
  | 서브쿼리 종류                              | 설명                                                            |
  | ------------------------------------ | ------------------------------------------------------------- |
  | 연관 서브쿼리<br>(Correlated Subquery)     | 서브쿼리가 메인쿼리 컬럼을 가지고 있는 형태                                      |
  | 비연관 서브쿼리<br>(Un-Correlated Subquery) | - 서브쿼리가 메인쿼리 컬럼을 가지고 있지 않은 형태<br>- 서브쿼리에 메인쿼리의 값을 제공하기 위해 사용. |


+ **데이터 형태에 따른 서브쿼리 분류**
  
  + 단일 행 서브쿼리(Single Row Subquery)
    
    + 서브쿼리의 결과 건수가 2건 이상을 반환하면 SQL문은 실행시간 오류 발생.
    
    + 예제1
      
      ```sql
      SELECT EMPNO, ENAME, SAL, DEPTNO
      FROM EMP
      WHERE DEPTNO = (SELECT DEPTNO
                      FROM EMP
                      WHERE ENAME = 'FORD');
      //FORD와 같은 부서에 근무하는 사원들의 정보 출
      ```
    
    + 예제2
      
      ```sql
      SELECT EMPNO, ENAME, JOB, DEPTNO, MGR
      FROM EMP
      WHERE DEPTNO = (SELECT DEPTNO
                      FROM DEPT
                      WHERE LOC = 'CHICAGO')
      AND MGR = (SELECT EMPNO
                 FROM EMP
                 WHERE ENAME = 'BLAKE');
      //시카고에 근무하는 사원들 중 BLAKE가 상관인 사원들의 정보 출력
      ```

+ **다중 행 서브쿼리(Multi Row Subquery)**
  
  + 단일 행 서브쿼리에도 사용 가능.
    
    | 서브쿼리 종류 | 설명                                                                                                |
    | ------- | ------------------------------------------------------------------------------------------------- |
    | IN      | - 서브쿼리의 결과에 존재하는 임의의 값과 동일 조건.<br>- 메인쿼리의 비교조건이 서브쿼리의 결과 중 하나만 동일하면 참.<br>- OR 조건                 |
    | ALL     | - 서브쿼리의 결과에 존재하는 모든 값을 만족하는 조건<br>- 메인쿼리와 서브쿼리의 결과가 모두 동일하면 참<br>> ALL : 최소값 반환<br>< ALL : 최대값 반환 |
    | ANY     | - 서브쿼리의 결과에 존재하는 어느 하나의 값이라도 만족하는 조건<br>> ANY : 하나라도 작게되면 참<br>< ANY : 하나라도 크게되면 참                |
    | EXISTS  | - 서브쿼리의 결과를 만족하는 값이 존재하는 지 여부 확인<br>- 메인쿼리와 서브쿼리의 결과가 하나라도 존재하면 참                                 |
  
  + 예제1 (IN)
    
    ```sql
    SELECT EMPNO, ENAME, SAL, DEPTNO
    FROM EMP
    WHERE DEPTNO IN (SELECT DEPTNO
                     FROM EMP
                     WHERE SAL >= 3000);
    //SAL이 3000이상인 사원들과 같은 부서에서 일하는 사원들의 정보 출
    ```
  
  + 예제2 (ALL)
    
    ```sql
    SELECT EMPNO, ENAME, SAL, DEPTNO
    FROM EMP
    WHERE SAL > ALL (SELECT AVG(SAL)
                     FROM EMP
                     GROUP BY DEPTNO);
    //모든 부서별 급여 평균보다 많이 받는 사원들 정보 출
    ```
  
  + 예제3 (ANY)
    
    ```sql
    SELECT EMPNO, ENAME, SAL, DEPTNO
    FROM EMP
    WHERE SAL > ANY (SELECT MIN(SAL)
                     FROM EMP
                     GROUP BY DEPTNO);
    //어느 부서별 최저 급여보다 더 많이 받는 사원들 정보 출력.
    //즉, 부서별 최저 SAL 중 가장 적은 최저 SAL보다 많은 급여 받는 사원 조회
    ```
  
  + 예제4(EXISTS)
    
    ```sql
    SELECT EMPNO, ENAME, SAL
    FROM EMP
    WHERE EXISTS (SELECT *
     FROM EMP
     WHERE SAL >= 3000);
    //사원들의 정보 출력.
    //(단 사원 중 SAL이 3000이상인 사원이 있을 때만 반환.)
    ```



+ **다중 컬럼 서브쿼리(Multi Column Subquery)**
  
  + SQL Server에서는 지원되지 않음.
  
  + 예제
    
    ```sql
    SELECT EMPNO, ENAME, MGR, DEPTNO
    FROM EMP
    WHERE (MGR, DEPTNO) IN (SELECT MGR, DEPTNO
                            FROM EMP
                            WHERE ENAME = 'FORD');
    //'FORD'와 MGR, DEPTNO가 같은 사원의 정보 출력.
    ```



+ **동작하는 방식에 따른 서브쿼리 분류**
  
  + 연관 서브쿼리 예제
    
    ```sql
    SELECT A.EMPNO, A.ENAME, A.SAL, A.DEPTNO
    FROM EMP A
    WHERE A.SAL > (SELECT AVG(B.SAL)
                   FROM EMP B
                   WHERE A.DEPTNO = B.DEPTNO);
    //자신이 속한 부서의 평균 급여보다 많이 받는 사원들의 정보 출력.
    ```



+ **스칼라 서브쿼리(Scalar Subquery)**
  
  + 스칼라 서브쿼리는 SELECT절에 사용.
  
  + 스칼라 서브쿼리는 '한 행, 한 컬럼' 만을 반환하는 서브쿼리.
  
  + 결과가 2건 이상 반환하면 에러 발생.(단일행 서브쿼리이기 때문)
  
  + 컬럼을 쓸 수 있는 대부분의 곳에서 사용 가능.
  
  + 예제
    
    ```sql
    SELECT *
    FROM (SELECT ROWNUM AS A, ENAME
          FROM EMP)
    WHERE A=4;
    //EMP테이블에서 4번째
    ```



+ **인라인 뷰(Inline View)**
  
  + FROM절에서 사용되는 서브쿼리를 인라인 뷰라고 함.
  
  + SQL문이 실행될 때만 임시적으로 생성되는 동적인 뷰. ->데이터베이스에 해당 정보가 저장되지 않음.
  
  + 일반적인 뷰 : 정적 뷰 / 인라인 뷰 : 동적 뷰
  
  + 예제
    
    ```sql
    SELECT *
    FROM (SELECT ROWNUM AS A, EMPNO, ENAME, SAL, DEPTNO
          FROM EMP)
    WHERE A=4 OR A=6;
    //EMP테이블에서 4,6번째 사원의 정보 출
    ```
