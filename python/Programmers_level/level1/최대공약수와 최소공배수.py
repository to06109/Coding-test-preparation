# Programmers 최대공약수와 최소공배수
def solution(n, m):
    answer = []
    a, b = n, m
    # 최대공약수 구하기
    while a % b != 0:
        a, b = b, a % b
    answer.append(b)
    # 최소공배수 구하기, n * m = L * G
    answer.append(n * m // b)
    return answer