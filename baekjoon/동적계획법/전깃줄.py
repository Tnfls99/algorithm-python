import sys
input = sys.stdin.readline

n = int(input())
line = [0] * 501
dp = [0] * 501

for _ in range(n):
    s, e = map(int, input().split())
    line[s] = e

for i in range(501):
    for j in range(i):
        if line[j] < line[i]:
            dp[i] = max(dp[j]+1, dp[i])

print(n - max(dp))