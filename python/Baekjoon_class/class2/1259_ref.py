import sys
input = sys.stdin.readline

while True:
    case = input().rstrip()
    if case == '0': break

    reverse = case[::-1]
    if case == reverse:
        print('yes')
    else:
        print('no')

# reverse 이용해서 원본이랑 같으면 yes 반환하면됨
