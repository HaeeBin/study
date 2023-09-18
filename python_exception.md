## 예외 처리 구문
+ **try-except문**
   ```python
   try:
    예외 발생 가능 코드
   except 예외 타입:
    예외 발생 시 실행되는 코드 
   ```
   + ZeroDivisionError : 어떤 숫자를 0으로 나누었을 때 발생하는 에러
      ```python
      for i in range(10):   
        #try문이 for문 밖에 있으면 안됨.(에러 발생 시 except문 실행 후 try문이 종료되기 때문)
        try:
            print(10 / i)
        except ZeroDivisionError:
            print("Not divided by 0")
      ```
   + IndexError : 리스트의 인덱스 범위를 넘어갈 때
   + NameError : 존재하지 않는 변수를 호출할 때
   + ValueError : 변환할 수 없는 문자나 숫자를 변환할 때
   +  