from collections import deque
def check(s):
    stack = []
    for w in s:
        if w == '[' or w == '{' or w == '(':
            stack.append(w)
        else:
            if not stack:
                return False
            x = stack.pop()
            if w == ')' and x != '(':
                return False
            if w == '{' and x != '}':
                return False
            if w == '[' and x != ']':
                return False
    return len(stack) == 0
def solution(s):
    answer = 0
    s = deque(s)
    for _ in range(len(s)):
        s.rotate(-1)
        if check(s):
            answer += 1
    return answer