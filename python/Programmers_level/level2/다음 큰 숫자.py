def solution(n):
    answer = 0
    first = len(format(n,"b").split("1")) - 1
    
    while(1):
        n += 1
        second = len(format(n,"b").split("1")) - 1
        if first == second:
            answer = n
            break
            
    return answer

# 다은 사람의 풀이 -> count 이용
def nextBigNumber(n):
    num1 = bin(n).count('1')
    while True:
        n = n + 1
        if num1 == bin(n).count('1'):
            break
    return n
