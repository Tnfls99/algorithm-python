def solution(s):
    array = []
    for k in s:
        if k == "(":
            array.append(0)    
        elif k == ")":
            if array == []:
                return False
            array.pop()
    
    return len(array) == 0