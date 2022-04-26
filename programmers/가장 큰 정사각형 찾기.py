def solution(board):
    answer = 0
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 1: # 1이라면
                board[i][j] += min(board[i-1][j-1], board[i-1][j], board[i][j-1])
                
    for b in board:
        m = max(b)
        answer = max(m, answer)
        
    return answer**2