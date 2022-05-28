# BOJ 1260 BFS와 DFS
# 0528_prepare
# 11% 에서 틀렸습니다
'''
반례
6 8 1
[[1, 6], [6, 2], [2, 4], [4, 3], [3, 5], [5, 1], [5, 6], [2, 3]]
-> 답: 1 5 3 2 4 6, 1 5 6 3 2 4
-> 내 답: 1 6 5 3 2 4, 1 6 5 2 3 4
'''
import sys
from collections import deque
input = sys.stdin.readline
N, M, V = map(int, input().split())

graph = []
for i in range(M):
    temp = list(map(int, input().split()))
    # if temp[0] > temp[1]:
    #     graph.append(temp[::-1])
    # else:
    graph.append(temp)

graph.sort()

# DFS
visited_dfs = [True] + [False] * (N)
result_dfs = []

def DFS(graph, v): 
    global visited_dfs
    
    # 현재노드 방문처리
    visited_dfs[v] = True
    # 현재 노드 저장
    result_dfs.append(v)
    for i in range(M):
        if graph[i][0] == v and visited_dfs[graph[i][1]] == False:
            DFS(graph, graph[i][1])
        elif graph[i][1] == v and visited_dfs[graph[i][0]] == False:
            DFS(graph, graph[i][0])
                
# BFS
visited_bfs = [True] + [False] * (N)
result_bfs = []
def BFS(graph, v):
    
    global visited_bfs
    
    queue = deque([v])
    # 현재 노드를 방문처리
    visited_bfs[v] = True  
    
    while queue:
        # 큐에서 원소 하나를 뽑아 저장
        v = queue.popleft()
        result_bfs.append(v)
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입 + 방문처리
        for i in range(M):
            if graph[i][0] == v and visited_bfs[graph[i][1]] == False:
                queue.append(graph[i][1])
                visited_bfs[graph[i][1]] = True 
            elif graph[i][1] == v and visited_bfs[graph[i][0]] == False:
                queue.append(graph[i][0])
                visited_bfs[graph[i][0]] = True 

DFS(graph, V)
for i in range(M):
    if visited_dfs[graph[i][0]] == False:
        DFS(graph, graph[i][0])

BFS(graph, V)
for i in range(M):
    if visited_bfs[graph[i][0]] == False:
        BFS(graph, graph[i][0])
       
print(*result_dfs)
print(*result_bfs)
    
        