# BOJ 2606 바이러스
# DFS로 풀면되겠다!
# 68ms
# 30840KB

import sys
input = sys.stdin.readline

computer = int(input())
node = int(input())
# 그래프 만들기
graph = [[] for _ in range(computer + 1)]
for i in range(node):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    
visited = [False] * (computer + 1)
count = 0
def DFS(r):
    global count
    # 방문처리
    visited[r] = True
    count += 1
    # 현재 노드와 연결된 다른 노드 탐색
    for i in graph[r]:
        if not visited[i]:
            DFS(i)

DFS(1) # 1번 컴퓨터가 웜바이러스에 걸림
print(count - 1)