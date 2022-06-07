# BOJ 2178 미로 탐색
# BFS로 현재 노드에서 상하좌우에 있는 노드에 거리 1씩 더하기
# 104ms
# 32476KB

import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [input().rstrip() for _ in range(N)]

# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

result = []
visited = [[False] * M for _ in range(N)]

def BFS(x, y, dis): # 현재 위치(열, 행), 거리
    queue = deque()
    queue.append([x, y])
    # 방문처리
    visited[y][x] = dis + 1
    
    while queue:
        node = queue.popleft()
        # 상하좌우에 있는지 확인
        for i in range(4):
            next_x = node[0] + dx[i]
            next_y = node[1] + dy[i]
            if 0 <= next_x < M and 0 <= next_y < N:
                if not visited[next_y][next_x] and graph[next_y][next_x] == "1":
                    # 방문처리2
                    queue.append([next_x, next_y])
                    visited[next_y][next_x] = visited[node[1]][node[0]] + 1
                          
distance = 0
BFS(0, 0, distance)
print(visited[N-1][M-1])