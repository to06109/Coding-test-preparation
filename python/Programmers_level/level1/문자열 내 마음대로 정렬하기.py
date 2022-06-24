def solution(strings, n):
    result = []
    dict = {}
    # 인덱스 문자 기준으로 dict에 저장
    for i in strings:
        if i[n] in dict:
            dict[i[n]].append(i)
        else:
            dict[i[n]] = [i]
    key = list(dict.keys())
    key.sort()
    
    # 오름차순으로 정렬한 결과 result에 저장
    for j in key:
        dict[j].sort()
        for m in dict[j]:
            result.append(m)

    answer = result
    return answer