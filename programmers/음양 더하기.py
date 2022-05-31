def solution(absolutes, signs):
        
    return sum([k if s else -k for k, s in zip(absolutes, signs)])