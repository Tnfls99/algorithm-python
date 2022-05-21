import sys
n = int(input())
nums = []
sum = 0
cnt = dict()
for _ in range(n):
    num = int(sys.stdin.readline())
    nums.append(num)
    sum += num
    if num not in cnt:
        cnt[num] = 1
    else: cnt[num] += 1

# 산술 평균
print(round(sum/len(nums)))
# 중앙 값
nums.sort()
print(nums[len(nums)//2])
# 최빈값
most = [k for k, v in cnt.items() if max(cnt.values()) == v]
if len(most) > 1:
    most.sort()
    print(most[1])
else : print(most[0])
# 범위
start = min(nums)
end = max(nums)
print(abs(end - start))