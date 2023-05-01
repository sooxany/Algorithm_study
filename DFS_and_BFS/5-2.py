#5-2 큐 예제

from collections import deque

#큐(Queue) 구현을 하기 위해서는 deque 라이브러리 사용

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() # 다음 출력을 위해 순서 바꾸기
print(queue)