# lower, number, -, _, .
# . 은 처음과 끝에 사용 불가능, 연속 사용 불가능

#### 정규식으로 바꿔서 풀이해보기 ###
def solution(new_id):
    #1
    new_id = new_id.lower()
    #2
    new_id = [i for i in new_id if i.isdigit() or i.isalpha() or i in ['-', '_', '.']]
    #3
    is_period = False
    for i, d in enumerate(new_id):
        if is_period and d == '.':
            new_id[i] = ""
        if d =='.':
            is_period = True
        else:
            is_period = False
    new_id = list(''.join(new_id)) # 빈칸 없애주기
    #4
    while new_id != [] and new_id[0] == '.':
        new_id.pop(0)
    while new_id != [] and new_id[-1] == '.':
        new_id.pop()
    
    #5
    if new_id == []:
        new_id.append('a')
    #6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        while new_id != [] and new_id[-1] == '.':
            new_id.pop()
    #7
    elif len(new_id) <= 2:
        while len(new_id) <= 2:
            new_id.append(new_id[-1])
        
    return ''.join(new_id)