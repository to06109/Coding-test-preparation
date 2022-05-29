# BOJ 1260 BFS와 DFS
# 2764ms
# 33452KB
'''
반례 해결
1000 1 1
99 1000
-> 답: 1, 1
-> 내 답: 1 99 1000, 1 99 1000
어떠한 간선도 존재하지 않는 노드가 존재하지 않을 경우
'''
import sys
from collections import deque
input = sys.stdin.readline
N, M, V = map(int, input().split())

graph = []
for i in range(M):
    temp = list(map(int, input().split()))
    graph.append(temp)

# 한 노드에 여러 노드가 있을 때, 숫자가 작은 노드 먼저 탐색해야함 ->  정렬
graph.sort(key=lambda x:(min(x), max(x)))

# DFS
visited_dfs = [True] + [False] * (N)
result_dfs = []

def DFS(graph, v): 
    
    global visited_dfs
    
    # 현재노드 방문처리
    visited_dfs[v] = True
    # 현재 노드 저장
    result_dfs.append(v)
    
    # 양방향 간선 고려
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
BFS(graph, V)
       
print(*result_dfs)
print(*result_bfs) 
        
# 반례 참고 https://www.acmicpc.net/board/view/24356