def solution(progresses, speeds):
    finish = []
    # 개발완료까지 남은 일수 계산
    for i in range(len(progresses)):
        remain_day = 100 - progresses[i]
        if remain_day % speeds[i] == 0:
            finish.append(remain_day // speeds[i])
        else:
            finish.append(remain_day // speeds[i] + 1)
    
    # 맨 앞 기능부터 남은 일수가 맨 앞 일수보다 작은 기능들 모두 pop
    result = []
    while finish:
        max_value = finish[0]
        count = 0 
        while finish and max_value >= finish[0]:
            finish.pop(0)
            count += 1
        result.append(count)
    answer = result
    return answer