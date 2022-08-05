# 피보나치 수와 비슷한 규칙을 찾아 동적 계획법으로 푸는 문제

# 1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12, 16

# 16 = 12 + 4
# 12 = 9 + 3
# 9 = 7 + 2
# 7 = 5 + 2
# 5 = 4 + 1
# 4 = 3 + 1
# 3 = 2 + 1
# 2 = 1 + 1

import sys
input = sys.stdin.readline

T = int(input())

answer = [0] * 101
answer[1] = 1
answer[2] = 1
answer[3] = 1
answer[4] = 2
answer[5] = 2
for i in range(6, 101):
    answer[i] = answer[i-1] + answer[i-5]


for _ in range(T):
    n = int(input())
    print(answer[n])