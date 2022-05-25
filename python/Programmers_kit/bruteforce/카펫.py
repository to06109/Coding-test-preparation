# Programmers 카펫
# 브루트포스
def solution(brown, yellow):
    answer = []
    for i in range(1, yellow + 1):
        # yellow의 가로세로 계산
        if yellow % i == 0:
            y_width = yellow // i
        else:
            continue
        y_height = i
        # 필요한 brown 수 계산
        need_brown = (y_height + 2) * 2 + y_width * 2
        if need_brown == brown:
            break
            
    answer.append(y_width + 2)
    answer.append(y_height + 2)
    return answer