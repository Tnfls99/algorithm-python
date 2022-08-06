import sys
input = sys.stdin.readline
n = int(input())
glass = [int(input()) for _ in range(n)]
if n == 1 :
    print(glass[0])
elif n == 2:
    print(sum(glass))
else:
    dp = [0] * (n+1)
    dp[1] = glass[0]
    dp[2] = glass[0] + glass[1]
    dp[3] = max(dp[2], glass[0] + glass[2], glass[1] + glass[2])
    for i in range(4, n+1):
        dp[i] = max(dp[i-1], glass[i-2]+ glass[i-1]+dp[i-3], glass[i-1]+dp[i-2])
    print(dp[-1])