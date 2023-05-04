# DFS 예제

# DFS 메서드 정의

def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문한 정보를 리스트 자료형으로 표현 (1차원 리스트)
visited = [False] * 9

dfs(graph, 1, visited)