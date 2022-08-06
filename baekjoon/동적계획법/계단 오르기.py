# i번째 계단에 오를 때, 몇 개의 연속한 계단을 올랐는지를 고려하여 부분문제를 정의해봅시다.

import sys
input = sys.stdin.readline

n = int(input())
w = [int(input()) for _ in range(n)]
dp = []
# 계단의 수가 300이하 자연수이므로 계단이 1개 2개일때도 존재 -> 예외처리 해줘야함!!
if n == 1:
    print(w[0])
elif n == 2:
    print(sum(w))
else:
    dp.append(w[0])
    dp.append(max(w[0] + w[1], w[1]))
    dp.append(max(w[0] + w[2], w[1]+ w[2]))

    for i in range(3, n):
        dp.append(max(dp[i-2] + w[i], dp[i-3] + w[i] + w[i-1]))

    print(dp[-1])