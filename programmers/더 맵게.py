import heapq
def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    
    while True:
        min1 = heapq.heappop(scoville)
        if min1 >= K:
            return cnt
        if not scoville:
            return -1
        min2 = heapq.heappop(scoville)
        heapq.heappush(scoville, min1+min2*2)
        cnt += 1