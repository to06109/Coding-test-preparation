# BOJ 2475
# 68ms
# 30840KB

arr = list(map(int, input().split()))
result = 0
for i in arr:
    result += i ** 2
print(result % 10)