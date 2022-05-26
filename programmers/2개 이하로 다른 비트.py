def f(num):
    if num % 2 == 0:
        return num+1
    else:
        n = '0' + bin(num)[2:]
        idx = n.rfind('0')
        n = list(n)
        n[idx] = '1'
        n[idx+1] = '0'
        return int(''.join(n), 2)

def solution(numbers):
    return [f(n) for n in numbers]