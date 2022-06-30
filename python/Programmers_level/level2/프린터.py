# 프로그래머스 프린터 - 큐
from collections import deque
def solution(priorities, location):
    queue = deque()
    for i in priorities:
        queue.append(i)
    count = 0 # 타켓 아닌 문서 먼저 인쇄할 경우
    while queue:
        if len(queue) == 1:
            count += 1
            break
        first = queue.popleft()
        location -= 1
        # first보다 우선순위가 큰게 있는지 확인
        num = max(list(queue))
        if first < num:
            # 뒤로보내기
            if location == -1:
                location = len(queue)
            queue.append(first)
        else:
            # 문서 인쇄
            if location == -1:
                count += 1
                break
            count += 1

    answer = count
    return answer