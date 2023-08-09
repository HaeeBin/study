# SQLD 공부

## 2,과목 SQL 기본 및 활용 (SQL 활용)

#### 1. 표준조인

+ **표준조인(STANDARD JOIN)**
  
  +  ANSI/ISO 표준 SQL에서 규정한 INNER JOIN, NATURAL JOIN, USING 조건절, ON 조건절, CROSS JOIN 문법
  
  + 사용자는 테이블간의 JOIN조건을 FROM절에서 명시적으로 정의할 수 있다.
  
  + 일반 집합 연산자 
    
    |              | 설명                                                                                          |
    | ------------ | ------------------------------------------------------------------------------------------- |
    | UNION        | - 수학적 합집합<br>- UNION : 공통 교집합의 중복을 제거하여 표현<br>- UNION ALL : 공통 교집합의 중복을 포함하여 표현. 정렬 작업이 없음. |
    | INTERSECTION | - 수학적 교집합<br>- INTERSECT 사용                                                                 |
    | DIFFERENCE   | - 수학적 차집합<br>- SQL표준 : EXCEPT<br>- Oracle : MINUS                                           |
    | PRODUCT      | - 곱집합<br>- CROSS PRODUCT(CARTESIAN PRODUCT)<br>- JOIN 조건이 없는 경우 생길 수 있는 모든 데이터의 조합          |
    
    
  
  + 순수 관계 연산자
    
    |         | 설명                                                                          |
    | ------- | --------------------------------------------------------------------------- |
    | SELECT  | WHERE절의 조건절 기능으로 구현                                                         |
    | PROJECT | SELECT절의 컬럼 선택 기능으로 구현                                                      |
    | JOIN    | WHERE절의 INNER JOIN조건과 함께 FROM절의 NATURAL JOIN, OUTER JOIN, USING 조건절, ON 조건절 |
    | DIVIDE  | - 나눗셈과 비슷한 개념<br>- SQL에서는 사용하지 않음.                                          |



+ **JOIN 유형**
  
  + JOIN 유형
    
    | 유형           | 설명                                              |
    | ------------ | ----------------------------------------------- |
    | INNER JOIN   | - JOIN 조건에서 동일한 값이 있는 행만 반환<br>- INNER 생략 가능    |
    | NATURAL JOIN | 두 테이블 간의 동일한 이름을 갖는 모든 컬럼들에 대해서 EQUI JOIN(=) 수행 |
    | CROSS JOIN   | 테이블 간 JOIN 조건이 없는 경우 생길 수 있는 모든 데이터의 조합         |
    | OUTER JOIN   | INNER JOIN과 대비. JOIN 조건에서 동일한 값이 없는 행도 반환       |
    
    
  
  + JOIN 조건절
    
    | 유형        | 설명                                               |
    | --------- | ------------------------------------------------ |
    | USING 조건절 | 동일한 이름을 가진 컬럼들 중에서 원하는 컬럼에 대해서만 선택적으로 JOIN 조건 사용 |
    | ON 조건절    | 동일한 이름을 갑지 않은 컬럼에 대해서도 JOIN 조건 사용 가능             |
    
    
  
  + INNER JOIN
    
    + USING 조건절이나 ON 조건절을 필수적으로 사용해야 함.
      
      ```sql
      SELECT *
      FROM 테이블1 (INNER) JOIN 테이블2 //INNER 키워드는 생략 가능
      ON 조건절
      ```
    
    
  
  + NATURAL JOIN
    
    + WHERE 절에서 JOIN조건, ON 조건저르 USING 조건절을 사용할 수 없음.
      
      ```sql
      SELECT *
      FROM 테이블1 NATURAL JOIN 테이블2; //두 테이블의 공통 컬럼 자통 선택
      ```
    
    
  
  + ON 조건절
    
    + WHERE  조건절과 ON 조건절을 혼용해서 사용할 수 있음.
      
      ```sql
      SELECT *
      FROM 테이블1 JOIN 테이블2 
      ON 조건절;
      ```
    
    
  
  + USING 조건절
    
    + USING 절에 사용한 컬럼명 앞에는 접두어를 사용할 수 없음.
    
    + SQL Server에서는 지원하지 않음.
      
      ```sql
      SELECT *
      FROM 테이블1 JOIN 테이블2
      USING(공통 컬럼명); // 테이블명.컬럼명 사용X 오직 컬럼명만 써야함.
      //두 테이블의 공콩 컬럼이 데이터 유형도 동일해야 함.
      ```
    
    
  
  + CROSS JOIN
    
    + CARTESIAN PRODUCT와 같은 의미.
      
      ```sql
      SELECT *
      FROM 테이블1 CROSS JOIN 테이블2; //JOIN 조건 정의X.
      ```
    
    
  
  + 다중 테이블 JOIN
    
    + 3개 이상의 테이블 간 JOIN 조건 정의.
    
    + WHERE 조건절 또는 ON 조건절 사용,
      
      ```sql
      SELECT *
      FROM 테이블1, 테이블2, 테이블3 ...
      WHERE 조건절;
      
      SELECT *
      FROM 테이블1 JOIN 테이블2 ON 조건절
      JOIN 테이블3 ON 조건절 ...;
      ```
    
    
  
  + OUTER JOIN
    
    + 동일한 값이 없는 행은 NULL로 표시.
    
    + ON 조건절에 (+)를 이용해 OUTER JOIN 나타낼 수 있음.<br>**(FULL OUTER JOIN에서는 사용X.)**
      
      | 유형               | 설명                                            |
      | ---------------- | --------------------------------------------- |
      | LEFT OUTER JOIN  | 두 개의 테이블에서 같은 것을 조회하고 왼쪽 테이블에만 있는 것을 포함해서 조회  |
      | RIGHT OUTER JOIN | 두 개의 테이블에서 같은 것을 조회하고 오른쪽 테이블에만 있는 것을 포함해서 조회 |
      | FULL OUTER JOIN  | LEFT OUTER JOIN 과 RIGHT OUTER JOIN을 모두 실행     |
      
      
  
  + LEFT OUTER JOIN
    
    + 동일한 값이 없는 오른쪽 행은 NULL로 표시.
    
    + ON 조건절의 오른쪽 컬럼명 뒤에 (+)를 붙이면 LEFT OUTER 생략 가능.
      
      ```sql
      SELECT *
      FROM 테이블1 LEFT OUTER JOIN 테이블2
      ON 조건절;
      
      
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
  
  + 
  
  + 
