x = 1
while x != 0 :
    print("구구단 몇 단을 계산할까요(1~9)?")
    x = int(input())

    if x == 0 :
        print("구구단 게임을 종료합니다.")
        break;

    print("구구단 ", x, "단을 계산합니다.")
    for i in range(1, 10) :
        print(x, " x ", i, " = ", x * i)
    