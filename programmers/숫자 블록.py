def solution(begin, end):
    road = []
    MAX = 10000000
    
    for num in range(begin, end+1):
        if num == 1:
            road.append(0)
        else:
            start = 2 if num % 2 == 0 else 3
            road.append(1)
            # 각 구간의 블록값은 위치값의 가장 큰 약수 = 1이 아닌 가장 작은 약수로 나눈 몫 -> 약수값을 구하기 위해 중간값 이용
            for i in range(start, int(num**0.5)+1):
                if num != i and num% i == 0:
                    if num//i <= MAX: # 제일 중요한 부분 -> 문제를 잘 읽어야만 보이는 조건임.
                        road[-1] = num//i
                        break
    return road