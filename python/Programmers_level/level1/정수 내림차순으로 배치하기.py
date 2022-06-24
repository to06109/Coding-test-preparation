# 정렬
def solution(n):
    temp = list(str(n))
    temp.sort(reverse=True)
    answer = int("".join(temp))
    return answer