# 6-3 삽입 정렬

array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)): # 첫번째 인덱스는 정렬되어 있다고 생각
    for j in range(i,0,-1): # 인덱스 i부터 1까지 감소하며 반복하는 문법
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)

