import sys
input = sys.stdin.readline
line = input().split('-')
s = 0

for i in line[0].split('+'):
    s += int(i)

for i in line[1:]:
    for j in i.split('+'):
        s -= int(j)

print(s)