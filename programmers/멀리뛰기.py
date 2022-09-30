def solution(n):
    dp = [0] * (n+1)
    if n == 1:
        return 1
    if n == 2:
        return 2
        
    dp[1] = 1
    dp[2] = 2
    
    for t in range(3, n+1):
        dp[t] = dp[t-1] + dp[t-2]
    
    return dp[n]%1234567