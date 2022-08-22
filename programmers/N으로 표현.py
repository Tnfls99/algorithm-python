def calculate(X, Y):
    tmp = set()
    
    for x in X:
        for y in Y:
            tmp.add(x + y)
            tmp.add(x * y)
            tmp.add(x - y)
            if y != 0:
                tmp.add(x // y)
    return tmp

def solution(N, number):
    dp = {}
    dp[1] = {N}
    if number == N:
        return 1
    for i in range(2, 9):
        dp[i] = {int(str(N)*i)}
        for j in range(1, i):
            dp[i].update(calculate(dp[j], dp[i-j]))
        
        if number in dp[i]:
            return i
    return -1