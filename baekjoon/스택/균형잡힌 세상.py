import sys
input = sys.stdin.readline

while True:
    stack = []
    string = input().rstrip()
    if string == '.':
        break
    string = string.replace(" ", "")
    for s in string:
        if s == '(':
            stack.append(0)
        elif s == ')':
            if not stack or stack[-1] != 0:
                print('no')
                break
            else:
                stack.pop()
        elif s == '[':
            stack.append(1)
        elif s == ']':
            if not stack or stack[-1] != 1:
                print('no')
                break
            else:
                stack.pop()
    else: print('yes') if len(stack) == 0 else print('no')
    