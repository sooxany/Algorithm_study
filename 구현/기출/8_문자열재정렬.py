inp = list(input())

# 문자 추출
res = 0
alpha = list(filter(str.isalpha, inp))
alpha.sort()

# 리스트형을 문자열로 변환해야함
# join 함수 이용
alpha = ''.join(alpha)

# 숫자 추출
num = list(filter(str.isdigit, inp))

for i in range(len(num)):
    res += int(num[i])

print(alpha+str(res))





