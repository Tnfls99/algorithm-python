from itertools import permutations

def is_prime(n):
    sq = int(n ** 0.5) + 1
    if n < 2:
        return False
    for i in range(2, sq):
        if n % i == 0:
            return False
    return True

def solution(numbers):
    numbers = [i for i in numbers]
    new_nums = []
    answer = 0
    for i in range(1, len(numbers)+1):
        new_nums += set([int(''.join(n)) for n in list(permutations(numbers, i))])
        
    for n in set(new_nums):
        if is_prime(n):
            answer += 1
    
    return answer