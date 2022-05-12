import sys
input = sys.stdin.readline
while 1:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except ValueError:
        break

# 개수 정해지지 않은 입력 받을 경우, try, except