import math
def solution(fees, records):
    arr = {}
    
    # 주차요금 계산 함수
    def calFee(minute):
        if minute <= fees[0]: return fees[1]
        else: return fees[1] + math.ceil((minute - fees[0]) / fees[2]) * fees[3]
    
    # 분 계산 함수
    def toMinute(s):
        hour, minute = map(int, s.split(":"))
        return hour * 60 + minute
    
    # 주차내역 정리
    for record in records:
        time, num, history = record.split(" ")
        if num not in arr:
            arr[num] = []
            arr[num].append([toMinute(time)])
            arr[num].append([])
        else:
            if history == "IN":
                arr[num][0].append(toMinute(time))
            elif history == "OUT":
                arr[num][1].append(toMinute(time))
    
    for key, value in arr.items():
        if len(value[0]) != len(value[1]):
            arr[key][1].append(toMinute("23:59"))
    
    # 주차시간 계산
    result_time = []
    for key in sorted(arr):
        time = 0
        for i in range(len(arr[key][0])):
            time += arr[key][1][i] - arr[key][0][i]
        result_time.append(time)

    # 주차요금 계산
    answer = []
    for _ in result_time:
        answer.append(calFee(_))
        
    return answer