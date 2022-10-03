import math
def solution(arr):
    
    # 소인수 판별 함수
    def isprime(n):
        if n == 0 or n == 1:
            return False
        elif n == 2:
            return True
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
    lcm = 1
    # 소인수 배열
    primes = [_ for _ in range(max(arr) + 1) if isprime(_)]
    # 아무 것으로도 안나누어 질 때까지 나누기
    for prime in primes:
        while True:
            temp = 0
            for idx in range(len(arr)):
                if arr[idx] % prime == 0:
                    temp += 1
                    arr[idx] = arr[idx] // prime

            if temp: # 나누어 지는 게 있으면 나누기
                lcm *= prime
            else:
                break

    return lcm