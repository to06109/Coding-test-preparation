# Programmers 조이스틱
# 굳이 인덱스를 앞으로 뒤로 옮기지 않고 문자열 순서대로 탐색하는 것을 기본으로하고
# 처음 A가 나왔을 때만 cnt를 알맞게 변경해주는 방식 시도함
# 실패...
name = input()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cnt = 0 # 조이스틱 조작 횟수\
first = True # A를 처음 만나는가?

for i in range(len(name)):
    letter = name[i]
    idx = alphabet.index(letter)
    if letter == "A" and first: # 거꾸로가기
            cnt += i - 2 # 문자열 마지막으로 가는 데 필요한 조작횟수
            first = False
    else:
        if idx > 12: # 알파벳 뒤에부터 찾는 게 최소횟수
            cnt += 26 - idx
        else:
            cnt += idx
    cnt += 1
print(cnt - 1)\
    
# https://bellog.tistory.com/152
# A가 여러 개일 경우, 여러 A가 연속적으로 붙어있을 경우를 생각하지 않음 