# BOJ 24444 알고리즘 수업 - 너비 우선 탐색 1
# 인접 정점 오름차순 방문
# 2208ms
# 58788KB
import sys
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for j in graph:
    j.sort()

result = [0] * (N + 1)
visited = [False] * (N + 1)
queue = []
count = 1
def DFS(r):
    global count

    # 방문처리
    visited[r] = True
    queue.append(r)
    result[r] = count

    # 인접한 노드 탐색
    while queue:
        node = queue.pop(0)
        for i in graph[node]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
                count += 1
                result[i] = count

DFS(R)
for i in range(1, N+1):
    print(result[i])
