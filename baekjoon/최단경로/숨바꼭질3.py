# 수빈이는 걷거나 순간이동 가능
# 걷는다면 1초 후에 X-1 또는 X+1로 이동
# 순간이동의 경우 0초 후에 2*X로 이동
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
n, k = map(int, input().split())

times = [INF] * 100001

def dijkstra(n):
    heap = [(0, n)]
    times[n] = 0
    while heap:
        t, v = heapq.heappop(heap)
        nodes = [(1, v-1), (1, v+1), (0, 2*v)]

        if times[v] < t:
            continue

        for next_t, next_n in nodes:
            if next_n > len(times)-1 or next_n < 0:
                continue
            time = t + next_t
            if time < times[next_n]:
                times[next_n] = time
                heapq.heappush(heap, (time, next_n))


dijkstra(n)
print(times[k])