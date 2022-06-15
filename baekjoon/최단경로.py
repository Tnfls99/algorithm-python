# 다익스트라 알고리즘이 사용된다.
# 가중치가 없는 최단경로는 BFS를 사용하면 쉽게 얻을 수 있다.
# 가중치가 있다면 DFS로 최단경로를 쉽게 얻을 수 있다?
import sys
import heapq

INF = int(1e9)
input = sys.stdin.readline
# 정점의 개수와 간선의 개수
v, e = map(int, input().split())
# 시작 정점
start = int(input())
# 최단거리 테이블
distance = [INF] * (v+1)
# 그래프 정보 받아오기
graph = [[] for _ in range(v+1)]
for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
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
    
dijkstra(start)

for i in range(1, v+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
