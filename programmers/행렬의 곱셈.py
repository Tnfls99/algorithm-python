def solution(arr1, arr2):
    rev = [[arr2[j][i] for j in range(len(arr2))] for i in range(len(arr2[0]))]
    answer = []
    
    for a1 in arr1:
        array = []
        for re in rev:
            array.append(sum([a1[i]*re[i] for i in range(len(re))]))
        answer.append(array)
        
    return answer