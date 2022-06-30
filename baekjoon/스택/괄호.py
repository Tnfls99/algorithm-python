import sys
input = sys.stdin.readline

t = int(input())

def func(string):
    stack = []
    for s in string:
        if s == '(':
            stack.append(0)
        elif s == ')':
            if not stack:
                return False
            else: stack.pop()
    return len(stack) == 0

for _ in range(t):
    string = input()
    if func(string):
        print('YES')
    else: print('NO')