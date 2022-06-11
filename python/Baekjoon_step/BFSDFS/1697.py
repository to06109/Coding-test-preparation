# BOJ 1697 숨바꼭질
# 152ms
# 34692KB

from collections import deque
N, K = map(int, input().split())
# 수빈이가 갈 수 있는 곳 다 찾기??
queue = deque()
def BFS():
    queue.append(N) # 수빈이 위치
    while queue:
        cur = queue.popleft()
        # 동생위치 도착하면 함수 종료
        if cur == K: 
            return
        
        for i in (cur - 1, cur + 1, cur * 2):
            if 0 <= i < 100001 and dp[i] == 0:
                dp[i] = dp[cur] + 1
                queue.append(i)

dp = [0] * 100001
BFS()
print(dp[K])