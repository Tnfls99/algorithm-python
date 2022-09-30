answer = []

def hanoi(n, f, t, aux):
    if n == 1:
        answer.append([f, t])
        return
    hanoi(n-1, f, aux, t)
    
    answer.append([f, t])
    
    hanoi(n-1, aux, t, f)

def solution(n):
    hanoi(n, 1, 3, 2)
    return answer