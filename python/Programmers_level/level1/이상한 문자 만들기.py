# 아스키코드 이용
def solution(s):
    l = list(s.split(' '))
    print(l)
    for i in range(len(l)):
        temp = list(l[i])
        for j in range(len(temp)):
            if j == 0 or j % 2 == 0:
                if 96 < ord(temp[j]) < 123: # 소문자인 경우
                    temp[j] = chr(ord(temp[j]) - 32)
            else:
                if 64 < ord(temp[j]) < 91: # 대문자인 경우
                    temp[j] = chr(ord(temp[j]) + 32)
        l[i] = ''.join(temp)
                                        
    answer = ' '.join(l)
    return answer