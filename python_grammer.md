## 자료형 변환
+ 실수형으로 변환 : float(문자형/정수형 ...)
+ 정수형으로 변환 : int(실수형/문자형 ...)
+ 문자형으로 변환 : str(정수형/실수형 ...)


## 화면 입출력
+ 표준 입력 함수 : input() 
  + input으로 받은 변수는 문자열임!!
+ 표준 출력 함수 : print()


## 리스트
+ 리스트의 길이 : len(리스트 이름)
+ 슬라이싱 : 변수명[시작 인덱스 : 마지막 인덱스] 
  + 출력은 '마지막 인덱스 -1'까지
+ 증가값 : 변수명[시작 인덱스 : 마지막 인덱스 : 증가값]
  + 변수명[::-1] : 역으로 출력
+ in 연산 : 포함 여부를 확인하는 연산.<br>
  `'blue in color2 //color2변수에서 문자열 'blue'의 존재 여부`
+ 리스트의 추가 및 삭제 
  + append() : 리스트의 맨 끝 인덱스에 추가.
  + extend() : 기존 리스트에 새로운 리스트를 합치는 기능<br>`color.extend(['black', 'purple']) //color라는 리스트에 추가`
  + insert() : 리스트의 특정 위치에 값 추가.<br>`color.insert(0, 'orange') // color라는 리스트의 0번째 인덱스에 orange 추가.`
  + remove() : 리스트에 있는 특정값 삭제<br>`color.remove('red') //red라는 값 삭제`
  + del : 특정 인덱스 값 삭제<br>`del color[0] //0번째 인덱스 값 삭제`


## 함수의 인수
+ 키워드 인수 : 함수에 입력되는 매개변수의 변수명을 사용하는 방법
  ```python
  def print_something(my_name, your_name):
    print("Hello {0}.My name is {1}".format(your_name, my_name))

  print_something("Kim", "Lee")
  print_something(your_name = "Lee", my_name = "Kim")  
  ```

+ 디폴트 인수 : 매개변수에 기본값을 지정하여 사용하고, 아무런 값도 인수로 넘기지 않으면 지정된 기본값을 사용하는 방식.
  ```python
  def print_something(my_name, your_name = "Lee"):
    print("Hello {0}.My name is {1}".format(your_name, my_name))

  print_something("Kim", "Lee")
  print_something("Kim") //매개변수를 하나만 입력된 경우 기본값이 없는 첫번째 값에 할당됨.  
  ```

+ 가변 인수(튜플형으로 저장)
  ```python
  def sum_num(a, b, *args):
    print(args) //결과 : (3, 4, 5)
    return a + b + sum(args)
    
  print(sum_num(1, 2, 3, 4, 5))
  ```
  
+ 키워드 가변 인수(딕셔너리형으로 저장)
  ```python
  def function1(**args):
    print(args) //결과 : {'first' : 1, 'second' : 2, 'third' : 3}
    print("First is {first}".format(**args)) //결과 : First is 1
    print("Second is {second}".format(**args)) //결과 : Second is 2
    
  function1(first = 1, second = 2, third = 3)
  ```

## 문자열
+ len() : 문자열의 문자 개수 반환 <br>`a = len("abc") //a의 값은 3`
+ upper() : 대문자로 변환 <br>`문자열변수.upper()`
+ lower() : 소문자로 변환<br>`문자열변수.lower()`
+ title() : 각 단어의 앞글자만 대문자로 변환.<br>`문자열변수.title()`
+ capitalize() : 첫 글자만 대문자로 변환<br>`문자열변수.capitalize()`
+ count("찾을 문자열") : '찾을 문자열'이 몇 개 있는지 개수 반환
+ find("찾을 문자열") : '찾을 문자열'이 왼쪽에서 몇 번째에 있는지 반환
+ rfind("찾을 문자열") : '찾을 문자열'이 오른쪽에서 몇 번째에 있는지 반환
+ startswith("문자열") : '문자열'로 시작하는지 여부 반환
+ endswith("문자열") : '문자열'로 끝나는지 여부 반환
+ strip() : 좌우 공백 삭제
+ rstrip() : 오른쪽 공백 삭제
+ lstrip() : 왼쪽 공백 삭제
+ split() : 문자열을 공백이나 다른 문자로 나누어 리스트로 반환
+ isdigit() : 문자열이 숫자인지 여부 반환
+ islower() : 문자열이 소문자인지 여부 반환
+ isupper() : 문자열이 대문자인지 여부 반환


