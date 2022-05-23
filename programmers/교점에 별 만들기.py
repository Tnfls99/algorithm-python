from itertools import combinations
def meet(line1, line2):
    a, b, e = line1[0], line1[1], line1[2]
    c, d, f = line2[0], line2[1], line2[2]
    
    if (a*d - b*c) == 0:
        return
    elif (b*f - e*d)%(a*d - b*c) != 0 or (e*c - a*f)%(a*d - b*c) != 0:
        return
    
    return [(b*f - e*d)//(a*d - b*c), (e*c - a*f)//(a*d - b*c)]
    

def solution(line):
    products = list(combinations(line, 2))
    meets = sorted([meet(p[0], p[1]) for p in products if meet(p[0], p[1]) is not None], key=lambda x:x[1], reverse=True)
    
    x = [m[0] for m in meets]
    mnx = min(x)
    mxx = max(x)
    
    y = [m[1] for m in meets]
    mny = min(y)
    mxy = max(y)
    
    answer = ['.' * ((mxx-mnx) + 1)] * ((mxy-mny) + 1)
    
    for m in meets:
        x,y = m
        answer[mxy-y] = answer[mxy-y][:x-mnx] + '*' + answer[mxy-y][x-mnx+1:]
        
    return [''.join(ans) for ans in answer]
            
    
            