def chess_board(m, n, board):
    answers = []

    for i in range(n-7):
        for j in range(m-7):
            cnt = 0
            idx = 0
            for k in range(i, i+8):
                for l in range(j, j+8):
                    if idx % 2 == 0:
                        if board[k][l] != 'W':
                            cnt += 1
                    else:
                        if board[k][l] != 'B':
                            cnt += 1
                    if l != j + 7:
                        idx += 1

            answers.append(min(cnt, 64-cnt))
    print(min(answers))

n, m = map(int, input().split())
board = [[' ' for _ in range(m)] for _ in range(n)]

for i in range(n):
    line = input()
    for j in range(m):
        board[i][j] = line[j]


chess_board(m, n, board)