## 문자열 서식 지정
+ %서식과 format()함수
  ```python
  print(1, 2, 3)
  print("a" + "" + "b" + "" + "c")

  print("%d %d %d" % (1, 2, 3))
  print('%s %s' % ('one', 'two'))

  print("{} {} {}".format("a", "b", "c"))
  print("I'm {0} years old.".format(20))
  print("Product: {0}, Price per unit: {1:.2f}.".format("Apple", 5.243)) 
  //.2f : 소수점 둘째자리까지 출력.
  ```

+ 변수의 자료형에 따른 서식
  + %s : 문자열
  + %c : 문자 1개
  + %d : 정수
  + %f : 실수
  + %o : 8진수
  + %x : 16진수
  + %% : 문자 % 자체


+ 패딩
  + %서식 패딩<br>`print("%10d" % 30) //결과 :(8칸 공백)30` <br>`print("%-10d" %  30) //결과 : 30(8칸 공백)`<br><br>`print("%10.3f" % 1.23456) //결과 : (6칸 공백)1.234`
  
  + format()함수 패딩<br>`print("{0>10s}".format("Apple")) //결과 : (5칸공백)Apple`<br>`print("{0:<10s}".format("Apple")) // 결과 : Apple(5칸 공백)`<br><br>`print("{1:10.5f}".format("Apple", 1.234)) // 결과 : 1.23400`

+ 네이밍<br>
  `print("Product: %(name)5s, Price per unit: %(price)5.5f." % {"name" : "Apple", "price" : 1.234})`<br>`print("Product: {name:>5s}, Price per unit: {price:5.5f}.".format(name="Apple", price=1.234))`



## 자료구조
+ 스택(리스트에서 구현)
  ```python
  a = [1, 2, 3, 4, 5]
  a.append(10) //a = [1, 2, 3, 4, 5, 10]
  
  a.pop() //a = [1, 2, 3, 4, 5]
  ```

+ 큐(리스트에서 구현)
  ```python
  a = [1, 2, 3, 4, 5]
  a.append(10) //a = [1, 2, 3, 4, 5, 10]
  
  a.pop(0) // 1
  ```

+ 튜플(값을 변경하는 것이 불가능한 리스트)
  ```python
  t = (1, 2, 3) 
  print(t + t, t * 2) //결과 : (1, 2, 3, 1, 2, 3)(1, 2, 3, 1, 2, 3)
  len(t) //3
  
  t[1] = 5 //에러 발생
  
  //값이 하나만 있을 때 튜플 선언
  t = (1, )
  //t = (1)로 선언하면 t = 1 으로 받아들여짐.
  ```

+ 세트(순서 없이 저장하면서 중복을 허용하지 않음)
  ```python
  s = set([1, 2, 3, 1, 2, 3])
  print(s) // 결과 : {1, 2, 3}
  s.add(1) //1 추가하는 명령이지만 중복 불허로 추가되지 않음
  s.remove(1) //1 삭제 => s = {2, 3}
  s.update([1, 4, 5, 6, 7]) //새로운 리스트 추가 => s = {1, 2, 3, 4, 5, 6, 7}
  s.discard(3) //3 삭제 => s = {1, 2, 4, 5, 6, 7}
  s.clear() //모든 변수 삭제 => s = set()

  //집합 연산
  s1.union(s2) //합집합
  s1 | s2 //합집합

  s1.intersection(s2) //교집합
  s1 & s2 //교집합

  s1.difference(s2) //차집합
  s1 - s2 //차집합
  ```    

+ 딕셔너리
  ```python
  student_info = {20180111: 'Kim', 20180112: 'Lee', 20180113: 'Park'}
  student[20180111] // 결과 : 'Kim'
  student[20180112] = 'Han'

  student_info.keys() //결과 : dict_keys([20180111, 20180112, 20180113])
  student_info.values() // 결과 : dict_values(['Kim', 'Han', 'Park'])
  student_info.items() 
  // 결과 : dict_items([(20180111, 'Kim'), (20180112, 'Han'), (20180113: 'Park')])

  20180111 in student_info.keys() //결과 : True
  'Kim' in student_info.values() //결과 : True
  
  code = {} //딕셔너리 선언
  ```


