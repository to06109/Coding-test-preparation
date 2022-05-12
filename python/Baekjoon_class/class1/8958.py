# BOJ 8958
# 72ms
# 30840KB

import sys
input = sys.stdin.readline

N = int(input())
for i in range(N):
    arr = input().rstrip()
    current = 0
    result = 0
    for j in arr:
        if j == "X":
            current = 0
        else:
            current += 1
            result += current

    print(result)

'''
readline은 입력행을 모두 가져와 마지막에 \n도 가져온다.
따라서 입력받은 값을 문자열로 받을 때는 rstrip()을 이용해 \n을 제거해주던지
그냥 input을 쓰던지 해야함
'''

