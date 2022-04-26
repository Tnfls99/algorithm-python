# 인쇄 대기 목록에서 가장 앞것 꺼냄
# 나머지 대기 목록에서 우선순위 높은 게 있으면 꺼낸 건 대기목록 맨 뒤로
# 아니면 꺼낸 거 인쇄
# 우선순위는 숫자가 클수록 높은거
def solution(priorities, location):
    answer = []
    
    priorities = [(p, i) for i, p in enumerate(priorities)]
    
    while priorities:
        task = priorities.pop(0)    
        if priorities and max(priorities)[0] > task[0]:
            priorities.append(task)
            
        else:
            answer.append(task)
            if task[1] == location:
                return len(answer)