# 이게 왜 level2??
import math
def solution(n, k):
    nums = [i for i in range(1, n + 1)]
    stack = []
    k = k-1
    while nums:
        # k / (n-1)! 을 했을 때의 몫이 맨 첫번째 자리
        a = k // math.factorial(n - 1)
        stack.append(nums[a])
        del nums[a]

        # k를 줄여야함.
        k = k % math.factorial(n - 1)
        n -= 1


    return stack