N, M, K = map(int, input().split()) # M은 최종적으로 더할 수 있는 가지 수/ K는 연속해서 더할 수 있는 수
data = list(map(int, input().split()))

data.sort() #데이터를 정렬하기

first = data[N-1]
second = data[N-2]

result = 0

while True:
    for i in range(K): #가장 큰 수를 K번 더하기
        if M == 0: #M이 0이라면 while문 탈출
             break
        result += first
        M -= 1
    if M == 0: #M이 0이라면 while문 탈출
        break
    result += second
    M -= 1

print(result)