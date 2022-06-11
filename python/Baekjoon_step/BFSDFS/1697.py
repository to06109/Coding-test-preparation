# BOJ 1697 숨바꼭질
# 메모리초과
from collections import deque
N, K = map(int, input().split())
# 수빈이가 갈 수 있는 곳 다 찾기??
queue = deque([])
def BFS():
    queue.append([N, 0]) # 수빈이 위치, 간 거리
    while queue:
        cur, cnt = queue.popleft()
        print(cur)
        if cur == K:
            print(cnt)
            break
        queue.append([2 * cur, cnt + 1])
        queue.append([cur + 1, cnt + 1])
        queue.append([cur - 1, cnt + 1])
        
BFS()