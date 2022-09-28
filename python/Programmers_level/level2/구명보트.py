# 실패코드 다시 풀어야함
from collections import deque
def solution(people, limit):
    people.sort()
    queue = deque(people)
    result = 0
    while queue:
        total = 0
        while queue and total <= limit:
            value = queue.popleft()
            total += value
        result += 1
        if total > limit:
            queue.appendleft(value)
            
    return result

'''
people을 정렬한 다음 가장 몸무게가 가장 큰 사람과 
가장 작은 사람의 값을 더해 limit값과 비교한 다음, 
작으면 둘 다 태우고, 크면 가장 큰 사람만 태운다.

이 때 주의할 점은 indexing으로 비교하는 것이 아니라, 
pop 혹은 del, remove등 리스트 자체에서 빼버리면 
정답은 맞을지라도 효율성 부분에서 틀려버린다.
'''