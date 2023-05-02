# 배열 0부터 검사해보기
# 첫번째 수를 기준으로 생각하기
# 첫번째가 1이면 0인 것을 찾아 1로 바꾸기

# --> n[0]의 값과 n[len(n)-1]의 값이 같다면
#     해당하는 수의 개수(연속적인 것은 하나 취급) - 1
# --> n[0]의 값과 n[len(n)-1]의 값이 다르면
#     해당하는 수의 개수(연속적인 것은 하나 취급)

n = input()

a = n[0]

cnt = 0
res = 0

if n[0] == n[len(n)-1]:
    for i in range(len(n)-2):
        if n[i] != n[i+1] and n[i+1] != n[i+2]:
            cnt += 1
    res = cnt-1
else:
    for i in range(len(n)-2):
        if n[i] != n[i+1] and n[i+1] != n[i+2]:
            cnt +=1
    res = cnt

print(cnt)






