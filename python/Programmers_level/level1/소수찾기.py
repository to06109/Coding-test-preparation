def solution(n):
    def isprime(a):
        if a == 1:
            return False
        if a == 2:
            return True
        for x in range(2, int(a**0.5) + 1):
            if a % x == 0:
                return False
        return True
    
    result = 0
    for i in range(1, n+1):
        if isprime(i):
            result += 1
    
    return result