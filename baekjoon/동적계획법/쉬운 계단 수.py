import sys
input = sys.stdin.readline
n = int(input())
dp = [[0] * 10 for _ in range(n+1)]
# dp[자리수][앞에 오는 수]
for i in range(1, 10):
    dp[1][i] = 1 # 한자리 수들은 모두 한가지 경우 이므로

for i in range(2, n+1):
    for j in range(10):
        # 0 앞 뒤에는 1이, 9 앞 뒤에는 8만 올 수 있다.
        if j == 0: 
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n]) % 1000000000)