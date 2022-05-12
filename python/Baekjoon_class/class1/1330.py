# BOJ 1330
# 68ms
# 30840KB
a, b = map(int, input().split())

if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("==")