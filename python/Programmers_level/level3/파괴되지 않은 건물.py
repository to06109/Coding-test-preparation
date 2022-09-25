# 현재 시간복잡도: O(N*M)
# 2차원배열 누적합으로 풀어야 효율성 테스트 통과함
def solution(board, skill):
    for skill_one in skill:
        skill_type, r1, c1, r2, c2, degree = skill_one 
        
        if skill_type == 1: # attack 
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    board[i][j] -= degree
        elif skill_type == 2: # heal
            for i in range(r1, r2+1):
                for j in range(c1, c2+1):
                    board[i][j] += degree
    
    result = 0
    for n in range(len(board)):
        for m in range(len(board[0])):
            if board[n][m] > 0:
                result += 1

    return result