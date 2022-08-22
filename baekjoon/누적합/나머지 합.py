import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))
sum_arr = [0 for _ in range(m)]

for i in range(1, n+1):
    arr[i] += arr[i-1]
    sum_arr[arr[i] % m] += 1

ans = sum_arr[0]

for i in sum_arr:
    ans += i*(i-1) // 2

print(ans)