# BOJ 7576 토마토
# 2312ms
# 106160KB

import sys
from collections import deque
input = sys.stdin.readline
M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 상하좌우
dx = [0, 0, -1, 1] # 열
dy = [-1, 1, 0, 0] # 행
# 정답이 들어갈 변수
count = 0 
# 좌표를 넣을 것이므로 deque에 []를 넣어줌
queue = deque([])
# 처음에 받은 토마토의 위치 좌표를 queue에 append.
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1:
            queue.append([j, i])
            
def BFS():
    while queue:
        print(queue)
        # 토마토의 위치좌표 꺼내기
        node = queue.popleft()
        for i in range(4):
            next_x = node[0] + dx[i]
            next_y = node[1] + dy[i]
            # 해당 좌표가 graph의 크기를 넘어가면 안되고 그 좌표애 토마토가 익지 않은 채로 있어야 함(0)
            if 0 <= next_x < M and 0 <= next_y < N and graph[next_y][next_x] == 0:
                queue.append([next_x, next_y])
                graph[next_y][next_x] = graph[node[1]][node[0]] + 1

BFS()

# BFS 다 끝났는데 0이 존재하면 -1 출력
for m in graph:
    for n in m:
        if n == 0:
            print(-1)
            exit(0)
    # 0이 없다면 graph의 최대값이 정답이 됨
    count = max(count, max(m))

print(count - 1)

# 참고링크: https://jae04099.tistory.com/entry/%EB%B0%B1%EC%A4%80-7576-%ED%86%A0%EB%A7%88%ED%86%A0-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%95%B4%EC%84%A4%ED%8F%AC%ED%95%A8