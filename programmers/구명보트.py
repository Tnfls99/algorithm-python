# limit = 구명보트 한개당 최대 무게
# 구명보트 최소 개수 리턴
# 구명보트에는 한번에 두명만 탈 수 있음
from collections import deque
def solution(people, limit):
    answer = 0
    people = sorted(people)
    start = 0
    end = len(people)-1
    
    while start <= end:
        answer += 1
        if people[start] + people[end] <= limit:
            start += 1
        end -= 1
    return answer