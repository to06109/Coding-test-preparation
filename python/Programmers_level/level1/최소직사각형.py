def solution(sizes):
    w_arr = []
    v_arr = []
    # 큰 숫자를 w_arr에 몰기
    for i in sizes:
        w, v = i[0], i[1]
        if w < v:
            w, v = i[1], i[0]
        w_arr.append(w)
        v_arr.append(v)

    return max(w_arr) * max(v_arr)