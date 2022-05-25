import itertools
def card_sum(cards, m):
    sums = []
    com = list(itertools.combinations(cards, 3))
    for c in com:
        sum = 0
        for i in c:
            sum += int(i)
        sums.append(sum)
    for ans in reversed(sorted(sums)):
        if ans > m:
            continue
        else :
            print(ans)
            break

n, m = map(int, input().split())
cards = list(map(int, input().split()))
card_sum(cards, m)