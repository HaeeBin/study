# SQLD 공부

## 2과목 SQL 기본 및 활용 (SQL 활용)

#### 1.그룹 함수

+ **그룹 함수(GROUP FUNCTION)**
  
  + 그룹 함수는 테이블에서 선택한 행을 컬럼 값에 따라 그룹화하여 결과를 출력하는 함수.
    
    | 그룹 함수 유형      | 설명                      |
    | ------------- | ----------------------- |
    | ROLLUP        | 지정된 컬럼의 소계 및 총계를 구하는 함수 |
    | GROUPING      | 컬럼의 소계 여부 확인            |
    | GROUPING SETS | 집계 대상 컬럼에 대한 소계 계산      |
    | CUBE          | 결합 가능한 모든 값에 대해 집계 계산   |
    
    
  
  + ROLLUP 함수
    
    + 지정 컬럼의 수보다 하나 더 큰 레벨의 Subtotal 생성.
    
    + 계층구조로 GROUP BY 컬럼순서가 바뀌면 결과 값이 달라짐.
      
      ```sql
      SELECT 컬럼명, 집계함수
      FROM 테이블명
      [WHERE 조건절]
      GROUP BY [컬럼명] ROLLUP(그룹화할 컬럼)
      [HAVING ...] [ORDER BY ...]
      
      ```
      
      
    
    + 예제1
      
      ```sql
      SELECT DEPTNO, SUM(SAL)
      FROM EMP
      GROUP BY ROLLUP(DEPTNO);
      //DEPTNO별 소계, 전체 합계 표시.
      ```
    
    + 예제2
      
      ```sql
      SELECT DEPTNO, JOB, SUM(SAL)
      FROM EMP
      GROUP BY ROLLUP(DEPTNO, JOB);
      //DEPTNO별 소계, (DEPTNO, JOB)별 소계, 전체 합계 조회.
      ```
    
    
  
  + GROUPING SETS 함수
    
    + GROUP BY SQL 문장을 여러 번 반복하지 않아도 원하는 결과를 얻을 수 있다.
    
    + GROUP BY 컬럼 순서와 무관하게 개별적으로 모두 처리.
      
      ```sql
      SELECT 컬럼명, 집계함수
      FROM 테이블명
      [WHERE 조건절]
      GROUP BY [컬럼명] GROUPING SETS(그룹화할 컬럼)
      [HAVING ...] [ORDER BY ...]
      
      ```
      
      
    
    + 예제1
      
      ```sql
      SELECT DEPTNO, SUM(SAL)
      FROM EMP
      GROUP BY GROUPING SETS(DEPTNO);
      //DEPTNO별 소계 표시.
      ```
    
    + 예제2
      
      ```sql
      SELECT DEPTNO, JOB, SUM(SAL)
      FROM EMP
      GROUP BY GROUPING SETS(DEPTNO, JOB);
      //DEPTNO별 소계, JOB별 소계.
      ```
    
    
  
  + CUBE 함수
    
    + 모든 켤합 가능한 경우의 수를 구하므로, 다른 그룹함수보다 시스템에 대한 부하가 큼.
    
    + 다차원 집계 생성.
      
      ```sql
      SELECT 컬럼명, 집계함수
      FROM 테이블명
      [WHERE 조건절]
      GROUP BY [컬럼명] CUBE(그룹화할 컬럼)
      [HAVING ...] [ORDER BY ...]
      ```
    
    + 예제1
      
      ```sql
      SELECT DEPTNO, SUM(SAL)
      FROM EMP
      GROUP BY CUBE(DEPTNO);
      //DEPTNO별 소계, 전체 합계 표시.
      ```
    
    + 예제2
      
      ```sql
      SELECT DEPTNO, JOB, SUM(SAL)
      FROM EMP
      GROUP BY CUBE(DEPTNO, JOB);
      //DEPTNO별 소계, JOB별 소계, (DEPTNO, JOB)별 소계, 전체 합계 조회.
      ```
    
    
  
  + GROUPING 함수
    
    + ROLLUP, GROUPING SETS, CUBE에서 생성되는 합계값을 구분하기 위해 사용.
    
    + 소계나 합계가 계산되면 1, 아닌 경우 0 반환.
    
    + SELECT절과 HAVING절에 사용 가능.
    
    + 예제1
      
      ```sql
      SELECT DEPTNO, JOB, SUM(SAL), 
             GROUPING(DEPTNO) AS DEPTNO,
             GROUPING(JOB) AS JOB
      FROM EMP
      GROUP BY ROLLUP(DEPTNO, JOB);
      //DEPTNO별 소계, (DEPTNO, JOB)별 소계, 전체 합계
      //DEPTNO와 JOB 소계 사용여부 표시. 
      ```
    
    + 예제2
      
      ```sql
      SELECT DEPTNO, JOB, SUM(SAL)
             GROUPING(DEPTNO) AS DEPTNO
             GROUPING(JOB) AS JOB
      FROM EMP
      GROUP BY CUBE(DEPTNO, JOB);
      //DEPTNO별 소계, JOB별 소계, (DEPTNO, JOB)별 소계, 전체 합계
      //DEPTNO와 JOB소계 사용여부 표시.
      ```
    
    
  
  + 인수 개수와 순서에 따른 그룹 함수 비교
    
    | 유형            | 설명                                                                     |
    | ------------- | ---------------------------------------------------------------------- |
    | ROLLUP        | - 인수가 1개일 때 CUBE와 같은 결과<br>- 인수가 2개 이상 : 모두 다른 결과<br>- 인수 순서에 따라 다른 결과 |
    | GROUPING SETS | - 인수가 2개 이상 : 모두 다른 결과<br>- 인수 순서와 무관.                                 |
    | CUBE          | - 인수가 1개일 때 : ROLLUP과 같은 결과<br>- 인수가 2개 이상 : 모두 다른 결과<br>- 인수 순서와 무관.  |
    
    
    
    
    
    
