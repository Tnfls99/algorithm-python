def dfs(chess, row, n):
    count = 0
    if row == n:
        # 타고타고 들어가서 row가 n 과 같아지면 모든 퀸을 다 뒀다는 의미
        return 1
    for col in range(n):
        #chess[row][col] 위치에 퀸을 두겠다.
        chess[row] = col
        # 퀸을 위에서부터 두고 있으므로 아레는 볼 필요 없이 오른쪽, 왼쪽 위 대각선만 보면 됨.
        for i in range(row):
            if chess[i] == chess[row]:
                break
            if abs(chess[i]-chess[row]) == row - i:
                break
        #break 되지 않으면 실행된다. -> 퀸을 놓을 수 있는 자리라는 뜻 
        else:
            count += dfs(chess, row+1, n)            
    return count
            

def solution(n):
    return dfs([0]*n, 0, n)