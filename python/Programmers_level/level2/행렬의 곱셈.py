def solution(arr1, arr2):
    answer = [[] for _ in range(len(arr1))]
    for m1 in range(len(arr1)):
        for n2 in range(len(arr2[0])):
            result = 0
            for n1 in range(len(arr1[0])):
                result += arr1[m1][n1] * arr2[n1][n2]
            answer[m1].append(result)
            
    return answer