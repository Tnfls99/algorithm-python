# 각 층의 모든 칸마다 최댓값을 저장하면서 동적 계획법으로 푸는 문제

import sys
input = sys.stdin.readline
n = int(input())
triangle = []
for _ in range(n):
    triangle.append(list(map(int, input().split())))
cur = 0
answer = triangle[0][0]
for i in range(1, n):
    for j in range(len(triangle[i])):
        if j == 0:
            triangle[i][j] = triangle[i-1][j] + triangle[i][j]
        elif j == len(triangle[i])-1:
            triangle[i][j] = triangle[i-1][j-1] + triangle[i][j]
        else:
            triangle[i][j] = max(triangle[i-1][j] + triangle[i][j], triangle[i-1][j-1] + triangle[i][j])

print(max(triangle[-1]))