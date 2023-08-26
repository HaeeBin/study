korean_score = [49, 80, 20, 100, 80]
math_score = [43, 60, 85, 30, 90]
english_score = [49, 82, 48, 50, 100]

score = [korean_score, math_score, english_score]

result = []
for i in range(5) :
    sum = 0
    for j in range(3) :
        sum = sum + score[j][i]
    result.append(sum / 3)

print(result)