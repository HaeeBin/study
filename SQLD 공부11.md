# SQLD 공부

## 2과목 SQL 기본 및 활용 (SQL 활용)

#### 1. 윈도우 함수

+ **윈도우 함수(WINDOW FUNCTION)**
  
  + 여러 행간의 관계를 정의하는 함수
  
  + 서브쿼리에도 사용가능하지만 함수 자체에서 중첩해서 사용하지는 못한다.
  
  + 순위, 합계, 평균, 행 위치 등의 조작 가능.
    
    ```sql
    SELECT 윈도우 함수(인수) OVER
                (
                  [PARTITION BY 컬럼명] //전체를 기준에 의해 소그룹으로 분류.
                  [ORDER BY 컬럼명] //그룹 내에서 순서 정
                  [WINDOWING 절]
                 )
    FROM 테이블명
    ```
 
  + WINDOWING 절 문법
    
    ```sql
    ROWS | RANGE 
    //ROWS : 물리적 결과의 행 수.
    //RANGE : 논리적 값에 의한 범위.(VALUE 기
    BETWEEN start
    AND end
    ```
  
  + 윈도우 함수 종류
    
    | 종류         | 설명                           | 함수                                               |
    | ---------- | ---------------------------- | ------------------------------------------------ |
    | 순위 관련 함수   | 특정항목 및 파티션에 대해 순위 계산         | RANK, DENSE_RANK, ROW_NUMBER                     |
    | 집계 관련 함수   | 여러 행 또는 테이블 전체 행으로부터 결과값 반환. | SUM, AVG, COUNT, MAX, MIN                        |
    | 행 순서 관련 함수 | 특정 위치의 행 반환.                 | FIRST_VALUE, LAST_VALUE, LAG, LEAD               |
    | 비율 관련 함수   | 백분율과 같은 비율과 관련된 결과 반환        | CUME_DIST, RANTIO_TO_REPORT, PERCENT_RANK, NTILE |





+ **순위 관련 함수**
  
  + 순위 정렬을 위해 ORDER BY가 필수로 사용된다.
    
    | 종류         | 설명                                                        |
    | ---------- | --------------------------------------------------------- |
    | RANK       | - 동일한 값에 대해서는 동일한 순위 부여. <br>- 공동 순위가 있다면 다음 등수는 제거하여 부여. |
    | DENSE_RANK | - 동일한 값에 대해서는 동일 순위 부여. <br>- 공동 순위가 있어도 상관없이 다음 등수 부여.   |
    | ROW_NUMBER | - 동일 값에 대해서도 다른 순위 부여.                                    |
    
    
  
  + 예제
    
    ```sql
    SELECT EMPNO, ENAME, SAL,
        RANK () OVER(ORDER BY SAL) RANK,
        DENSE_RANK () OVER(ORDER BY SAL) DENSE_RANK,
        ROW_NUMBER () OVER(ORDER BY SAL) ROW_NUMBER
    FROM EMP;
    ```





+ **집계 관련 함수**
  
  | 종류    | 설명             |
  | ----- | -------------- |
  | SUM   | 파티션 별로 합계 계산.  |
  | AVG   | 파티션 별로 평균 계산.  |
  | COUNT | 파티션 별로 행 수 계산. |
  | MAX   | 파티션 별로 최댓값 계산. |
  | MIN   | 파티션 별로 최솟값 계산. |
  
  
  
  + 예제(SUM)
    
    ```sql
    SELECT EMPNO, DEPTNO, SAL,
     SUM(SAL) OVER () SUM1, //전체 급여 합계 조회.(모든 행이 다 같은 값).
     SUM(SAL) OVER(ORDER BY SAL) SUM2 //전체 급여 누적 합계 조회.
     //행의 SAL값까지의 합계가 결과로 나옴.
    FROM EMP;
    
    
    SELECT EMPNO, DEPTNO, SAL,
        SUM(SAL) OVER (PARTITION BY DEPTNO) SUM3,
        //부서별 전체 급여 합계 조회. 같은 부서끼리 같은 값.
        SUM(SAL) OVER (PARTITION BY DEPTNO ORDER BY SAL) SUM4
        //부서별 급여 누적 합계 조회. 같은 부서에서의 자신의 값까지의 합계.
    FROM EMP;
    ```
    
    
  
  + 예제(AVG)
    
    ```sql
    SELECT EMPNO, DEPTNO, SAL,
     ROUND(AVG(SAL) OVER (), 1) AVG1, 
    //전체 급여 평균 조회.(소수 첫째자리까지). 
    //다 같은 값.
     ROUND(AVG(SAL) OVER (ORDER BY SAL), 1) AVG2
     //전체 급여 누적 평균 조회.(소수 첫째자리까지).
    FROM EMP; 
    
    SELECT EMPNO, DEPTNO, SAL,
     ROUND(AVG(SAL) OVER(PARTITION BY DEPTNO), 1) AVG3,
     //부서별 전체 급여 평균 조회.(부서별 같은 값.)
     ROUND(AVG(SAL) OVER(PARTITION BY DEPTNO
                         ORDER BY SAL), 1) AVG4 FROM EMP;
     //부서별 급여 누적 평균 조회.
    ```
    
    
  
  + 예제(COUNT)
    
    ```sql
    SELECT EMPNO, DEPTNO, SAL,
        COUNT(*) OVER() COUNT1, //전체 인원 조회.
        COUNT(*) OVER(ORDER BY SAL) COUNT2 //전체 누적 인원 조회.
    FROM EMP;
    
    
    SELECT EMPNO, DEPTNO, SAL,
        COUNT(*) OVER (PARTITION BY DEPTNO) COUNT3, //부서별 전체인원.
        COUNT(*) OVER (PARTITION BY DEPTNO ORDER BY SAL) COUNT4
        //부서별 누적 인원 조회.
    FROM EMP;
    ```
    
    
  
  + 예제(MAX, MIN)
    
    ```sql
    SELECT EMPNO, DEPTNO, SAL,
     MAX(SAL) OVER () MAX1, //전체 최대 급여 조회. 모든 행 같은 값.
     MIN(SAL) OVER () MIN1, //전체 최소 급여 조회. 모든 행 같은 값.
     MAX(SAL) OVER (ORDER BY SAL) MAX2, //전체 누적 최대 급여 조회.
     MIN(SAL) OVER (ORDER BY SAL) MIN2 //전체 누적 최소 급여 조회.
    FROM EMP;
    
    SELECT EMPNO, DEPTNO, SAL,
     MAX(SAL) OVER (PARTITION BY DEPTNO) MAX3, //부서별 최대 급여.
     MIN(SAL) OVER (PARTITION BY DEPTNO) MIN3, //부서별 최소 급여.
     MAX(SAL) OVER (PARTITION BY DEPTNO ORDER BY SAL) MAX4,
     MIN(SAL) OVER (PARTITION BY DEPTNO ORDER BY SAL) MIN4 
    FROM EMP;
    ```
