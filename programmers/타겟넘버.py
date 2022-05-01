def solution(numbers, target):
    array = []
    for num in numbers:
        if array == []:
            array = [num, -num]
        else:
            tmp = []
            for x in array:
                tmp.append(x+num)
                tmp.append(x-num)
            array = tmp

    return array.count(target)