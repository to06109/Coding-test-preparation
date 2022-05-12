# BOJ 10952
# 68ms
# 30840KB

import sys
input = sys.stdin.readline
while 1:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print(a+b)