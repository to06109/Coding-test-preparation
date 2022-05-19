# BOJ 1012 유기농 배추
# DFS -> 재귀
import sys
input = sys.stdin.readline
T = int(input())
# 가로, 세로, 배추 개수
M, N, K = map(int, input().split())
visit = [list(map(int, input().split())) for _ in range(K)]

graph = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
for k in range(K):
    x, y = visit[k][0], visit[k][1]
    graph[y][x] = 1


# 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(idx, arr):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if 0 > arr[0] or arr[0] >= M or 0 > arr[1] or arr[1] >= N or idx >= K:
        return False
    
    if arr in visit: # 현재 노드에 배추가 있고
        if not visited[arr[1], arr[0]]: # 현재 노드를 아직 방문하지 않았다면
            # 현재 노드를 방문처리
            visited[arr[1], arr[0]] = True
             
            # 상하좌우 확인
            dfs(idx + 1, [arr[0] + dx[0], arr[1] + dy[0]])
            dfs(idx + 1, [arr[0] + dx[1], arr[1] + dy[1]])
            dfs(idx + 1, [arr[0] + dx[2], arr[1] + dy[2]])
            dfs(idx + 1, [arr[0] + dx[3], arr[1] + dy[3]])
            return True 

            # for m in range(4): 
            #     x_next = arr[0] + dx[m]
            #     y_next = arr[1] + dy[m]
            #     dfs(idx + 1, [x_next, y_next])
    return False

count = 0
for i in range(K):
    if dfs(i, visit[i]) == True:
        count += 1

print(count)





