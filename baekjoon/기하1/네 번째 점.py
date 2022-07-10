import sys
input = sys.stdin.readline

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
x4, y4 = 0 , 0
x = set([x1, x2, x3])
y = set([y1, y2, y3])

x_2 = [x1, x2, x3]
y_2 = [y1, y2, y3]

for t in x:
    if x_2.count(t) != 2:
        x4 = t
    
for t in y:
    if y_2.count(t) != 2:
        y4 = t
print(f'{x4} {y4}')