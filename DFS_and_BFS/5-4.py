#5-4 재귀 함수 종료 예제

def recursive_function(i):
    if i == 100:
        return
    print(i, '번째 재귀 함수에서', i+1, '번째 재귀 함수를 호출한다')
    recursive_function(i+1)
    print(i, '번째 재귀 함수를 종료한다')

recursive_function(1)

# 재귀함수는 스택 자료구조를 이용한다