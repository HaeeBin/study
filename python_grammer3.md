## 클래스 구현하기
+ `class 클래스이름(상속받는 객체명):`

+ 속성의 선언
  ```python
  class soccerPlayer(object):
    def__init__(self, name, position, back_number):
        self.name = name
        self.position = position
        self.back_number = back_number
  ```
  + `__init__()` 함수 : class에서 사용할 변수를 정의하는 함수.
    + 첫번째 매개변수는 반드시 self 변수를 사용해야 함.
    + self 뒤의 매개변수들은 실제로 클래스가 가진 속성.
+ 함수의 선언
    ```python
    class soccerPlayer(object):
        def change_number(self, new_number):
            print("등번호 변경: From %d to %d" %(self.back_number, new_number))
            self.back_number = new_number
    ```

+ 인스턴스 사용
  ```python
  class soccerPlayer(object):
    def __init__(self,name,position,back_number):
        self.name = name
        self.position = position
        self.back_number = back_number

    def change_number(self,new_number):
        print("등번호 변경: From %d to %d" %(self.back_number, new_number))
        self.back_number = new_number

    def __str__(self):
        return "Hello, my name is %s. I play in %s in center." %(self.name, self.position)    

  #인스턴스 사용  
  kim = soccerPlayer("kim", "MF", 10)

  print("현재 선수의 등번호: ", kim.back_number)    #결과 : 현재 선수의 등번호: 10
  kim.change_number(5)      #결과 : 등번호 변경: From 10 to 5
  print("현재 선수의 등번호: ", kim.back_number)    #결과 : 현재 선수의 등번호: 5

  print(kim)    #결과 : Hello, my name is kim. I play MF in center.
  ```

## 객체 지향 프로그래밍의 특징
+ 상속
  + 부모 클래스로부터 값과 메서드를 물려받아 자식 클래스를 생성하는 것.
  + **class 자식 클래스명(부모 클래스명)**
    ```python
    class Person(object):
        def __init__(self, name, age):
            self.name = name
            self.age = age
    
    class Korean(Person):
        pass

    korean = Korean("kim", 30)
    print(korean.name)      #결과 : kim
    ``` 
  + 일반적인 속성을 부모 클래스에, 상세 기능을 자식 클래스에 넣어야 함.
    ```python
    #부모 클래스
    class Person(object):
        def __init__(self, name, age, gender):
            self.name = name
            self.age = age
            self.gender = gender

        def about_me(self):
            print("저의 이름은", self.name, "이고, 제 나이는", str(self.age), "살입니다.")
    ``` 
    ```python
    #자식 클래스
    class Employee(Person):
        def __init__(self, name, age, gender, salary, hire_date):
            super().__init__(name, age, gender)     
            #부모 객체 사용(새로운 내용 추가하려면 작성해야 한다.)
            self.salary = salary
            self.hire_date = hire_date

        def do_work(self):
            print("열심히 일한다.")

        def about_me(self):
            super().about_me()  #새로운 내용 추가위해 작성.
            print("제 급여는", self.salary, "원이고, 제 입사일은", self.hire_date, "입니다.")
    ``` 
+ 다형성
  + 같은 이름의 메서드가 다른 기능을 할 수 있도록 하는 것.
    ```python
    class Animal:
        def __init__(self, name):
            self.name = name
        def talk(self):
            raise NotImplementedError("Subclass must implement abstract method")

    class Cat(Animal):
        def talk(self):
            return 'Meow!'

    class Dog(Animal):
        def talk(self):
            return 'Woof!Woof!'

    animals = [Cat('Missy'), Cat('Mr.Mistoffeless'), Dog('Lassie')]
    for animal in animals:
        print(animal.name + ": " + animal.talk())
    #결과 : Missy: Meow!
    #      Mr.Misoffeless: Meow!
    #      Lassie: Woof!Woof!
    ```
+ 가시성
  + 객체의 정보 접근을 숨기는 것
  + 캡슐화, 정보 은닉