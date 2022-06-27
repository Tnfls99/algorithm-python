import sys
input = sys.stdin.readline
n, m = map(int, input().split())
INF = int(1e9)
graph = []
for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((a, b, c))
distance = [INF] * (n+1)

def bellman_ford(start):
    distance[start] = 0
    
    for i in range(n):
        # 매 반복마다 '모든 간선' 확인
        for k in range(m):
            node, next_n, cost = graph[k]
            if distance[node] != INF and distance[node] + cost < distance[next_n]:
                distance[next_n] = distance[node] + cost
                if i == n-1:
                    return True

    return False

has_cycle = bellman_ford(1)

if has_cycle:
    print(-1)
else: 
    for i in range(2, n+1):
        if distance[i] == INF:
            print(-1)
        else:
            print(distance[i])