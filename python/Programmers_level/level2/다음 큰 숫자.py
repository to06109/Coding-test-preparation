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