def whosBig(people):
    for per in people:
        bigger = 0
        for p in people:
            if per == p : continue
            if per[0] < p[0] and per[1] < p[1]:
                bigger += 1
        people[people.index(per)].append(bigger+1)


# 입력 받기
n = int(input())
people = []
for i in range(0, n):
    w, h = map(int, input().split())
    people.append([w, h])

whosBig(people)

for per in people:
    print(per[2], end= " ")