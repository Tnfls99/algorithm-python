import sys
input = sys.stdin.readline

n = int(input())
length = list(map(int, input().split()))
prices = list(map(int, input().split()))

price = 0
p = prices[0]

for i in range(n-1):
    if prices[i] < p:
        p = prices[i]
    price += p * length[i]

print(price)