import sys
input = sys.stdin.readline
melon = int(input())

# 가장 긴 가로 전, 후로 가장 긴 세로와 구하기 위해 빼야 할 세로가 나온다.

widths = []
heights = []
total = []

for _ in range(6):
    d, l = map(int, input().split())
    if d == 1 or d == 2:
        widths.append(l)
    else:
        heights.append(l)
    total.append(l)

max_width_id = total.index(max(widths))
max_height_id = total.index(max(heights))

large_rec = max(heights) * max(widths)
# 만약 max_width_id = 0 이라면 1을 빼도 -1 로 마지막것을 가져오기 때문에 괜찮다. 인덱스 오류 발생 안함.
small_height = abs(total[max_width_id-1] - total[(max_width_id - 5 if max_width_id == 5 else max_width_id + 1)])
small_width = abs(total[max_height_id - 1] - total[(max_height_id - 5 if max_height_id == 5 else max_height_id + 1)])

area = large_rec - (small_height*small_width)
print(area * melon)