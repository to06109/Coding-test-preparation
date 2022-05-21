# BOJ 1074 Z
# 틀린 코드 -> 사분면으로 나눠서 분할정복으로 풀어야하는듯
# 반례: 5, 5, 5 -> 정답: 828, 내 답: 876
N, r, c = map(int, input().split())

length = 2 ** N - 1
half = 2 ** (N-1) - 1

count = 0

def counting(start_r, start_c):
    cnt = 0
    
    # 몇번째 4개짜린지 찾기
    dif_r = r - start_r
    dif_c = c - start_c
    # 현재 위치 전 상자까지의 개수
    num = (dif_r // 2) * ((half + 1) // 2) + (dif_c // 2)
    
    cnt += num * 4

    # 현재 4개짜리에서 몇번째인지 찾기
    # 현재 위치 시작위치 찾기 -> num+1번째 상자의 시작위치
    s_r = start_r + (dif_r // 2) * 2
    s_c = start_c + (dif_c // 2) * 2

    diff_r = r - s_r
    diff_c = c - s_c
    if diff_r == 0 and diff_c == 0:
        cnt += 1
    elif diff_r == 0 and diff_c == 1:
        cnt += 2
    elif diff_r == 1 and diff_c == 0:
        cnt += 3
    else:
        cnt += 4
    
    return cnt

half_num = (half+1) * (half+1)
# 1사분면
if 0 <= r <= half and 0 <= c <= half:
    # 개수세기
    count += counting(0, 0)
# 2사분면
elif 0 <= r <= half and half < c <= length:
    count += half_num
    count += counting(0, half + 1)
# 3사분면
elif half < r <= length and 0 <= c <= half:
    count += 2 * half_num
    count += counting(half + 1, 0)
# 4사분면
else:
    count += 3 * half_num
    count += counting(half + 1, half + 1)

print(count - 1) # 카운팅을 0부터 시작하므로

# 예제는 다 맞았는데 틀렸습니다 뜸
