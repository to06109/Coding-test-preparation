# BOJ 7569 토마토
# 3296ms
# 50856KB

import sys
from collections import deque
input = sys.stdin.readline
M, N, H = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]    

# 상하좌우앞뒤
dx = [0, 0, -1, 1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]
dz = [-1, 1, 0, 0, 0, 0]

# 초기 익은 토마토 queue에 집어넣기
# 좌표를 넣을 것이므로 []넣기 / pop(0)의 시간복잡도는 O(n), popleft()의 시간복잡도는 O(1)
queue = deque([])
for h in range(H):
    for n in range(N):
        for m in range(M):
            if graph[h][n][m] == 1:
                queue.append([m, n, h]) # x, y, z

# BFS
def BFS():
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            next_x = x + dx[i]
            next_y = y + dy[i]
            next_z = z + dz[i]
            # 다음 노드가 범위를 벗어나지 않고 익지 않은 토마토가 들어있을 때
            if 0<=next_x<M and 0<=next_y<N and 0<=next_z<H:
                if graph[next_z][next_y][next_x] == 0:
                    graph[next_z][next_y][next_x] = graph[z][y][x] + 1
                    queue.append([next_x, next_y, next_z])

BFS()
result = 0
# 토마토가 모두 익지 못하는 상황
for h in graph:
    for n in h:
        for m in n:
            if m == 0:
                print(-1)
                exit(0)
        # 토마토를 모두 익힌 상황 -> 최소일수 구하기
        result = max(result, max(n))

print(result - 1)