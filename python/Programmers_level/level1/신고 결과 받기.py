def solution(id_list, report, k):
    result = [0 for _ in range(len(id_list))]
    dict = {} # 각 사용자가 신고한 사람 배열 정리
    dict2 = {} # 각 사용자별 신고받은 횟수 정리
    for i in id_list:
        dict2[i] = 0
    for j in report:
        user, reported = map(str, j.split())
        if user in dict:
            dict[user].append(reported)
        else:
            dict[user] = [reported]
    # 중복신고 없애주기
    for m in dict.keys():
        dict[m] = list(set(dict[m]))
    # 하나씩 돌아가면서 신고횟수 조회
    for n in dict.keys():
        temp = dict[n]
        for z in temp:
            dict2[z] += 1
    
    reporteds = []
    # 신고당하는 애들 거르기
    for a in dict2.keys():
        if dict2[a] >= k:
            reporteds.append(a)
    # 신고결과 메일횟수 파악
    for b in dict.keys():
        for c in reporteds:
            if c in dict[b]:
                idx = id_list.index(b)
                result[idx] += 1
    
    answer = result
    return answer