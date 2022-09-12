def solution(numbers):
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    stand = set(arr)
    stand2 = set(numbers)
    answer = sum(list(stand - stand2)) # 차집합
    return answer