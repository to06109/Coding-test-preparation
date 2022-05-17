# BOJ 18111 마인크래프트
# 높이가 0부터 256까지 모든 경우를 따져서 최솟값을 반환하면 되는 완전탐색 문제
# 836ms
# 117532KB

import sys
input = sys.stdin.readline
answer = sys.maxsize # 최대 정수값
idx = 0

N, M, B = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

# 0층부터 256층까지 반복
for target in range(257):
    max_target, min_target = 0, 0

    # 반복문을 통해 블록 확인
    for i in range(N):
        for j in range(M):

            # 블록이 층수보다 크면 빼기
            if graph[i][j] >= target:
                max_target += graph[i][j] - target

            # 블록이 층수보다 작으면 더하기
            else:
                min_target += target - graph[i][j]

    # 블록을 뺀 것과 원래있던 블록의 합과 블록을 더한 값을 비교
    if max_target + B >= min_target: # 만들 수 있음
        # 시간초 구하고 최저시간과 비교
        if min_target + (max_target * 2) <= answer:
            answer = min_target + (max_target * 2) # 최저시간
            idx = target # 층수

print(answer, idx)


# 참고링크: https://fre2-dom.tistory.com/457            



