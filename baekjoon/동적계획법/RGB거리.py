#i번째 집을 각각의 색으로 칠할 때 1~i번째 집을 모두 칠하는 최소 비용으로 부분문제를 정의해봅시다.

import sys
input = sys.stdin.readline
n = int(input())
costs = []
for _ in range(n):
    costs.append(list(map(int, input().split())))

for i in range(1, n):
    costs[i][0] = min(costs[i-1][1], costs[i-1][2]) + costs[i][0]
    costs[i][1] = min(costs[i-1][0], costs[i-1][2]) + costs[i][1]
    costs[i][2] = min(costs[i-1][0], costs[i-1][1]) + costs[i][2]

print(min(costs[n-1]))