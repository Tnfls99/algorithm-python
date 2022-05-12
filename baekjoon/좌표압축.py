import sys
input = sys.stdin.readline
# 딕셔너리, 대소관계만을 활용 , 0에서 N 미만의 수로 만들어주기
n = int(input())
nums = list(map(int, input().split()))
sort_nums = sorted(nums)
nums_dict = {}
i = -1
for num in sort_nums:
    if num in nums_dict.keys(): continue
    else:
        i += 1
        nums_dict[num] = i

for num in nums :
    print(nums_dict[num], end = ' ')