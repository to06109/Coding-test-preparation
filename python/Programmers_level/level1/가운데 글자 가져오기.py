def solution(s):
    length = len(s)
    if length % 2 == 0: # 짝수개면
        index = length // 2 - 1 
        answer = s[index:index+2]
    else:
        index = length // 2
        answer = s[index]
    return answer