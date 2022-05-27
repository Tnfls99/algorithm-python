def solution(N, stages):
    fail_rate = []

    for i in range(1, N+1):
        p = len([1 for x in stages if x >= i])
        f = stages.count(i)
        
        if p == 0:
            fail_rate.append((i, 0))
        else:
            fail_rate.append((i, f/p))
        
        
    return [x[0] for x in sorted(fail_rate, key=lambda x : x[1], reverse=True)]