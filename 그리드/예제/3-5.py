#1이 될 때까지

n, k = map(int, input().split())

cnt = 0

while True: # 반복
    if (n==1): # 우리가 원하는 답이 나오면 반복문 탈출
        break
    elif (n % k) == 0:
        n //= k
        cnt += 1
    else:
        n -= 1
        cnt += 1

print(cnt)
