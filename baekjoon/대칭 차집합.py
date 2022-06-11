import sys
input = sys.stdin.readline

a, b = map(int, input().split())
aa = sys.stdin.readline
bb = sys.stdin.readline
A = set(list(map(int, aa().split())))
B = set(list(map(int, bb().split())))
print(len(A^B))