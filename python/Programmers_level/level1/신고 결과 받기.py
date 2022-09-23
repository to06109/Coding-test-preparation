# def solution(id_list, report, k):
#     result = [0 for _ in range(len(id_list))] # 각 사용자가 받는 결과메일 개수
#     dict = {} # 각 사용자가 신고한 사람 배열
#     dict2 = {} # 각 사용자별 신고받은 횟수
#     for i in id_list:
#         dict2[i] = 0
#     for j in report:
#         user, reported = map(str, j.split())
#         if user in dict:
#             dict[user].append(reported)
#         else:
#             dict[user] = [reported]
#     # 중복신고 없애주기
#     for m in dict.keys():
#         dict[m] = list(set(dict[m]))
#     # 하나씩 돌아가면서 신고횟수 조회
#     for n in dict.keys():
#         temp = dict[n]
#         for z in temp:
#             dict2[z] += 1
            
#     # 신고당하는 유저목록 
#     reporteds = []
#     for a in dict2.keys():
#         if dict2[a] >= k:
#             reporteds.append(a)
#     # 신고결과 메일횟수 파악
#     for b in dict.keys():
#         for c in reporteds:
#             if c in dict[b]:
#                 idx = id_list.index(b)
#                 result[idx] += 1
    
#     answer = result
#     return answer

# 재 풀이(220923)
def solution(id_list, report, k):
    report_user = {}
    reported_user = {}
    stopped = []
    
    # 신고함
    for s in report:
        user, reported = s.split(" ")
        if user not in report_user:
            report_user[user] = [reported]
        else: report_user[user].append(reported)

    for reported_arr in report_user.values():
        for item in list(set(reported_arr)):
            if item not in reported_user:
                reported_user[item] = 1
            else: reported_user[item] += 1
    
    # 정지당하는 유저 찾기
    for key, value in reported_user.items():
        if value >= k:
            stopped.append(key)
    
    result = [0 for _ in range(len(id_list))]
    # 메일 보낼 유저 고르기
    for i in range(len(id_list)):
        for user in stopped:
            if id_list[i] in report_user:
                if user in report_user[id_list[i]]:
                    result[i] += 1

    return result