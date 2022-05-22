import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
queue = deque()
for i in range(1, n+1):
    queue.append(i)
while True:
    # throw out
    if len(queue) > 1:
        queue.popleft()
    else:
        print(queue[0])
        break
    # first to back
    if len(queue) > 1:
        k = queue.popleft()
        queue.append(k)
    else:
        print(queue[0])
        break