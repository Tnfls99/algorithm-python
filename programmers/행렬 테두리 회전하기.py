def solution(rows, columns, queries):
    answer = []
    l = [[0 for i in range(columns+1)] for j in range(rows+1)]
    num = 1
    for row in range(1, rows+1):
        for column in range(1, columns+1):
            l[row][column] = num
            num += 1

    for x1, y1, x2, y2 in queries:
        ans = l[x1][y1]
        tmp = ans
        # 좌측부터 시작해야 첫번째 값 보존 가능?! 
        for k in range(x1,x2):
            test = l[k+1][y1]
            l[k][y1] = test
            ans = min(ans, test)

        for k in range(y1,y2):
            test = l[x2][k+1]
            l[x2][k] = test
            ans = min(ans, test)

        for k in range(x2,x1,-1):
            test = l[k-1][y2]
            l[k][y2] = test
            ans = min(ans, test)

        for k in range(y2,y1,-1):
            test = l[x1][k-1]
            l[x1][k] = test
            ans = min(ans, test)

        l[x1][y1+1] = tmp
        answer.append(ans)
    
    return answer
            
                    