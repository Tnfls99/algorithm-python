import sys
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
sum_arr = [0 for _ in range(n+1)]
answer = []

for i in range(1, n+1):
    sum_arr[i] = sum_arr[i-1] + arr[i-1]

for i in range(k, n+1):
    answer.append(sum_arr[i] - sum_arr[i-k])

print(max(answer))