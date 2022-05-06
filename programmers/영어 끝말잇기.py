def solution(n, words):
    answer = [1, 1]
    w = words.pop(0)
    his = [w]
    while words:
        if answer[0] == n:
            answer[0] = 1
            answer[1] += 1
        else:
            answer[0] += 1
        if w[-1] != words[0][0]:
            return answer
        else:
            w = words.pop(0)
            if w in his:
                return answer
            else:
                his.append(w)     
    return [0,0]

    """
    def solution(n, words):
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1] or words[i] in words[:i]:
            print(words[:i])
            return [(i%n)+1, (i//n)+1]
    return [0, 0]
    """