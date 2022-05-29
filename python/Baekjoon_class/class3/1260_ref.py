# BOJ 1260 BFS와 DFS
# 80ms
# 32280KB
# 처음에 연결된 노드를 그래프로 만들어놓으면 양방향 간선인것과 
# 작은 노드부터 탐색하는 과정을 따로 처리해주지 않아도 됨
# BFS 구현할 때 deque를 쓰는 것보다 list를 쓰는 게 더 효율적

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]
# 각 노드에 연결된 노드들을 정리
for _ in range(M):
	u, v = map(int, input().split())
	graph[u].append(v)
	graph[v].append(u)
# 연결된 노드들을 정렬 -> 작은 노드부터 탐색하도록
for i in graph:
	i.sort()

# DFS -> 재귀
visited_dfs = [False] * (N + 1)
result_dfs = []
def DFS(graph, v):
    # 현재 노드 방문처리
	result_dfs.append(v)
	visited_dfs[v] = True
    # 현재 노드에 연결되어 있으면서 방문하지 않은 노드 방문
	for i in graph[v]:
		if not visited_dfs[i]:
			DFS(graph, i)

# BFS -> 큐
visited_bfs = [False] * (N + 1)
queue = []
result_bfs = []
def BFS(graph, v):
    # 현재 노드 큐에 넣고 방문처리
	queue.append(v)
	visited_bfs[v] = True 
    # 큐가 비지 않을 때까지
	while queue:
        # 큐에서 pop
		node = queue.pop(0)
		result_bfs.append(node)
        # 현재 노드에 연결되어있고 방문하지 않은 노드 큐에 삽입, 방문처리
		for i in graph[node]:
			if not visited_bfs[i]:
				queue.append(i)
				visited_bfs[i] = True
	
DFS(graph, V)
BFS(graph, V)

print(*result_dfs)
print(*result_bfs)