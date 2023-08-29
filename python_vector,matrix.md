## 벡터와 행렬
+ 벡터 : 표현할 때 리스트와 비슷
+ 행렬 : m개의 행과 n개의 열로 구성. 1개 이상의 벡터 모임이라고 생각.


## 파이썬으로 표현한 벡터
```python
vector_a = [1, 2, 10]       #리스트로 표현
vector_b = (1, 2, 10)       #튜플로 표현
vector_c = {'x': 1, 'y': 1, 'z': 10}        #딕셔너리로 표현
```
+ **벡터의 연산**
  + 기본적인 연산 : 같은 위치에 있는 값끼리 연산. (각 벡터의 크기가 같아야 함)
  ```python
  #리스트 컴프리헨션과 zip() 사용

  u = [2, 2]
  v = [2, 3]
  z = [3, 5]

  result = [sum(t) for t in zip(u,v,z)]
  print(result)     #결과 : [7, 10]
  ```
+ **별표 활용**
  ```python
  def vector_addition(*args):
    return [sum(t) for t in zip(*args)]

  vector_addition(u, v, z)


  #더 좋은 방법 (이차원 리스트 사용)
  row_vectors = [[2, 2], [2, 3], [3, 5]]
  vector_addition(*row_vectors)  
  ```
+ **스칼라-벡터 연산**
  ```python
  u = [1, 2, 3]
  v = [4, 4, 4]
  alpha = 2     #스칼라값

  result = [alpha * sum(t) for t in zip(u, v)]
  print(result)     #결과 : [10, 12, 14]
  ```  


## 파이썬으로 표현한 행렬
```python
matrix_a = [[3, 6], [4, 5]]     #리스트로 표현
matrix_b = [(3, 6), (4, 5)]     #튜플로 표현
matrix_c = {(0, 0): 3, (0, 1): 6, (1, 0): 4, (1, 1): 5}     #딕셔너리로 표현
``` 
+ **행렬의 연산**
  + 덧셈과 뺄셈 : 2개 이상의 행렬을 연산하기 위해서는 각 행렬의 크기는 같아야 함.
  ```python
  matrix_a = [[3,6],[4,5]]
  matrix_b = [[5,8], [6,7]]
  result = [[sum(row) for row in zip(*t)] for t in zip(matrix_a, matrix_b)]

  print(result) #결과 : [[8, 14], [10, 12]]
  ```
  + 행렬의 동치
    + 2개의 행렬이 서로 같은지를 나타내는 표현
    ```python
    matrix_a = [[1, 1], [1, 1]]
    matrix_b = [[1, 1], [1, 1]]

    all([row[0] == value for t in zip(matrix_a, matrix_b) for row in zip(*t) for value in row])     #결과 : True
    ``` 
    ```python
    #all() 함수와 any() 함수

    any([False, False, False])      #결과 : False
    any([False, True, False])       #결과 : True 
    #any()는 안에 있는 값 중 하나만 true면 true

    all([False, True, True])        #결과 : False
    all([True, True, True])         #결과 : True
    #all()은 안에 있는 값이 모두 true여야 true
    ```
  + 전치행렬
    + 주어진 m X n행렬에서 행과 열을 바꾸어 만든 행렬
    ```python
    matrix_a = [[1,2,3], [4,5,6]]
    result = [[element for element in t] for t in zip(*matrix_a)]
    print(result)       #결과 : [[1, 4], [2, 5], [3, 6]]
    ```   
  + 행렬의 곱셈
    + 앞 행렬의 크기가 m X n 이면 뒤 행렬은 n X m이어야 함
     ```python
     matrix_a = [[1, 1, 2], [2, 1, 1]]
     matrix_b = [[1, 1], [2, 1], [1, 3]]
     result = [[sum(a * b for a, b in zip(row_a, column_b)) for column_b in zip(*matrix_b)] for row_a in matrix_a]

     print(result)      #결과 : [[5, 8], [5, 6]]
     ``` 
     + `for row_a in matrix_a`   =>행의 값
     + `for column_b in zip(*matrix_b)`     =>열의 값 