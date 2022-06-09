import sys
n = int(input())
card = sys.stdin.readline

cards = set(map(int, card().split()))

m = int(input())
card2 = sys.stdin.readline
cards2 = list(map(int, card2().split()))

for c in cards2:
        print(1, end = " ") if c in cards else print(0, end=" ")