import sys
input = sys.stdin.readline
from collections import deque
# 반드시 오름차순으로 푸시할 수 있음
# 8을 푸시하려면 1~7까지 푸시하고 8을 푸시할 수 있음
n = int(input())
cur = 1
stack = []
answer = []
for _ in range(n):
    k = int(input())
    while cur <= k:
        stack.append(cur)
        answer.append('+')
        cur += 1
    
    if stack[-1] == k:
        stack.pop()
        answer.append('-')
    else:
        print('NO')
        break
else:
    for i in answer:
        print(i)