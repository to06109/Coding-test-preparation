# 프로그래머스 문자열 압축 - 완전탐색
def solution(s):
    result = [] # 1 - n개로 자를 때 나오는 문자열의 길이 배열
    n = len(s)
    # 아예 잘라버리자
    def count_len(num):
        temp = [] # n개로 자른 문자열 배열
        index = 0
        while index < n:
            if index + num > n:
                temp.append(s[index:n])
                break
            temp.append(s[index:index+num])
            index = index + num
        
        string = '' # n개로 자를 시 압축된 문자열
        count = 1
        for i in range(len(temp)):
            
            cur = temp[i]
            if i == len(temp) - 1: # 마지막 요소라 다음 요소와 비교할 수 없을 때
                if count > 1:
                    string += str(count) + cur
                else:
                    string += cur
                break
            next = temp[i+1]
            
            if cur == next: # 현재 문자열과 다음 문자열이 동일한 경우 count 업데이트
                count += 1
            else:
                if count > 1:
                    string += str(count) + cur
                else:
                    string += cur
                count = 1 # count 초기화
                
        result.append(len(string))            

    for i in range(1, n+1): # 완탐, 문자열을 1개로 - n개로 잘랐을 경우  모두 고려
        count_len(i)
        
    answer = min(result)
    return answer