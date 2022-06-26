# R 순서 뒤집기 / D 첫번째 수 버리기 - 배열이 비어있으면 오류 발생

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = input().rstrip()
    n = int(input())
    array = deque(input().rstrip()[1:-1].split(','))
    flag = 0
    if n == 0:
        array = []
    for f in p:
        if f == 'R':
            flag += 1
        else:
            if not array:
                print('error')
                break
            else:
                if flag % 2 == 0:
                    array.popleft()
                else:
                    array.pop()
                    

    else:
        if flag % 2 == 0:
            print("[" + ",".join(array) + "]")
        else:
            array.reverse()
            print("[" + ",".join(array) + "]")