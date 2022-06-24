def solution(arr):
    # list.remove()
    mini = min(arr) # 최소값 찾기
    arr.remove(mini) # 배열에서 최소값 제거
    
    if len(arr) == 0: # 빈 배열 예외처리
        arr.append(-1)
        
    answer = arr
    return answer