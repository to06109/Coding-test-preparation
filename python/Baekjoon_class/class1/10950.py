# BOJ 10950
# 68ms
# 30840KB

import sys
input = sys.stdin.readline

N = int(input())
for i in range(N):
    a, b = map(int, input().split())
    print(a+b)