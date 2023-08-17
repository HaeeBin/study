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
    
    ```
