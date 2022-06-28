import sys

# V: 마을 갯수, E: 도로 갯수
V, E = map(int, sys.stdin.readline().split())

INF = int(1e9)
arr = [[INF for _ in range(V+1)] for _ in range(V+1)]

for _ in range(E):
    i, j, c = map(int, sys.stdin.readline().split())
    arr[i][j] = c

for k in range(1, V+1):
    for i in range(1, V+1):  # from
        for j in range(1, V+1):  # to
            arr[i][j] = min(arr[i][j], arr[i][k] + arr[k][j])

result = INF
#  계속 갱신한 뒤 사이클은 본인부터 본인까지에 저장됨
for i in range(1, V+1):
    result = min(result, arr[i][i])

if result == INF:
    print(-1)
else:
    print(result)