import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
queue = deque()
for i in range(1, n+1):
    queue.append(i)
k = k - 1
print('<', end="")
while True:
    for _ in range(k):
        i = queue.popleft()
        queue.append(i)
    print(queue.popleft(), end="")
    if len(queue) == 0:
        break
    print(', ', end="")
print('>')