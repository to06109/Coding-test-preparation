# BOJ 2667 단지번호 붙이기
# DFS
# 72ms
# 31088KB

import sys
input = sys.stdin.readline

N = int(input())
graph = []
for i in range(N):
    graph.append(input().rstrip())

# 상하좌우  
dx = [-1, 1, 0, 0]  
dy = [0, 0, -1, 1]

result = []
visited = [[False] * N for _ in range(N)]
def DFS(x, y):
    
    global count
    
    # 방문처리
    visited[x][y] = True
    count += 1
    
    # 해당 노드에서 상하좌우 있는지 확인
    for i in range(4):
        next_x = x + dx[i]
        next_y = y + dy[i]
        if next_x >= 0 and next_y >= 0 and next_x < N and next_y < N:
            if graph[next_x][next_y] == '1' and not visited[next_x][next_y]:
                DFS(next_x, next_y)
        
for i in range(N):
    for j in range(N):
        if graph[i][j] == '1' and visited[i][j] == False:
            count = 0
            DFS(i, j)
            result.append(count)
            
print(len(result))
result.sort()
for i in result:
    print(i)