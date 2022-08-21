import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
sum_arr = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(1, n+1):
    for j in range(1, n+1):
        # sum_arr[i-1][j-1] 중복되는 것 빼는 거 잊지 말기 !!!!
        sum_arr[i][j] = sum_arr[i-1][j] + sum_arr[i][j-1] + arr[i-1][j-1] - sum_arr[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    # 인덱스 에러 난 이유?
        # 각각 주어지는 값이 행렬 값이고 0보다 큰 자연수로 주어지기 때문에 그대로 활용하면 됨.
    print(sum_arr[x2][y2] - sum_arr[x2][y1-1] - sum_arr[x1-1][y2] + sum_arr[x1-1][y1-1])