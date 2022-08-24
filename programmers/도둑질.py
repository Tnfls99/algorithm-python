def solution(money):
    dp1 = [0 for _ in range(len(money))]
    dp2 = [0 for _ in range(len(money))]
    
    dp1[1] = money[0]
    dp1[2] = max(dp1[1], money[1])
    
    for i in range(3, len(money)):
        dp1[i] = max(dp1[i-2]+money[i-1], dp1[i-1], dp1[i-3]+money[i-1])

    
    money.reverse()
    dp2[1] = money[0]
    dp2[2] = max(dp2[1], money[1])

    
    for i in range(3, len(money)):
        dp2[i] = max(dp2[i-2]+money[i-1], dp2[i-1], dp2[i-3]+money[i-1])
    
    
    return max(max(dp1), max(dp2))