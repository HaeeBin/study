print("당신이 태어난 연도를 입력하세요.")
year = int(input())

student = 2020 - year + 1

if student <= 26 and student >= 20 :
    print("대학생")
elif student < 20 and student >= 17 :
    print("고등학생")
elif student < 17 and student >= 14 :
    print("중학생")
elif student < 14 and student >= 8 :
    print("초등학생")
else :
    print("학생이 아닙니다.")