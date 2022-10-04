def solution(n,a,b):
    answer = 0
    arr = [False for _ in range(n)]

    arr[a - 1] = True
    arr[b - 1] = True

    while len(arr) > 1:
        temp = [False for i in range(n)]
        for idx in range(0, n, 2): # 상위 두 배열 요소 비교연산
            if arr[idx] and arr[idx+1]:
                answer += 1
                return answer
            elif arr[idx] or arr[idx+1]:
                temp[idx//2] = True
        # 한 라운드 끝
        arr = temp
        answer += 1 
        n = n // 2

    return answer

# 다른 사람의 풀이 -> 이게 더 빠르다.
# def solution(n, a, b):
#     answer = 0
#     while True:
#         if a  == b:
#             break
#         else:
#             if a % 2 == 1:
#                 a = a // 2 + 1
#             else:
#                 a = a // 2
#             if b % 2 == 1:
#                 b = b // 2 + 1
#             else:
#                 b = b // 2
#             answer += 1
#     return answer