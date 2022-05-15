def solution(n,a,b):
    a, b = min(a, b), max(a,b)
    for i in range(1, n//2+1):
        if b-a == 1 and b % 2 == 0:
            return i
        else:
            b = b//2 if b % 2 == 0 else b//2 + 1
            a = a//2 if a % 2 == 0 else a//2 + 1