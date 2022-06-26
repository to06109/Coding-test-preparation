'''
파이썬 ASCII코드 이용
chr(숫자) : 숫자에 해당하는 문자
ord(문자) : 문자에 해당하는 숫자
'''
def solution(s, n):
    result = ''
    for i in s:
        if ord(i) != 32:
            temp = ord(i)+n
            if 64 < ord(i) < 91 and temp > 90:
                temp = temp - 90 + 64
            elif 89 < ord(i) < 123 and temp > 122:
                temp = temp - 122 + 96
            
            result += chr(temp)
        else:
            result += ' '
    answer = result
    return answer