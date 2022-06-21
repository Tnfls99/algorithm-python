# 그래프는 방향성이 없음
# 1번부터 최단거리로 N까지 이동
# 한 번 이동했던 정점, 간선 모두 이용 가능
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
n, e = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

must_v1, must_v2 = map(int, input().split())

def dijkstra(start, end):
    distance = [INF] * (n+1)
    q = []
    # 최소힙을 사용하여 가장 짧은 거리의 노드 반환
    heapq.heappush(q, (0, start))
    distance[start] = 0
    # 시작노드와 연결된 경로 중 최단 경로 탐색
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue

        for v, w in graph[now]:
            cost = dist + w
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(q, (cost, v))
    return distance[end]
            

len1 = dijkstra(1, must_v1) + dijkstra(must_v1, must_v2) + dijkstra(must_v2, n)
len2 = dijkstra(1, must_v2) + dijkstra(must_v2, must_v1) + dijkstra(must_v1, n)


if len1 >= INF and len2 >= INF:
    print(-1)
else: print(min(len1, len2))