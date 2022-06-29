def solution(s):
    # isdigit() 문자열이 숫자이면 True 반환
    lenth = len(s)
    if lenth == 4 or lenth == 6:
        if s.isdigit():
            return True
    return False