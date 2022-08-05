# 동적 계획법으로 합이 최대인 부분 배열을 구하는 문제
# 규칙을 찾고 수여리 주어졌을 때 DP 배열을 구성할 똑같은 크기의 수열이 필요하다는 점이 중요하다?

import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
dp = [0] * len(nums)
dp[0] = nums[0]

for i in range(1, len(nums)):
    # 이전의 연속된 숫자의 합 중 가장 큰 것을 저장해둠으로 가져와서 계산하면 됨...
    dp[i] = max(nums[i], dp[i-1] + nums[i])

print(max(dp))