# 집합 자료형

N = int(input())
# 부품 번호를 입력받아서 집합(set) 자료형에 기록
array = set(map(int, input().split()))

M = int(input())
target = list(map(int, input().split()))

for i in target:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')
