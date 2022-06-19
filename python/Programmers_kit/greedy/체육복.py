# Programmers 체육복
# 그리디
def solution(n, lost, reserve):
    num = [1 for _ in range(n)] # 각 학생마다 가지고 있는 체육복 수 리스트
    for i in lost: 
        num[i-1] -= 1
    for j in reserve:
        num[j-1] += 1
        
    for index in range(n):
        if num[index] == 0: # 체육복이 없는 학생의 경우
            # 앞에 빌려줄 사람 찾기
            if (index-1) > -1 and num[index-1] == 2:
                num[index] += 1
                num[index-1] -= 1
            # 뒤에 빌려줄 사람 찾기
            elif (index+1) < n and num[index+1] == 2:
                num[index] += 1
                num[index+1] -= 1
    answer = 0
    for res in num:
        if res > 0:
            answer += 1
            
    return answer