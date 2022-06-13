# BOJ 7562 나이트의 이동
# BFS
# 3024ms
# 32468KB

from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
# 시계방향으로
drow = [-1, -2, -2, -1, 1, 2, 2, 1]
dcol = [-2, -1, 1, 2, 2, 1, -1, -2]

def BFS(row, col):
    queue = deque([])
    
    # 방문체크
    queue.append([row, col, 0])
    visited[row][col] = True
    
    while queue:
        cur_row, cur_col, count = map(int, queue.popleft())
        # 도착하면 함수 종료 
        if cur_row == arrival[0] and cur_col == arrival[1]:
            print(count)
            return
        
        for j in range(8):
            next_row = cur_row + drow[j]
            next_col = cur_col + dcol[j]
            if 0<=next_row<I and 0<=next_col<I and visited[next_row][next_col] == False:
                queue.append([next_row, next_col, count + 1])
                visited[next_row][next_col] = True
                
for i in range(N):
    I = int(input())
    visited = [[False] * I for _ in range(I)]
    depart = list(map(int, input().split()))
    arrival = list(map(int, input().split()))
    BFS(depart[0], depart[1])
    
