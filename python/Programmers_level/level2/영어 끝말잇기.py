def solution(n, words):
    answer = []
    arr = [[] for _ in range(n)]
    arr[0].append(words[0])
    first = words[0][0]
    last = words[0][-1]
    index = 1
    
    def find_over(s):
        # 중복되는 수가 있는 경우
        for i in arr:
            for j in i:
                if j == s:
                    return True
        return False
    
    for i in range(1, len(words)):
        first = words[i][0]
        if index >= n:
            index = 0
        # 끝말잇기 성공
        if (first == last and len(words[i]) != 1 and not find_over(words[i])):
            last = words[i][-1]
            arr[index].append(words[i])   
            index += 1
        else: # 끝말잇기 실패
            index += 1
            answer.append(index)
            answer.append(len(arr[index-1]) + 1)
            return answer
        
    answer = [0, 0]
    return answer