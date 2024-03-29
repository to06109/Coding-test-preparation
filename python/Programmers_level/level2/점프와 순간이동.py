def solution(n):
    ans = 1
    while n > 1:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            ans += 1

    return ans

'''
각 위치에서 점프나 순간이동을 했을 경우 소모된 배터리양을 각각 구하는 완탐
-> 시간복잡도가 O(2^N)으로 너무 크고 이때 N이 최대 10억이 될 수 있으므로 
    이 방법으로는 불가할 것이라고 판단
    
규칙을 살펴보니 2로 나누어지면 n을 2로 나누고 아니면 1을 배서 2로 나누어지게 만들어서
n이 1이 될 때까지 이 행동을 반복하면 사용해야 하는 건전지 사용량의 최솟값을 구할 수 있다.
'''