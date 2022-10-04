import datetime
def solution(today, terms, privacies):
    result = []
    # 날짜 계산
    def cal_date(year, month, day, term_month):
        print("1", year, month, day, term_month)
        month += term_month
        while(month > 12):
            year += 1
            month -= 12

        day -= 1
        if day == 0:
            month -= 1
            day = 28
        
        if month <= 0:
            year -= 1
            month = 12
            
        print("2", year, month, day, term_month)
        return datetime.datetime(year, month, day)

    # 약관 정보 저장
    term = {}
    for _ in terms:
        term_type, period = _.split(" ")
        term[term_type] = int(period)
    # 오늘 날짜 계산
    t_y, t_m, t_d = map(int, today.split("."))
    today_time = datetime.datetime(t_y, t_m, t_d)
    # 유효기한 계산
    for privacy in range(len(privacies)):
        temp, term_type = privacies[privacy].split(" ")
        year, month, day = map(int, temp.split("."))
        term_month = term[term_type]
        if today_time > cal_date(year, month, day, term_month):
            result.append(privacy + 1)

    return result

# 테스트 함수 작성
import random
for i in range(100):
    year = random.randrange(2000, 2023)
    month = random.randrange(1, 13)
    day = random.randrange(1, 29)
    today = str(year) + "." + str(month) + "." + str(day)
    
    terms = []
    period = random.randrange(1, 101)
    terms.append("A " + str(period))
    period = random.randrange(1, 101)
    terms.append("B " + str(period))
    period = random.randrange(1, 101)
    terms.append("Z " + str(period))

    privacies = []
    string_pool = "ABZ"
    for _ in range(100):
        year2 = random.randrange(2000, 2023)
        month2 = random.randrange(1, 13)
        day2 = random.randrange(1, 29)
        today2 = str(year2) + "." + str(month2) + "." + str(day2)
        
        privacies.append(today2 + " " + random.choice(string_pool))

    print(privacies)
    print(solution(today, terms, privacies))
    print("----------------------------------")
