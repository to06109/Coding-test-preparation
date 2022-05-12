# BOJ 10818
# 428ms
# 148408KB

N = int(input())
arr = list(map(int, input().split()))

a = min(arr)
b = max(arr)
print(a, b, end="")