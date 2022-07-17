import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    v = list(map(int, input().split()))
    start, end = (v[0], v[1]), (v[2], v[3])

    n = int(input())
    count = 0
    for _ in range(n):
        cx, cy, r = map(int, input().split())
        dis1 = ((start[0] - cx)**2 + (start[1] - cy)**2)**0.5
        dis2 = ((end[0] - cx)**2 + (end[1] - cy)**2)**0.5
        if dis1 < r and dis2 < r:
            pass
        elif dis1 < r:
            count += 1
        elif dis2 < r:
            count += 1
    print(count)
    # start, end 가 각각 원 안에 있는가? 그러면 진입/이탈을 해야함.
    # 만약 도착점과 출발점이 모두 원 내부에 있다면 그것도 0!!!!