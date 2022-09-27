def solution(s):
    # replace 함수를 사용하면 시간복잡도 커짐
    # 문자열을 stack에 하나씩 넣으면서 스택의 마지막 요소와 동일하면 pop
    # -> 시간복잡도 O(1)으로 문제를 처리할 수 있음
    stack = []
    for letter in s:
        if len(stack) == 0:
            stack.append(letter)
        elif stack[-1] == letter:
            stack.pop()
        else:
            stack.append(letter)
            
    result = 0
    if len(stack) == 0:
        result = 1
        
    return result