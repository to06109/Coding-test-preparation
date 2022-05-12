# BOJ 2562
# 72ms
# 30840KB

import sys
input = sys.stdin.readline

arr = []
for i in range(9):
    arr.append(int(input()))

print(max(arr))
print(arr.index(max(arr)) + 1)

'''
파이썬에서 원하는 문자의 위치를 찾고싶을 때: find, index
find: 원하는 문자가 존재하지 않을 경우, -1 반환
index: 원하는 문자가 존재하지 않을 경우, 에러메세지 반환
'''
