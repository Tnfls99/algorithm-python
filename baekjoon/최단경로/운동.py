import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
v,e = map(int, input().split())
distance = [INF for _ in range(v+1)]
graph = [[] for _ in range(v+1)]
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    distance[b] = c
answer = INF
for start in range(1, v+1):
    distance = [INF for _ in range(v+1)]
    heap = []
    for next, d in graph[start]:
        distance[next] = d
        heapq.heappush(heap, (next, d))
    while heap:
        end, dist = heapq.heappop(heap)
        if start == end:
            break

        if distance[end] < dist:
            continue

        for next_end, next_dist in graph[end]:
            cost = dist + next_dist
            if distance[next_end] > cost:
                distance[next_end] = cost
                heapq.heappush(heap, (next_end, cost))
    answer = min(answer, distance[start])

print(answer) if answer != INF else print(-1)