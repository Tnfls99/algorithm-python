import sys
input = sys.stdin.readline

n, k = map(int, input().split())
w = [int(input()) for _ in range(n)]
count = 0
for i in w[::-1]:
    count += k//i
    k = k%i
print(count)