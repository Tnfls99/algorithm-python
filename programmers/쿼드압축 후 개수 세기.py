def rectangle(a, b, l, arr, result):
    start = arr[a][b]
    for i in range(a, a+l):
        for j in range(b, b+l):
            if arr[i][j] != start:
                l = l // 2
                rectangle(a, b, l, arr, result)
                rectangle(a, b+l, l, arr, result)
                rectangle(a+l, b, l, arr, result)
                rectangle(a+l, b+l, l, arr, result)
                return
                
    result[start] += 1

def solution(arr):
    result = [0, 0]
    rectangle(0, 0, len(arr), arr, result)
    
    return result

# 아직도 재귀가 어렵다,,,,,,, 재귀 겁내지 말기,,,,,^^