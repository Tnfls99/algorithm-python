# 메모제이션으로 N을 1로 바꾸기 위해 주어진 연산을 몇 번 사용하는지 계산하는 문제

import sys
input = sys.stdin.readline

n = int(input())
nums = [0] * (n+1)

for i in range(2, n+1):
    nums[i] = nums[i-1] + 1

    if i % 2 == 0:
        nums[i] = min(nums[i], nums[i//2]+1)
    if i % 3 == 0:
        nums[i] = min(nums[i], nums[i//3]+1)

print(nums[n])