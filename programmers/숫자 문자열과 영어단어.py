def solution(s):
    nums= {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 
           'six':'6', 'seven':'7', 'eight':'8', 'nine':'9', 'zero':'0'}
    n = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    k = ''
    answer = ''
    for i in s:
        if i in n:
            answer += i
        else:
            k += i
            if k in nums.keys():
                answer += nums[k]
                k = ''
    
    return int(answer)