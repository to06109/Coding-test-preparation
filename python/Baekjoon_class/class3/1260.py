# BOJ 1260 BFS와 DFS
# 0528_prepare
# 88% 에서 틀렸습니다
'''
반례
5 1 1
5 4
-> 답: 1 5 4
-> 내 답: 1 4 5
위에서 작은수로 정렬하기 위해 입력값의 순서를 바꾼데에서 오류가 난 듯함
'''

import sys
from collections import deque
input = sys.stdin.readline
N, M, V = map(int, input().split())

graph = []
for i in range(M):
    temp = list(map(int, input().split()))
    if temp[0] > temp[1]:
        graph.append(temp[::-1])
    else:
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
    
        
        
# https://www.acmicpc.net/board/view/24356