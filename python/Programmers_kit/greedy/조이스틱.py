# Programmers 조이스틱
# 실패...
name = input()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
index = 0 # name의 index
cnt = 0 # 조이스틱 조작 횟수
visit = [False] * len(name)
back = False

while (False in visit):
    if index == -1:
        index = len(name) - 1
    if not visit[index]: # 방문한 적이 없다면?
        letter = name[index]
        idx = alphabet.index(letter)
        if letter == "A" and not back: # 거꾸로가기
            cnt -= 3 # 문자열 마지막으로 가는 데 필요한 조작횟수
            visit[index] = True
            index = len(name) - 1 # 문자열 마지막으로 가기
            back = True
        else:
            if idx > 12: # 알파벳 뒤에부터 찾는 게 최소횟수
                cnt += 26 - idx
            else:
                cnt += idx
            visit[index] = True
        
    if back:
        index -= 1
    else:
        index += 1 
    cnt += 1 # 좌우로 움직이는거?

answer = cnt

print(cnt-1)