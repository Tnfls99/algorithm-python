def solution(board, moves):
    board2 = [[board[j][i] for j in range(len(board))] for i in range(len(board))]
    
    for i, b in enumerate(board2):
        board2[i] = list(filter(lambda x : x > 0, b))
    
    dolls = []
    cnt = 0
    for m in moves:
        if board2[m-1]:
            doll = board2[m-1].pop(0)
            if dolls and dolls[len(dolls)-1] == doll:
                dolls.pop()
                cnt+=2
            else:
                dolls.append(doll)
    return cnt