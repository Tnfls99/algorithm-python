import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
sum_arr = [0 for _ in range(n+1)]

for i in range(1, n+1):
    sum_arr[i] = sum_arr[i-1] + nums[i-1]

for _ in range(m):
    i, j = map(int, input().split())

    print(sum_arr[j] - sum_arr[i-1])