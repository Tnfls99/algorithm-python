import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
table = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        table[i][j] = line[j]

combination = list(combinations([i for i in range(n)], n//2))

answer = 123456789

for i in range(len(combination)//2):
    k = len(combination)-1 - i
    s = combination[i]
    l = combination[k]

    combi_s = combinations(s, 2)
    combi_l = combinations(l, 2)
    start, link = 0, 0
    for com in combi_s:
        start += table[com[0]][com[1]] + table[com[1]][com[0]]

    for com in combi_l:
        link += table[com[0]][com[1]] + + table[com[1]][com[0]]

    if start >= link :
        if answer > (start - link):
            answer = start - link
    else:
        if answer > (link - start):
            answer = link - start

print(answer)