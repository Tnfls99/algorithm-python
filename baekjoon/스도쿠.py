import sys
input = sys.stdin.readline

sudoku = []
for _ in range(9):
    tmp = list(map(int, input().split()))
    sudoku.append(tmp)

zeros = [[i, j] for i in range(9) for j in range(9) if sudoku[i][j] == 0]

def in_nums(i, j):
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    for k in range(9):
        if sudoku[i][k] in nums:
            nums.remove(sudoku[i][k])
        if sudoku[k][j] in nums:
            nums.remove(sudoku[k][j])
    i //= 3
    j //= 3
    for p in range(i * 3, (i + 1) * 3):
        for q in range(j * 3, (j + 1) * 3):
            if sudoku[p][q] in nums:
                nums.remove(sudoku[p][q])
    return nums
flag = False
def dfs(idx):
    global flag
    if flag:
        return
    if idx == len(zeros):
        for row in sudoku:
            print(*row)
        flag = True
        return
    else:
        (i, j) = zeros[idx]
        nums = in_nums(i, j)
        for num in nums:
            sudoku[i][j] = num
            dfs(idx+1)
            sudoku[i][j] = 0

dfs(0)
#print(sudoku)