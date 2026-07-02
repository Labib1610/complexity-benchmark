import sys
from collections import deque


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    nA = int(data[idx]); idx += 1
    nB = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1

    adj = [[] for _ in range(nA + 1)]
    for _ in range(m):
        a = int(data[idx]); b = int(data[idx + 1]); idx += 2
        adj[a].append(b)

    # Hopcroft-Karp maximum matching between the two wings. By König's theorem
    # the minimum number of guards (minimum vertex cover) equals this matching.
    INF = float("inf")
    pair_u = [0] * (nA + 1)   # west -> east
    pair_v = [0] * (nB + 1)   # east -> west
    dist = [0] * (nA + 1)

    def bfs():
        q = deque()
        for u in range(1, nA + 1):
            if pair_u[u] == 0:
                dist[u] = 0
                q.append(u)
            else:
                dist[u] = INF
        reachable_free = False
        while q:
            u = q.popleft()
            for v in adj[u]:
                w = pair_v[v]
                if w == 0:
                    reachable_free = True
                elif dist[w] == INF:
                    dist[w] = dist[u] + 1
                    q.append(w)
        return reachable_free

    def dfs(u):
        for v in adj[u]:
            w = pair_v[v]
            if w == 0 or (dist[w] == dist[u] + 1 and dfs(w)):
                pair_u[u] = v
                pair_v[v] = u
                return True
        dist[u] = INF
        return False

    matching = 0
    while bfs():
        for u in range(1, nA + 1):
            if pair_u[u] == 0 and dfs(u):
                matching += 1

    print(matching)


main()
