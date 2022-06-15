# BOJ 1389 케빈 베이컨의 6단계 법칙
# 92ms
# 32452KB
'''
굳이 각 사람마다 출발점과 목적지로 케빈 베이컨 수를 구하게 이중 for문 처리해줄 필요 없이
BFS함수에 출발점만 주면 출발점에서 그래프에 연결된 모든 노드에 도착하는 거리를 각각 num에 저장할 수 있으므로
함수를 다 돈 뒤에 num의 합을 구하면 그게 start번째 사람의 케빈 베이컨 수가 된다.

'''

import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

def check_bacon(s): # BFS
    queue = deque([s])
    num = [0] * (N + 1)
    visited[s] = True # 방문처리

    while queue:
        cur = queue.popleft()
        for i in graph[cur]:
            if not visited[i]:
                num[i] = num[cur] + 1 # i까지 가는 거리 계산
                queue.append(i)
                visited[i] = True
    
    return sum(num)

result = []
for start in range(1, N+1): # 모든 유저의 kevin bacon 수 세기
    visited = [False] * (N + 1)
    bacon = check_bacon(start) # 출발지
    result.append(bacon)

print(result.index(min(result)) + 1) # 케빈베이컨 수가 가장 작은 사람 출력

