# 프로그래머스 기둥과 보 설치 - 빡구현
def solution(n, build_frame):
    current = [] # 현재까지 설치된 구조물 배열
    def check_condition1(x, y, a, b): # 설치하는 경우
        # 기둥의 경우
        if a == 0:
            if y == 0: # 바닥위에
                return True
            for j in current: # 보의 한쪽 끝부분 위에
                x0, y0, a0 = map(int, j)
                if x == x0 and y == y0 and a0 == 1: 
                    return True
                if x - 1 == x0 and y == y0 and a0 == 1:
                    return True
                if x == x0 and y - 1 == y0 and a0 == 0: # 기둥
                    return True
        # 보의 경우
        else:
            count = 0
            for m in current:
                x1, y1, a1 = map(int, m)
                if x == x1 and y-1 == y1 and a1 == 0: # 한 쪽 끝부분이 기둥 위에
                    return True
                if x+1 == x1 and y-1 == y1 and a1 == 0:
                    return True
                if x-1 == x1 and y == y1 and a1 == 1:
                    count += 1
                if x+1 == x1 and y == y1 and a1 == 1:
                    count += 1
            if count >= 2:
                return True
        return False
    
    def check_condition2(x, y, a, b): # 제거하는 경우
        if a == 0: # 기둥인 경우
            temp = []
            # 기둥에 걸쳐있는 애들 찾기
            for z in current:
                x1, y1, a1 = map(int, z)
                if x == x1 and y + 1 == y1 and a1 == 0:
                    temp.append([x1, y1, a1])
                if x-1 == x1 and y+1 == y1 and a1 == 1:
                    temp.append([x1, y1, a1])
                if x == x1 and y+1 == y1 and a1 == 1:
                    temp.append([x1, y1, a1])
            # 기둥을 제거해봄
            current.remove([x, y, a])
            # 제거했을 때 걸쳐있던 애들 다시 설치할 수 없으면 False
            for test in temp:
                t1, t2, t3 = map(int, test)
                if check_condition1(t1, t2, t3, 1) == False:
                    current.append([x, y, a])
                    return False
            current.append([x, y, a])
            
        else: # 보인 경우
            temp2 = []
            # 보에 걸쳐있는 애들 찾기
            for u in current:
                x2, y2, a2 = map(int, u)
                if a2 == 1 and x - 1 == x2 and y == y2:
                    temp2.append([x2, y2, a2])
                if a2 == 1 and x + 1 == x2 and y == y2:
                    temp2.append([x2, y2, a2])
                if a2 == 0 and x == x2 and y == y2:
                    temp2.append([x2, y2, a2])
                if a2 == 0 and x == x2 and y - 1 == y2:
                    temp2.append([x2, y2, a2])
                if a2 == 0 and x + 1 == x2 and y == y2:
                    temp2.append([x2, y2, a2])
                if a2 == 0 and x + 1 == x2 and y - 1 == y2:
                    temp2.append([x2, y2, a2])
            
            current.remove([x, y, a])
            # 제거했을 때 걸쳐있던 애들 다시 설치할 수 없으면 False
            for test in temp2:
                r1, r2, r3 = map(int, test)
                if check_condition1(r1, r2, r3, 1) == False:
                    current.append([x, y, a])
                    return False
            current.append([x, y, a])
        return True
                        
    for i in build_frame:
        x, y, a, b = map(int, i)
        # 설치한다면? 설치여부 확인하고 설치
        if b == 1:
            if check_condition1(x, y, a, b):
                current.append([x, y, a])
        else: # 제거한다면? 제거여부 확인하고 제거
            if check_condition2(x, y, a, b):
                current.remove([x, y, a])
    current.sort(key=lambda x:(x[0], x[1], x[2]))
    answer = current
    return answer