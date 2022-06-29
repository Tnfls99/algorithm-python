import sys
input = sys.stdin.readline
n = int(input())
stack = []
for _ in range(n):
    command = input().rstrip()
    if 'push' in command:
        command, num = command.split()
        stack.append(int(num))

    elif command == 'size':
        print(len(stack))
    
    elif command == 'pop':
        if not stack:
            print(-1)
        else: print(stack.pop())
    
    elif command == 'empty':
        if not stack:
            print(1)
        else: print(0)

    elif command == 'top':
        if not stack:
            print(-1)
        else: print(stack[-1])