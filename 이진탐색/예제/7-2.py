# 재귀 함수로 구현한 이진 탐색 소스코드
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end) // 2 # 이진 탐색의 중간 위치는 내림 처리한다
    if array[mid] == target:
        return mid
    # 중간점의 값보다 target이 더 작을 경우
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    # 중간점의 값보다 target이 클 경우
    else:
        return binary_search(array, target, mid+1, end)

n, target = list(map(int, input().split()))

array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다")
else:
    print(result+1)
