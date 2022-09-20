def solution(n):
    # 10진법 -> 3진법 변환 함수 (앞뒤 반전버전)
    def transform(i): 
        temp = ""
        remain = i
        while(i != 0):
            # 몫, 나머지
            remain, i = i % 3, i // 3
            temp += str(remain)
        return temp
    
    return int(transform(n), 3) # 3진법 -> 10진법