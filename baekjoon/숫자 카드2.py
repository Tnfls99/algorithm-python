import sys
n = int(input())
card = sys.stdin.readline

cards = list(map(int, card().split()))
d = {}
for c in cards:
    if c in d.keys():
        d[c] += 1
    else:
        d[c] = 1
m = int(input())
card2 = sys.stdin.readline
cards2 = list(map(int, card2().split()))

for c in cards2:
    if c in d.keys():
        print(d[c], end= " ")
    else:
        print(0, end=" ")