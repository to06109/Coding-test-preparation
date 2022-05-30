# BOJ 24444 알고리즘 수업 - 너비 우선 탐색 1
# 인접 정점 오름차순 방문
# 608ms
# 66608KB
# list로 했을 때보다 deque로 구현했을 때 약 1400ms정도 더 빠르다.
# deque가 list에 비해 데이터를 넣고 빼는 속도가 효율적이다.

from collections import deque
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
def BFS(r):
    count = 1
    queue = deque([r])
    # 방문처리
    visited[r] = True
    result[r] = count

    # 인접한 노드 탐색
    while queue:
        node = queue.popleft()
        for i in graph[node]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                count += 1
                result[i] = count

BFS(R)
print('\n'.join(map(str, result[1:])))