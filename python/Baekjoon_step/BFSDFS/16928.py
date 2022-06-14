# BOJ 16928 뱀과 사다리 게임
# 108ms
# 32460KB

import sys
from collections import deque
input = sys.stdin.readline
graph = [i for i in range(1, 101)]
N, M = map(int, input().split())

ladder = []
snake = []
for n in range(N):
    ladder.append(list(map(int, input().split())))
for m in range(M):
    snake.append(list(map(int, input().split())))

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
            if 0<=next<101 and visited[next] == False:
                # 사다리 확인
                for a in ladder:
                    if next == a[0]:
                        next = a[1]
                for b in snake:
                    if next == b[0]:
                        next = b[1]

                queue.append([next, cnt + 1])
                visited[next] = True

BFS()