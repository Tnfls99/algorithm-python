import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
stack = [0]
answer = [-1] * n
for i in range(1, n):
    # 스택에 인덱스 값을 저장
    # 만약 A[i] 번째 수보다 스택에 들은 인덱스의 배열 값이 다 크다면 오큰수를 못찾은 것
    # 그러다가 오큰수를 찾으면 스택 안에 있는 인덱스의 오큰수들이 다 그것이 되는 것!
    while stack and arr[stack[-1]] < arr[i]:
        answer[stack.pop()] = arr[i]
    # A[i]를 기준으로 왼쪽에 있는 수들과 비교하는 방식
    stack.append(i)

print(*answer)