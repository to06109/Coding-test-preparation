def solution(n):
    answer = 0
    temp = n ** 0.5
    if temp == int(n ** 0.5):
        answer = (temp + 1) ** 2
    else:
        answer = -1
        
    return answer