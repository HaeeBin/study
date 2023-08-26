import random

num = random.randint(1, 100)

print("숫자를 맞혀 보세요. (1 ~ 100)")
n = int(input())

while n != num :
    if n < num :
        print("숫자가 너무 작습니다.")
        n = int(input())
    else :
        print("숫자가 너무 큽니다.")
        n = int(input())

print("정답입니다. 입력한 숫자는 ", num, "입니다.")