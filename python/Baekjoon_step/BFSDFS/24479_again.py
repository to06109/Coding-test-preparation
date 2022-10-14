# BOJ 24479 알고리즘 수업 - 깊이 우선 탐색 1
# 159784KB
# 684ms

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N, M, R = map(int, input().split())
result = [0 for _ in range(N + 1)]
graph = [[] for _ in range(N + 1)]
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
for item in graph:
    item.sort()

visited = [False for _ in range(N + 1)]  

temp = 0
def dfs(visited, r):
    
    global temp
    
    # 방문처리
    temp += 1
    result[r] = temp
    visited[r] = True
    
    for i in graph[r]:
        if not visited[i]:
            dfs(visited, i)

dfs(visited, R)
for s in result[1:]:
    print(s)