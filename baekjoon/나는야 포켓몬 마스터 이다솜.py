import sys
input = sys.stdin.readline
n, m = map(int, input().split())

mm = [input() for _ in range(n)]
d1 = {k+1:v.rstrip() for k, v in enumerate(mm)}
d2 = {k.rstrip():v+1 for v,k in enumerate(mm)}

pp = [input() for _ in range(m)]

for p in pp:
    p = p.rstrip()
    if p.isdigit():
        print(d1[int(p)])
    else:
        print(d2[p])