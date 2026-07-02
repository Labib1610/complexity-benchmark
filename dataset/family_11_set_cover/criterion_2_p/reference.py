import sys
from collections import deque


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    uA = int(data[idx]); uB = int(data[idx + 1]); s = int(data[idx + 2]); idx += 3

    adj = [[] for _ in range(uA + 1)]
    seen = set()
    for _ in range(s):
        a = int(data[idx]); b = int(data[idx + 1]); idx += 2
        if (a, b) not in seen:          # parallel consultants don't change matching
            seen.add((a, b))
            adj[a].append(b)

    # Each consultant is an edge between a frontend skill and a backend skill.
    # Covering all skills = choosing a minimum edge cover; with no uncovered
    # skill, its size is V - maxMatching (Gallai), V = uA + uB.
    INF = float("inf")
    pair_u = [0] * (uA + 1)
    pair_v = [0] * (uB + 1)
    dist = [0] * (uA + 1)

    def bfs():
        q = deque()
        for uu in range(1, uA + 1):
            if pair_u[uu] == 0:
                dist[uu] = 0
                q.append(uu)
            else:
                dist[uu] = INF
        reachable_free = False
        while q:
            uu = q.popleft()
            for v in adj[uu]:
                w = pair_v[v]
                if w == 0:
                    reachable_free = True
                elif dist[w] == INF:
                    dist[w] = dist[uu] + 1
                    q.append(w)
        return reachable_free

    def dfs(uu):
        for v in adj[uu]:
            w = pair_v[v]
            if w == 0 or (dist[w] == dist[uu] + 1 and dfs(w)):
                pair_u[uu] = v
                pair_v[v] = uu
                return True
        dist[uu] = INF
        return False

    matching = 0
    while bfs():
        for uu in range(1, uA + 1):
            if pair_u[uu] == 0 and dfs(uu):
                matching += 1

    print((uA + uB) - matching)


main()
