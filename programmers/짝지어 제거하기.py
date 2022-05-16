def solution(s):
    stack = []
    for i in s:
        if len(stack) > 0 and stack[-1] == i:
            stack.pop()
            continue
        stack.append(i)
    return 0 if len(stack) else 1