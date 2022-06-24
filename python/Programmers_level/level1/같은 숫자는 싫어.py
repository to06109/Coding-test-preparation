def solution(arr):
    result = []
    pre = -1
    # 이전숫자 저장하기
    for i in range(len(arr)):
        if arr[i] != pre:
            result.append(arr[i])
        pre = arr[i]
    
    answer = result
    return answer