# BOJ 1389 케빈 베이컨의 6단계 법칙
# 296ms
# 34932KB

import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

# 인접정점 오름차순 방문
for j in range(N + 1):
    graph[j].sort()

def check_baken(s): # BFS 하자
    queue = deque([])
    queue.append([s, 0])
    global count
    visited[s] = True # 방문처리
    
    while queue:
        cur, cnt = map(int, queue.popleft())
        if cur == end:
            return cnt
        for i in graph[cur]:
            if not visited[i]:
                queue.append([i, cnt + 1])

result = []
for start in range(1, N+1): # 모든 유저의 kebin baken 수 세기
    baken = 0
    for end in range(1, N+1): # 유저 한명의 kebin baken 수 세기
        visited = [False] * (N + 1)
        count = 0
        if end == start: # 본인 -> 본인 케이스 제외
            continue 
        baken += check_baken(start) # 출발지
    result.append(baken)

temp = min(result)
print(result.index(temp) + 1) # 케빈베이컨 수가 가장 작은 사람 출력
        

