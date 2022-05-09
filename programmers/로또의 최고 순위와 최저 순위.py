def solution(lottos, win_nums):
    z = lottos.count(0)
    if z == 0:
        answer = 7 - len([i for i in lottos if i in win_nums])
        return [answer, answer] if not answer == 7 else [6, 6]
    
    cnt = 0
    for w in win_nums:
        if w in lottos:
            cnt += 1
    
    return [7-cnt-z, 7-cnt if cnt > 0 else 6]