import sys 
sys.setrecursionlimit(100000) # 런타임에러 해결
def solution(n):
    def factorial(n):
        if n == 0:
            return 1
        return n * factorial(n-1)
    
    answer = 0
    
    one_num = n
    two_num = 0
    while True:
        answer += factorial(one_num + two_num) // (factorial(one_num) * factorial(two_num))
        two_num += 1
        one_num = n - 2 * two_num
        if one_num < 0:
            break

    return answer % 1234567

# 다른 사람의 풀이
def jumpCase(num):
    if num==1:
        return 1
    elif num==2:
        return 2
    else:
        return jumpCase(num-1)+jumpCase(num-2)