# BOJ 7576 토마토
# 풀이 중. 처음에 1이 여러 개 있을 때 동시에 BFS 시작하는 것을 구현하지 못함
import sys
from collections import deque
input = sys.stdin.readline
M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

visited = [[False] * M for _ in range(N)]

count = 0
def BFS(x, y):
    
    global count
    
    queue = deque()
    queue.append([x, y])
    # 방문처리
    visited[y][x] = True
    
    while queue:
        node = queue.popleft()
        for i in range(4):
            next_x = node[0] + dx[i]
            next_y = node[1] + dy[i]
            if 0 <= next_x < M and 0 <= next_y < N:
                if graph[next_y][next_x] == 0 and visited[next_y][next_x] == False:
                    queue.append([next_x, next_y])
                    graph[next_y][next_x] = graph[node[1]][node[0]] + 1
                    visited[next_y][next_x] = True
        count += 1
    print(node)

for i in range(N):
    for j in range(M):
        if graph[i][j] == 1 and not visited[i][j]:
            BFS(j, i)

# BFS 다 끝났는데 0이 있으면 -1 출력
for m in graph:
    for n in m:
        if n == 0:
            print(-1)
            break

print(graph)