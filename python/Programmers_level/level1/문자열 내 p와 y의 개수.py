# 내 풀이
from collections import Counter
def solution(s):
    dict = Counter(s.lower())
    p_num = dict["p"]
    y_num = dict["y"] # dict에 없으면 0을출력해준다. Counter는 친절하다..
    return p_num == y_num


# 방법 2 -> count() 사용
def numPY(s):
    # 함수를 완성하세요
    return s.lower().count('p') == s.lower().count('y')