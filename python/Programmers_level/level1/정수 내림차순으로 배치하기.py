# 정렬
def solution(n):
    temp = []
    for i in str(n):
        temp.append(i)
        
    temp.sort(reverse=True)
    answer = int("".join(temp))
    
    return answer