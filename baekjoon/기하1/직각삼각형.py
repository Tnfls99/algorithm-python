import sys
input = sys.stdin.readline
# 피타고라스의 정의 사용
while True:
    num = list(map(int, input().split()))
    if sum(num) == 0:
        break
    c = max(num)
    num.remove(c)
    if c**2 == num[0]**2 + num[1]**2:
        print('right')
    else:
        print('wrong')
