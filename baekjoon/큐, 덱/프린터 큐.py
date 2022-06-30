import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    priority = list((map(int, input().split())))
    priority = deque([(i, idx) for idx, i in enumerate(priority)])
    count = 0
    while priority:
        if priority[0][0] != max(priority)[0]:
            priority.append(priority.popleft())
        else:
            pop = priority.popleft()
            count += 1
            if pop[1] == m:
                print(count)
                break