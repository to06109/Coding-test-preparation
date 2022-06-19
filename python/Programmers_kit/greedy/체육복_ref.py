# 다른 사람의 풀이
def solution(n, lost, reserve):
    # reserve와 lost 모두에 번호가 있는 사람은 제외 (수업을 들을 수 있으므로)
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost: # 앞사람 탐색
            _lost.remove(f)
        elif b in _lost: # 뒷사람 탐색
            _lost.remove(b)
    return n - len(_lost)