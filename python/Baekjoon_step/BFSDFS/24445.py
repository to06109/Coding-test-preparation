# BOJ 24445 알고리즘 수업 - 너비 우선 탐색 2
# 인접 정점 내림차순 방문
# 664ms
# 66608KB

import sys
from collections import deque
input = sys.stdin.readline
N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for j in graph:
    j.sort(reverse=True)

visited = [False] * (N + 1)
result = [0] * (N + 1)
def BFS2(r):
    count = 1
    # 방문 처리
    queue = deque([r])
    queue.append(r)
    visited[r] = True
    result[r] = count
    # 현재 노드 인접 노드 탐색
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                count += 1
                result[i] = count

BFS2(R)
print('\n'.join(map(str, result[1:])))