from itertools import combinations
def solution(clothes):
    answer = 1
    kinds = set([c[1] for c in clothes])
    
    array = {k:[] for k in kinds}
    for c in clothes:
        array[c[1]].append(c[0])
    
    for k in kinds:
        cnt = len(array[k])
        answer *= (cnt+1)
    
    
    
    return answer-1