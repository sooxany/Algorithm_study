# 행마다 작은 수 중 제일 큰 수 찾기

n, m = map(int, input().split())

res = 0

for i in range(n):
    data = list(map(int, input().split()))

    min_value = min(data)

    res = max(res, min_value)

print(res)



