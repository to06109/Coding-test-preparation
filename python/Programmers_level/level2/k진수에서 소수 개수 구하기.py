import math
def solution(n, k):
    temp = ["0*0", "*0", "0*", "*"]
    # 소수판별
    def isprime(num):
        if num == 1:
            return False
        elif num == 2:
            return True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    # n진법으로 바꾸기
    def transform(n, k): 
        s = ''
        while(n != 0):
            n, remain = n // k, n % k
            s += str(remain)
        return s[::-1]
    
    transformed_n = transform(n, k)
    # 문자열에서 0이 아닌 숫자 배열
    arr = transformed_n.split("0")
    
    # 소수인 숫자 "*"로 대체
    for letter in arr:
        if letter != "":
            if isprime(int(letter)):
                transformed_n = transformed_n.replace(letter, "*")
    # 조건에 맞는 소수 "#"로 대체
    for condition in temp:
        transformed_n = transformed_n.replace(condition, "#")
    # "#" 개수 새기
    return transformed_n.count("#")



''' 다른 사람의 풀이 '''
# n을 k진법으로 나타낸 문자열 반환
def conv(n, k):
    s = ''
    while n:
        s += str(n%k)
        n //= k
    return s[::-1]

# n이 소수인지 판정
def isprime(n):
    if n <= 1: return False
    i = 2
    while i*i <= n:
        if n%i == 0: return False
        i += 1
    return True

def solution(n, k):
    s = conv(n,k)
    cnt = 0
    for num in s.split('0'):
        if not num: continue # 빈 문자열에 대한 예외처리
        if isprime(int(num)): cnt += 1
    return cnt