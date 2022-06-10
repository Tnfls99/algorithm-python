import sys
input = sys.stdin.readline
n, m = map(int, input().split())

not_heard = set(input().rstrip() for _ in range(n))
not_seen = set(input().rstrip() for _ in range(m))

answer = sorted(list(not_heard & not_seen))

print(len(answer))
for i in answer:
    print(i)