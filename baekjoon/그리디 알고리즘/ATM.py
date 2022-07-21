import sys
input = sys.stdin.readline
n= int(input())
p = sorted(list(map(int, input().split())))

time = [0] * n
for i, t in enumerate(p):
    if i != 0:
        time[i] = time[i-1] + t
    else:
        time[i] = t

print(sum(time))