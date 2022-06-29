def solution(n, arr1, arr2):
    # 지도 해독하기
    def map(arr):
        temp = []
        for i in range(n):
            temp.append(str(bin(arr[i])[2:].zfill(n)))
        return temp
    
    arr1 = map(arr1)
    arr2 = map(arr2)
    
    answer = [] # 최종 지도
    for a in range(n):
        temp = ''
        for b in range(n):
            if arr1[a][b] == "1" or arr2[a][b] == "1": # 벽인 경우
                temp += "#"
            else: # 공백인 경우
                temp += " "
        answer.append(temp)
    return answer