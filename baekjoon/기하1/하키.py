import sys
input = sys.stdin.readline
w, h, x, y, p = map(int, input().split())
r = h/2
count = 0

for _ in range(p):
    px, py = map(int, input().split())
    # rec
    if x <= px <= x+w and y <= py <= y+h:
        count += 1
    # circle
    elif (abs(px-x)**2 + abs(py-(y+r))**2)**0.5 <= r:
        count += 1
    elif (abs(px-(x+w))**2 + abs(py-(y+r))**2)**0.5 <= r:
        count += 1

print(count)