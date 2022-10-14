# BOJ 1012
# 84ms
# 33220KB
# DFS -> 재귀

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

T = int(input())

# x: 열, y: 행 / 상하좌우
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(arr, x, y):
    # 방문처리
    arr[y][x] = 0
    
    # 상하좌우 확인
    for i in range(4):
        x2 = x + dx[i]
        y2 = y + dy[i]
        
        if -1 < x2 and x2 < M and -1 < y2 and y2 < N:
            if arr[y2][x2] == 1:
                dfs(arr, x2, y2)

for t in range(T):
    # 맵 만들기
    M, N, K  = map(int, input().split())
    temp = []
    for k in range(K):
        x, y = map(int, input().split())
        temp.append([x, y])

    arr = [[0 for _ in range(M)] for _ in range(N)]
    
    for item in temp:
        x2, y2 = item[0], item[1]
        arr[y2][x2] = 1
    
    result = 0
    for search in temp:
        x3,  y3 = search[0], search[1]
        if arr[y3][x3] == 1:
            dfs(arr, x3, y3)
            result += 1
    
    print(result)
    
    
