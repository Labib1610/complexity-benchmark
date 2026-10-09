import sys
from collections import deque


def main():
    data = sys.stdin.buffer.read().split()
    idx = 0
    u = int(data[idx]); s = int(data[idx + 1]); k = int(data[idx + 2]); idx += 3
    # Each consultant (set) has exactly 2 skills -> an edge between two skills. Read them.
    sets = []
    adj = [[] for _ in range(u + 1)]     # skill -> list of (other_skill, consultant_index)
    for ci in range(1, s + 1):
        c = int(data[idx]); idx += 1
        elems = [int(data[idx + t]) for t in range(c)]; idx += c
        sets.append(elems)
        if c == 2:
            a, b = elems
            adj[a].append((b, ci)); adj[b].append((a, ci))

    # Minimum set cover with 2-element sets == minimum EDGE COVER of the skill graph
    # = u - (maximum matching)  [Gallai], valid because every skill appears in some set.
    # 2-colour to recover the two skill groups (the graph is bipartite by the problem promise).
    color = [-1] * (u + 1)
    for st in range(1, u + 1):
        if color[st] != -1:
            continue
        color[st] = 0
        q = deque([st])
        while q:
            x = q.popleft()
            for (y, _ci) in adj[x]:
                if color[y] == -1:
                    color[y] = color[x] ^ 1
                    q.append(y)

    A = [v for v in range(1, u + 1) if color[v] == 0]
    INF = float("inf")
    matchA = {v: 0 for v in A}
    matchB = [0] * (u + 1)
    dist = {}

    def bfs():
        q = deque()
        for v in A:
            if matchA[v] == 0:
                dist[v] = 0; q.append(v)
            else:
                dist[v] = INF
        found = False
        while q:
            x = q.popleft()
            for (y, _ci) in adj[x]:
                w = matchB[y]
                if w == 0:
                    found = True
                elif dist.get(w, INF) == INF:
                    dist[w] = dist[x] + 1; q.append(w)
        return found

    def dfs(x):
        for (y, _ci) in adj[x]:
            w = matchB[y]
            if w == 0 or (dist.get(w, INF) == dist[x] + 1 and dfs(w)):
                matchA[x] = y; matchB[y] = x
                return True
        dist[x] = INF
        return False

    matching = 0
    while bfs():
        for v in A:
            if matchA[v] == 0 and dfs(v):
                matching += 1

    min_ec = u - matching
    if min_ec > k:
        sys.stdout.write("NO\n")
        return

    # Build a witness edge cover of size min_ec: take the matching edges, then cover each still-
    # uncovered skill with any one incident set.
    def edge_index(x, y):
        for (nb, ci) in adj[x]:
            if nb == y:
                return ci
        return None

    chosen = set()
    covered = [False] * (u + 1)
    for x in A:
        y = matchA[x]
        if y:
            chosen.add(edge_index(x, y)); covered[x] = True; covered[y] = True
    for v in range(1, u + 1):
        if not covered[v]:
            nb, ci = adj[v][0]
            chosen.add(ci); covered[v] = True; covered[nb] = True

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, sorted(chosen))) + "\n")


main()
