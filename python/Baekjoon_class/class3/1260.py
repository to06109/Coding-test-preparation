# BOJ 1260 BFS와 DFS
# 0527_prepare
import sys
from collections import deque
input = sys.stdin.readline
N, M, V = map(int, input().split())

graph = []
for i in range(M):
    graph.append(list(map(int, input().split())))

graph.sort()
# print(graph)

visited_dfs = [False] * (N + 1)
result_dfs = [V]
def DFS(cur, next): # 노드 위치, 현재 노드
    global result_dfs

    # 현재노드 방문처리
    visited_dfs[cur] = True
    
    # 다음 노드 탐색
    result_dfs.append(next)
    
    for i in range(M):
        if graph[i][0] == next and visited_dfs[next] != True:
            DFS(next, graph[i][1])

visited_bfs = [False] * (N + 1)
result_bfs = []
def BFS(cur):
    global graph
    queue = deque([cur])
    # 현재 노드를 방문처리
    visited_bfs[cur] = True  
    
    while queue:
        # 큐에서 원소 하나를 뽑아 저장
        v = queue.popleft()
        result_bfs.append(v)
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입 + 방문처리
        for i in range(M):
            if graph[i][0] == cur and visited_bfs(graph[i][1]) != True:
                queue.append(graph[i][1])
    
for i in range(M):
    if graph[i][0] == V:
        DFS(V, graph[i][1])
        
BFS(V)
       
print(result_dfs)
print(result_bfs)
    
        