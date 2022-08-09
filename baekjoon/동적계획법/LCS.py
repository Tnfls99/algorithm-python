import sys
input = sys.stdin.readline

s1 = [0] + list(input().rstrip())
s2 = [0] + list(input().rstrip())

dp = [[0] * (len(s1)+1) for _ in range(len(s2)+1)]

for i in range(1, len(s2)):
    for j in range(1, len(s1)):
        if s2[i] == s1[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
answer = 0
for i in dp:
    answer = max(max(i), answer)
print(answer)