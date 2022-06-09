import sys
input = sys.stdin.readline

n,m = map(int, input().split())
sets = set([input() for _ in range(n)])
strings = [input() for _ in range(m)]
count = 0
for s in strings:
    if s in sets:
        count += 1

print(count)