# BOJ 24479 알고리즘 수업 - 깊이 우선 탐색 1
# 700ms
# 156956KB
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N, M, R = map(int, input().split())
result = [0] * (N + 1)
# 그래프 만들기
graph = [[] for _ in range(N + 1)]
for i in range(M):
    u, v = map(int, input().split())
    # 양방향 간선
    graph[u].append(v)
    graph[v].append(u)

# 인접정점 오름차순 방문
for j in range(N + 1):
    graph[j].sort()

visited = [False] * (N + 1)
count = 1
def DFS(r):
    global count
    # 방문처리
    visited[r] = True
    result[r] = count
    # 현재 노드와 연결되어있는 노드 순차탐색
    for i in graph[r]:
        if visited[i] == False:
            count += 1
            DFS(i)

DFS(R) 

for i in range(1, N + 1):
    print(result[i])