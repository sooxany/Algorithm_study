# 이진탐색 알고리즘
def binary_search(array, target, start, end):
    while start  <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

N = int(input())
array = list(map(int, input().split()))
array.sort()
M = int(input())
target = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인
for i in target:
    result = binary_search(array, i, 0, N-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')





