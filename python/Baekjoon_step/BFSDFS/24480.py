# BOJ 24480 알고리즘 수업 - 깊이 우선 탐색 2
# 인접 정점 내림차순
# 712ms
# 156952KB

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for j in graph:
    j.sort(reverse=True) # 내림차순 정렬

visited = [False] * (N + 1)
result = [0] * (N + 1)
count = 1

def DFS2(r):

    global count

    # 방문처리
    visited[r] = True
    result[r] = count

    # 현재 노드와 인접한 노드 탐색
    for i in graph[r]:
        if visited[i] == False:
            count += 1
            DFS2(i)

DFS2(R)
for m in range(1, N + 1):
    print(result[m])