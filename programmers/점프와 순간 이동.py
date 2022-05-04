# 한번에 점프 -> 그만큼 배터리 사용
# 현재거리 * 2 -> 배터리 사용 안함

def solution(n):
    cnt = 0
    while n > 1:
        if n % 2 != 0:
            n -= 1
            cnt += 1
        else: n //= 2
    return cnt + 1

    """
    def solution(n):
        return bin(n).count('1')
    """