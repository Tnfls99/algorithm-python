from itertools import permutations
def solution(k, dungeons):
    p = list(permutations(dungeons))
    answer = 0
    for i in p:
        piro = k
        count = 0
        for j in i:
            if j[0] <= piro:
                piro -= j[1]
                count += 1
        if count > answer:
            answer = count
    return answer