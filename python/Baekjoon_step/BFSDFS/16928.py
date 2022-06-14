# BOJ 16928 뱀과 사다리 게임
# list 대신 dict 이용
# 100ms
# 32460KB

import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())

ladder = dict()
snake = dict()
for n in range(N):
    depart, arrival = map(int, input().split())
    ladder[depart] = arrival
for m in range(M):
    start, end = map(int, input().split())
    snake[start] = end

visited = [False] * 101

def BFS():
    queue = deque()
    # 방문처리
    visited[1] = True
    queue.append([1, 1])
    while queue:
        cur, cnt = queue.popleft()
        if cur == 100:
            print(cnt - 1)
            return
        for j in range(1, 7):
            next = cur + j
            if 0<next<101 and visited[next] == False:
                # 사다리 확인
                if next in ladder.keys():
                    next = ladder[next]
                if next in snake.keys():
                    next = snake[next]
                queue.append([next, cnt + 1])
                visited[next] = True

BFS()