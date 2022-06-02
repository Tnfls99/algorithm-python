def J(arr1, arr2):
    # 교집합
    inter = []
    arr2_copy = arr2.copy()
    for a1 in arr1:
        if a1 in arr2_copy:
            inter.append(a1)
            arr2_copy.remove(a1)
    
    # 합집합
    union = arr1.copy()
    arr1_copy = arr1.copy()
    
    for a2 in arr2:
        if a2 not in arr1_copy:
            union.append(a2)
        else:
            arr1_copy.remove(a2)
    
    
    if union == []:
        return 65536
    
    return int((len(inter) / len(union)) * 65536)

def solution(str1, str2):
    arr1, arr2 = [], []
    for i in range(0, len(str1)-1):
        t1 = str1.lower()[i]
        t2 = str1.lower()[i+1]
        if t1.isalpha() and t2.isalpha():
            arr1.append(t1+t2)
        
    for i in range(0, len(str2)-1):
        t1 = str2.lower()[i]
        t2 = str2.lower()[i+1]
        if t1.isalpha() and t2.isalpha():
            arr2.append(t1+t2)
    
    return J(arr1, arr2)