def solution(n):
    result = []
    # 약수찾기
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            result.append(i)
            if n // i not in result:
                result.append(n // i)
                
    answer = sum(result)
    return answer