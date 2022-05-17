def solution(n):
    answer = [[0]*i for i in range(1, n+1)]
    x, y = -1, 0
    num = 1
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            else:
                x -= 1
                y -= 1
            answer[x][y] = num
            num += 1
    
    return sum(answer, [])
    # 로직 떠올리는게 너무 어려웠음. 아직도 어려움.