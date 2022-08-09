# LIS(Longest Increasing Subsequence)를 구하는 문제

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n # 자신보다 작은 수열 값의 개수를 저장하는 리스트

for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[j]+1, dp[i])
            # j 번째 수열값보다 i번째 수열값이 크면, 
            # j 위치의 개수에 1개를 더한 것과 현재 자신의 갯수와 비교해서 큰 값을 저장 
            # 결국 j번째 값을 가져오게 되면 값의 오름차순도 지켜지며 갯수가 누적된다.

print(max(dp))