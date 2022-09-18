def solution(n):
    arr = [0 for i in range(n+1)]
    arr[0] = 0
    arr[1] = 1
    
    for j in range(2, n+1):
        arr[j] = (arr[j-1] % 1234567 + arr[j-2] % 1234567) % 1234567
    return arr[j]
