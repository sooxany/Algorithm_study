# 두 배열의 원소 교체
# a의 가장 큰 수와 b의 가장 작은 수 교체
N, K = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

res = 0

a.sort() #오름차순 (작은 수부터 정렬)
b.sort(reverse=True) #내림차순 (큰 수부터 정렬)

for i in range(K):
    if a[i] < b[i]:
        a[i] = b[i]

for i in range(N):
    res += a[i]

print(res)



