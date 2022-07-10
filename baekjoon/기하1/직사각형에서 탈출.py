import sys
input = sys.stdin.readline
x, y, w, h = map(int, input().split())

# 경계선에 있으려면 x=0, 0 <= y <= h / y = 0, 0 <= x <= w / y = h, 0 <= x <= w / x = w, 0 <= y <= h
length = []

if 0 <= x <= w:
    length.append(abs(0-y))
    length.append(abs(h-y))

if 0 <= y <= h:
    length.append(abs(0-x))
    length.append(abs(w-x))

print(min(length))