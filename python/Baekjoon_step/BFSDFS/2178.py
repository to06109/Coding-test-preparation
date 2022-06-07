# BOJ 2178 미로 탐색
# DFS -> 최단거리 못찾음 
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
graph = [input().rstrip() for _ in range(N)]

# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

result = []
visited = [[False] * M for _ in range(N)]
def DFS(x, y, dis): # 현재 위치(열, 행), 거리
    
    # 방문처리
    visited[y][x] = dis
    
    # 리턴조건
    if x == M - 1 and y == N - 1:
        result.append(dis)
        return
    
    # 상하좌우에 있는지 확인
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if 0 <= next_x < M and 0 <= next_y < N:
            if not visited[next_y][next_x] and graph[next_y][next_x] == "1":
                visited[next_y][next_x] = visited[y][x] + 1
                DFS(next_x, next_y, visited[next_y][next_x])
                
distance = 0
DFS(0, 0, distance)
print(result)