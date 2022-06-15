import heapq
import sys

input = sys.stdin.readline
n = int(input())
right_heap = []
left_heap = []
for _ in range(n):
    num = int(input())
    
    if len(right_heap) == len(left_heap):
        heapq.heappush(left_heap, -num)
    else:
        heapq.heappush(right_heap, num)

    if right_heap and left_heap and right_heap[0] < -left_heap[0]:
        right = heapq.heappop(right_heap)
        left = heapq.heappop(left_heap)

        heapq.heappush(right_heap, -left)
        heapq.heappush(left_heap, -right)

    print(left_heap[0] * -1)