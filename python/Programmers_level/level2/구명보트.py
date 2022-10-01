from collections import deque
def solution(people, limit):
    people.sort()
    queue = deque(people)
    result = 0
    
    while queue:
        mini = queue[0]
        maxx = queue[-1]
        
        # 큐에 한 사람 밖에 없을 경우
        if len(queue) == 1:
            result += 1
            break
        # 두 명 다 태울 경우
        if mini + maxx <= limit:
            queue.popleft()
        # 두 명 못태우는 경우 -> 최대값만 태움
        queue.pop()
        result += 1
    
    return result

'''
people을 정렬한 다음 가장 몸무게가 가장 큰 사람과 
가장 작은 사람의 값을 더해 limit값과 비교한 다음, 
작으면 둘 다 태우고, 크면 가장 큰 사람만 태운다.

이 때 주의할 점은 indexing으로 비교하는 것이 아니라, 
리스트에서 pop, del, remove등을 사용해 빼면 효율성 부분에서 틀린다.

하지만 deque의 pop을 사용하면 시간복잡도가 O(1)으로 
요소를 뺄 수 있으므로 효율성 테스트에 통과한다. 
'''