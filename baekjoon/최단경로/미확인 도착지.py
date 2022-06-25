# s 지점에서 출발
# 후각으로 지나간 도로 앎.
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
T = int(input())
def dijkstra(s, n):
    distance = [INF] * (n+1)

    heap = [(s, 0)]
    distance[s] = 0

    while heap:
        n, d = heapq.heappop(heap)

        if distance[n] < d:
            continue

        for next_n, next_d in graph[n]:
            cost = next_d + d
            if cost < distance[next_n]:
                distance[next_n] = cost
                heapq.heappush(heap, (next_n, cost))

    return distance


for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = [[] for i in range(n+1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        if (a == g and b == h) or (a == h and b == g):
            d -= 0.1
        graph[a].append((b, d))
        graph[b].append((a, d))

    nodes = [int(input()) for _ in range(t)]
    nodes.sort()
    dis = dijkstra(s, n)

    for node in nodes:
        if dis[node] != INF and type(dis[node]) == float:
            print(node, end=" ")
    print()