# BOJ 1259 팰린드롬수
# 72ms
# 30840KB

while True:
    string = input()
    if string == "0":
        break

    # 팰린드롬수인지 확인
    # 반까지 문자열 추출해서 넣고
    length = len(string)
    arr = string[0: length // 2]

    # 뒤에서부터 추출한 문자열이랑 안맞으면 no 출력
    num = 0
    for i in range(length // 2):
        if arr[i] != string[length - i - 1]:
            num += 1
            break

    if num == 0:
        print("yes")
    else:
        print("no")

    
