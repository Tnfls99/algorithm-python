from itertools import product
def solution(word):
    answer = 0
    p = []
    for c in range(1, 6):
        p.extend(''.join(p) for p in list(product(['A', 'E', 'I', 'O', 'U'], repeat=c)))
    
    return sorted(p).index(word) + 1