## 문자열의 분리 및 결합
+ 문자열의 분리 : split() 함수<br>
  `'zero one two three'.split() //공백 기준으로 문자열 분리`<br>
  `'python,java,c,html'.split(",") //","를 기준으로 문자열 분리`

+ 문자열의 결합 : join() 함수
  ```python
  colors = ['red','blue','green','yellow']
  result = ''.join(colors)
  print(result) # 결과 : 'redbluegreenyellow'

  result2 = '-'.join(colors)
  print(result2) #결과 : 'red-blue-green-yellow'
  ```  


## 리스트 컴프리헨션
+ 리스트 컴프리헨션 : 기존 리스트형을 사용하여 새로운 리스트를 만드는 기법
  ```python
  result = [i for i in range(10)]
  print(result) # 결과 : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  ```

+ 리스트 컴프리헨션 용법
  + **필터링 (if와 함께 사용하는 용법)**
   ```python
   result = [i for i in range(10) if % 2 == 0]
   print(result) #결과 : [0, 2, 4, 6]
   ```
   ```python
   #else문과 사용하는 방법

   result = [i if i % 2 == 0 else 10 for i in range(10)]
   print(result) # 결과 : [0, 10, 2, 10, 4, 10, 6, 10, 8, 10]
   ```
  + **중첩 반복문**
  ```python
  word_1 = "Hello"
  word_2 = "World"
  result = [i + j for i in word_1 for j in word_2]
  print(result) #결과 : ['HW','Ho','Hl','Hr', ...]
  ```  
  ```python
  #중첩 반복문과 필터링 

  case_1 = ["A","B","C"]
  case_2 = ["D","E","A"]
  result = [i + j for i in case_1 for j in case_2 if not(i == j)]
  print(result) #결과 : ['AD','AE','BE','BA', ...] 
  ```
  + **이차원 리스트**
  ```python
  #대괄호 2개 사용하는 방법(가장 간단한 방법)

  words = 'The quick brown fox jumps over the lazy dogs'.split()
  stuff = [[w.upper(), w.lower(), len(w)] for w in words]
  print(stuff) #결과 : ['THE','the',3],['QUICK','quick',5] ...
  ``` 
  ```python
  #for문 2개 사용하는 방법

  case_1 = ["A","B","C"]
  case_2 = ["D","E","A"]
  result = [[i + j for i in case_1] for j in case_2]
  print(result) #결과 : [['AD','BD','CD'],['AE','BE','CE'],['AA','BA','CA']]

  #case_2가 고정되고 A,B,C가 차례로 붙음.(=뒤의 for문이 먼저 실행된다고 볼 수 있음)
  # for j in case_2:
  #     for i in case_1:
  # 위 코드와 같음. 
  ```


## 다양한 방식의 리스트값 출력
+ 리스트 값에 인덱스를 붙여 출력 : enumerate() 함수
  ```python
  {i:j for i, j in enumerate('TEAMLAB is an academic institute located in South Korea'.split())}
  #결과 : {0:'TEAMLAB',1:'is',2:'an',3:'academic' ....}
  ```

+ 리스트값을 병렬로 묶어 출력 : zip() 함수
  ```python
  alist = ['a1','a2','a3']
  blist = ['b1','b2','b3']
  for a,b in zip(alist, blist):
    print(a,b) #결과 : a1 b1 <br> a2 b2 <br> a3 b3
  ```
  ```python
  a, b, c = zip((1,2,3), (10,20,30), (100,200,300))
  print(a, b, c) #결과 : (1, 10, 100) (2, 20, 200) (3, 30, 300)

  [sum(x) for x in zip((1,2,3),(10,20,30),(100,200,300))]
  #결과 : [111,222,333]
  ```


## 람다 함수
+ 람다 함수 : 함수의 이름 없이, 함수처럼 사용할 수 있는 익명의 함수
  ```python
  #일반적인 함수

  def f(x,y):
    return x + y

  print(f(1, 4))


  #람다 함수
  
  f = lambda x, y: x + y
  print(f(1,4))
   ```


## 맵리듀스
+ **map() 함수**
  + 일반적으로 리스트나 튜플처럼 요소가 있는 시퀀스 자료형에 사용됨.
  ```python
  ex = [1, 2, 3, 4, 5]
  f = lambda x: x ** 2

  print(list(map(f, ex))) #결과 : [1, 4, 9, 16, 25]
  ```
  + map(함수 이름, 리스트 데이터) 구조.
  + 최근에는 람다 함수나 map()함수를 개발에 사용하는 것을 권장하지 않음. 리스트 컴프리헨션 기법으로도 같은 효과를 낼 수 있기 때문.
  ```python
  #위 코드를 리스트 컴프리헨션으로 구현

  ex = [1, 2, 3, 4, 5]
  [x ** 2 for in ex]
  ```
  + 한 개 이상의 시퀀스 자료형 데이터의 처리
  ```python
  ex = [1, 2, 3, 4, 5]
  f = lambda x, y: x + y
  print(list(map(f, ex, ex))) #결과 : [2, 4, 6, 8, 10]

  #리스트 컴프리헨션으로 구현(zip함수 사용)
  [x + y for in zip(ex,ex)]
  ```
  + 필터링 기능(else문을 반드시 작성해야 함)
  ```python
  list(map(lambda x: x ** 2 if x % 2 == 0 else x, ex))
  #결과 : [1, 4, 3, 16, 5]

  #리스트 컴프리헨션으로 구현
  [x ** 2 if x % 2 == 0 else x for x in ex]
  ```

+ **reduce() 함수**
  + 리스트와 같은 시퀀스 자료형에 차례로 함수 적용하여 모든 값을 통합하는 함수
  ```python
  from functools import reduce
  print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])) #결과 : 15
  ```  
  + reduce()함수는 리스트 변수의 모든 값을 람다 함수로 모두 적용해야 함.