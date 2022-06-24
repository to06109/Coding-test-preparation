def solution(a, b):
    answer = 0
    
    # 예외처리
    if a > b:
        a, b = b, a
    
    for i in range(a, b+1):
        answer += i
    # answer = sum(range(a, b+1)) 이렇게도 가능!
        
    return answer