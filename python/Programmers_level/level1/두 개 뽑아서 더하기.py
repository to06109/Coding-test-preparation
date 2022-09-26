from itertools import permutations 
def solution(numbers):
    result_arr = set()
    # 조합 구하기
    arr = list(permutations(numbers, 2))
    # 결과 set에 저장
    for i in arr:
        result_arr.add(i[0] + i[1] ) 
    return sorted(result_arr)