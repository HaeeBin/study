## 내장 모듈
+ **random 모듈**
  + randint() : 정수 모듈 생성
  + random() : 임의의 난수 생성
     ```python
     import random

     print(random.randint(0, 100))  #0~100사이의 정수 난수 생성
     print(random.random())     #일반적인 난수 생성(정수, 실수 모두)
     ```

+ **time 모듈**
  + 시간을 변경하거나 현재 시각 출력.
     ```python
     import time

     print(time.localtime()) #현재 시각 출력
     #결과 : time.struct_time(tm_year=2018, tm_mon=8, tm_day=19, tm_hour=22, tm_min=9, tm_sec=21, tm_wday=6, tm_yday=231, tm_isdst=0)
     ```

+ **urllib 모듈**
  + 웹 주소의 정보를 불러옴.
  + request 모듈 : 특정 URL의 정보를 불러올 수 있음.
     ```python
     import urllib.request

     response = urllib.request.urlopen("http://theteamlab.io")  
     #해당 주소의 HTML정보를 가져옴
     print(response.read())
     ```