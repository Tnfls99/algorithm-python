from collections import deque
def bfs(g, start, visited):
    route = []
    queue = deque([start])
    visited[start] = True
    
    while queue:
        q = queue.popleft()
        route.append(q)
        for i in g[q]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return route

def solution(n, wires):
    answer = 100
    g = [[] for _ in range(n+1)]
    for start, end in wires:
        g[start].append(end)
        g[end].append(start)
    
    for w1, w2 in wires:
        visited = [False] * (n+1)
        visited[w2] = True # 전선 끊는 곳은 미리 방문했다고 표시 -> 그럼 이어진 곳 방문 안하므로 끊어진 것처럼 취급됨.
        r = bfs(g, w1, visited)
        if abs(len(r) - (n - len(r))) < answer:
            answer = abs(len(r) - (n - len(r)))
        
    return answer