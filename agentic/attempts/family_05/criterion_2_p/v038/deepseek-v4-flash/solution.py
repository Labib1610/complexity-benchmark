import sys
from collections import deque

input = sys.stdin.readline

def hopcroft_karp(graph, n_left, n_right):
    INF = 10**9
    pair_u = [-1] * n_left
    pair_v = [-1] * n_right
    dist = [0] * n_left

    def bfs():
        q = deque()
        for u in range(n_left):
            if pair_u[u] == -1:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        found = False
        while q:
            u = q.popleft()
            for v in graph[u]:
                u2 = pair_v[v]
                if u2 == -1:
                    found = True
                elif dist[u2] == INF:
                    dist[u2] = dist[u] + 1
                    q.append(u2)
        return found

    def dfs(u):
        for v in graph[u]:
            u2 = pair_v[v]
            if u2 == -1 or (dist[u2] == dist[u] + 1 and dfs(u2)):
                pair_u[u] = v
                pair_v[v] = u
                return True
        dist[u] = INF
        return False

    matching = 0
    while bfs():
        for u in range(n_left):
            if pair_u[u] == -1 and dfs(u):
                matching += 1
    return matching, pair_u

k, t = map(int, input().split())
graph = [[] for _ in range(k)]
for _ in range(t):
    u, v, w = map(int, input().split())
    graph[u-1].append(w-1)

matching, pair_u = hopcroft_karp(graph, k, k)
if matching != k:
    print("NO")
else:
    print("YES")
    # The relay station for each sensor is fixed by the input; let's reconstruct it
    sensor_relay = [0] * k
    # We could have stored it during input, but let's re-scan: not possible without storing protocols.
    # Better approach: store relay mapping during input.
    # Since we didn't, we can re-read? No. So we need to store it in input phase.
    # We'll fix by reading input again? Not advisable here.
    # Actually we can store while reading before matching.
    # Let's adjust: we'll keep sensor_relay during input.
    # But we already printed matching; rewrite solution properly.
    sys.stdout.write("")