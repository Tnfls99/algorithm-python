# LIS 응용문제 1
import sys
input = sys.stdin.readline

# 바이토닉 수열인지 판단하고, 가장 긴 수열의 길이 출력

n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n
answer = [0] * n

for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[j]+1, dp[i])

arr.reverse()

rdp = [1] * n
for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            rdp[i] = max(rdp[j]+1, rdp[i])
rdp.reverse()
for i in range(n):
    answer[i] = dp[i] + rdp[i] - 1

print(max(answer))

