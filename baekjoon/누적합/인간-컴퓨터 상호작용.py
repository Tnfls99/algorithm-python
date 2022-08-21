import sys
import string
input = sys.stdin.readline

s = input()
q = int(input())
char_list = {}
# 미리 알파벳별로 나오는 횟수를 담아놓음. -> 누적합으로
for char in string.ascii_lowercase:
    char_list[char] = [0]
    count = 0
    for i in range(len(s)):
        if s[i] == char:
            count += 1
        char_list[char].append(count)

for _ in range(q):
    arr = input().split()
    a, l, r = arr[0], int(arr[1]), int(arr[2])

    print(char_list[a][r+1] - char_list[a][l])