from collections import deque
def bfs(g, start, times, K):
    queue = deque([start])

    times[start] = 0

    while queue:
        y = queue.popleft() # 현재 방문 중인 마을
        for x in range(1, len(g[y])): # 방문중인 마을에 연결된 마을 탐색
            if g[y][x] != 0: # 연결된 마을이라면 = 방문할 수 있는 마을이라면
                # 최소거리 리스트에 담겨있는 해당 마을까지의 거리보다 현재 방문중인 마을까지의 거리 + 앞으로 이동할 마을까지의 거리가
                # 더 작아야하고 (아니면 최소거리 리스트에 있는게 더 최소거리인것)
                # (문제조건) K보다 작아야한다.
                if times[x] > times[y] + g[y][x] and times[y] + g[y][x] <= K:
                    times[x] = times[y]+g[y][x]
                    queue.append(x)
    return len([i for i in times if i <= K])


def solution(N, roads, K):
    times = [500000 for _ in range(N+1)]
    g = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for fro, to, time in roads:
        if g[fro][to] == 0 and g[to][fro] == 0:
            g[fro][to], g[to][fro] = time, time
        else:
            if time < g[fro][to]:
                g[fro][to], g[to][fro] = time, time
                
    return bfs(g, 1, times, K)
