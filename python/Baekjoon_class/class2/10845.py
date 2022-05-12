# BOJ 10845 큐
# 80ms
# 30840KB

import sys
input = sys.stdin.readline
N = int(input())
queue = []
for i in range(N):
    string = input().rstrip()
    if "push" in string:
        temp, x = string.split()
        queue.append(x)
    elif string == "pop":
        if queue:
            print(queue[0])
            del queue[0]
        else: 
            print(-1)
    elif string == "size":
        print(len(queue))
    elif string == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif string == "front":
        if queue:
            print(queue[0])
        else: print(-1)
    else:
        if queue:
            print(queue[-1])
        else: print(-1)

# 입력이 여러줄인 경우 sys.stdin.readline이 훨씬 빠름
    
