# BOJ 1107
# 64ms
# 30840KB
# brute force

import sys
input = sys.stdin.readline

button = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
broken = []
N = int(input()) # 가고싶은 채널
M = int(input()) # 고장난 버튼의 개수
if M != 0:
    broken = map(int, input().split())
button = list(set(button) - set(broken)) # 남은 버튼

# 근사 함수
def approx(num):
    temp = str(num)
    for i in temp:
        if int(i) not in button:
            return False
    return True

# 1. 가고싶은 채널에서 현재채널 차이만큼 +나 -누르기
if N >= 100:
    min1 = N - 100
else:
    min1 = 100 - N

# 2. 가고싶은 채널 근사치 만들기
if button != []:
    impossible = 0

    # 아래로 근사치
    num_minus = N
    while 1:
        # 아래로 근사치 만들 수 없는 경우
        if num_minus < 0:
            impossible = 1
            break
        
        if approx(num_minus) == True:
            break
        num_minus -= 1

    # 위로 근사치
    num_plus = N
    while 1:
        if approx(num_plus) == True:
            break

        # 아래로 근사치했을 때 최소값을 넘어버리면 위로 근사치 찾기 중지
        if impossible != 1 and num_plus - N > N - num_minus:
            break
        num_plus += 1

    min2 = len(str(num_plus)) + num_plus - N
    if impossible == 1:
        min3 = sys.maxsize
    else:
        min3 = len(str(num_minus)) + N - num_minus
    
else:
    min2 = sys.maxsize
    min3 = sys.maxsize

print(min(min1, min2, min3))


