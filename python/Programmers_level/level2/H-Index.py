def solution(citations):
    citations.sort()
    citations.append(-1)
    
    # print(citations)
    for idx in range(len(citations) - 2, -1, -1):
        
        h = citations[idx]
        # print(idx, h)
        if len(citations) - idx > h and idx - 1 < h:
            next = citations[idx + 1]
            # print(next)
            if next != -1:
                h = next  - 1
            return h