## 자료구조2(collections 모듈)
+ **deque모듈(스택과 큐 모두 지원)**
  ```python
  from collections import deque

  deque_list = deque()
  for i in range(5):
    deque_list.append(i)

  print(deque_list) //결과 : deque([0, 1, 2, 3, 4])

  //스택
  deque_list.pop()

  //큐(pop(0)은 작동하지 않기 때문에 입력할 때 새로운 값을 왼쪽부터 입력되게 하여 출력.)
  deque_list2 = deque()
  for i in range(5):
    deque_list2.appendleft(i)

  print(deque_list2) //결과 : deque([4, 3, 2, 1, 0])
  deque_list2.pop()     
  ```  
  ```python
  //rotate() 함수
  from collections import deque

  deque_list = deque()
  for i in range(5):
    deque_list.append(i) //결과 : [0, 1, 2, 3, 4]

  deque_list.rotate(2) //결과 : [3, 4, 0, 1, 2]
  deque_list.rotate(2) //결과 : [1, 2, 3, 4, 0]  
  ```
  ```python
  //reversed() 함수 =>기존과 반대로 데이터 저장
  print(deque(reversed(deque_list))) //결과 : [0, 4, 3, 2, 1]

  //extend() 함수 =>리스트 추가
  deque_list.extend([5, 6, 7]) //결과 : [1, 2, 3, 4, 0, 5, 6, 7]

  //extendleft() 함수 =>왼쪽에 리스트 추가
  deque_list.extendleft([5, 6, 7]) //결과 : [7, 6, 5, 1, 2, 3, 4, 0, 5, 6, 7]
  ```



+ **OrderedDict 모듈(순서를 가진 딕셔너리 객체)**
  
  ```python
  from collections import OrderedDict

  d = OrderedDict()
  d['x'] = 100
  d['y'] = 200
  d['z'] = 300
  d['l'] = 400

  for k, v in d.items():
    print(k, v) //결과 : 입력한 순서대로 출력됨
  ```
  ```python
  //키나 값으로 정렬
  def sort_key(t):
    return t[0] 
    //값을 기준으로 정렬하고 싶을 때 : return t[1]

  from collections import OrderedDict

  d = dict()
  d['x'] = 100
  d['y'] = 200
  d['z'] = 300
  d['l'] = 400

  for k, v in OrderedDict(sorted(d.items(), key = sort_key)).items():
    print(k, v) //결과 : 키를 기준으로 오름차순으로 출력됨.
  ```

+ **defaultdict 모듈**
  ```python
  from collections import defaultdict

  d = defaultdict(lambda: 0)
  print(d["first"]) //결과 : 0
  ```
  ```python
  //리스트 형태로도 설정
  from collections import defaultdict

  s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
  d = defaultdict(list) // 초기 value를 리스트로 선언

  for k, v in s:
    d[k].append(v)

  print(d.items()) 
  //결과 : [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]  
  ```

+ **Counter 모듈(데이터 값의 개수를 딕셔너리 형태로 반환)**
  ```python
  from collections impiort Counter

  text = list("gallahad")

  c = Counter(text)
  print(c) //결과 : {'a':3, 'l':2, 'g':1, 'h':1, 'd':1}
  print(c["a"]) //결과 : 3
  ```  
  ```python
  //counter 객체 생성
  from collections import Counter

  c = Counter({'red':4, 'blue':2}) //딕셔너리 형태로 생성
  print(list(c.elements())) //결과 : ['red','red','red','red','blue','blue']

  c = Counter(cats=4, dogs=8) //키워드 형태의 매개변수 사용해서 생성
  ```

  ```python
  //사칙연산 지원
  c = Counter(a=4, b=2, c=0, d=-2)
  d = Counter(a=1, b=2, c=3, d=4)

  c.subtract(d) //c-d
  print(c) //결과 : {'a':3, 'b':0, 'c':-3, 'd':-6}
  print(c + d)

  c = Counter(a=4, b=2, c=0, d=-2)
  print(c & d) //결과 : {'a':1, 'b':2}
  print(c | d) //결과 : {'a':4, 'b':2, 'c':3, 'd':4}
  ```

+ **namedtuple 모듈**
  ```python
  from collections import namedtuple

  Point = namedtuple('Point', ['x', 'y']) //point객체의 이름은 point로 지정.
  p = Point(11, y=22)
  print(p.x, p.y) //결과 : 11 22
  print(p[0] + p[1]) //결과 : 33 (p[0]은 먼저 저장되어야하는 x값에 대응. p[1]은 y값.)
  ```  