# BOJ 2739
# 68ms
# 30840KB

N = int(input())

for i in range(1, 10):
    print("%d * %d = %d" % (N, i, N * i))

'''
문자열에 변수 넣어서 출력: format,  %d
format: print("Case #{0}: {1}".format(i + 1, a + b))
%d: print("Case #%d: %d" % (i + 1, a + b))
'''

