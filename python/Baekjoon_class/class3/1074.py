# BOJ 1074 Z
# 72ms
# 30840KB
N, r, c = map(int, input().split())

count = 0

# 재귀
def counting(start_r, start_c, n): # r, c 시작점, N
    global count
    
    length = 2 ** n - 1
    half = 2 ** (n - 1) - 1
    
    if n == 1:
        # Z에서 카운팅
        if r == start_r and c == start_c:
            count += 1
        elif r == start_r and c == start_c + 1:  
            count += 2
        elif r == start_r + 1 and c == start_c:
            count += 3
        else:
            count += 4
        return
        
    half_num = (half+1) * (half+1)
    # 1사분면
    if start_r <= r <= start_r + half and start_c <= c <= start_c + half:
        # 4분면으로 다시 쪼개고 개수세기
        counting(start_r, start_c, n - 1)
    # 2사분면
    elif start_r <= r <= start_r + half and start_c + half < c <= start_c + length:
        count += half_num
        counting(start_r, start_c + half + 1, n - 1)
    # 3사분면
    elif start_r + half < r <= start_r + length and start_c <= c <= start_c + half:
        count += 2 * half_num
        counting(start_r + half + 1, start_c, n - 1)
    # 4사분면
    else:
        count += 3 * half_num
        counting(start_r + half + 1, start_c + half + 1, n - 1)
    
counting(0, 0, N)

print(count - 1) # 카운팅을 0부터 시작하므로 1 빼주기
