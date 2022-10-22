def solution(citations):
    citations.sort()
    
    for h in range(citations[-1], -1, -1):
        temp = 0
        for item in citations:
            if item >= h:
                temp += 1
        if temp >= h:
            return h