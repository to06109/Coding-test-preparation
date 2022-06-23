def prime_num(num): # 약수의 개수 구하기
    res = 0
    for i in range(1, num + 1):
        if num % i == 0:
            res += 1
    return res

def solution(left, right): 
    result = 0
    for i in range(left, right + 1): 
        temp = prime_num(i)
        if temp % 2 == 0:
            result += i
        else:
            result -= i
    
    answer = result
    return answer