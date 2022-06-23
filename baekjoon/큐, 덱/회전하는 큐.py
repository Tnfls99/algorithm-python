import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
queue = deque([i for i in range(1, n+1)])
count = 0
location = list(map(int, input().split()))

for l in location:
    while True:
        if queue[0] == l:
            queue.popleft()
            break
        else:
            if queue.index(l) < len(queue)/2:
                while queue[0] != l:
                    queue.append(queue.popleft())
                    count += 1
            else:
                while queue[0] != l:
                    queue.appendleft(queue.pop())
                    count += 1

print(count)