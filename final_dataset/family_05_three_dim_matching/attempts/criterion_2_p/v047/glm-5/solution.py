import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    total = k * (k + 1) // 2

    # pilot -> list of (phase, mech)
    pilot_phases = [[] for _ in range(k + 1)]
    pilot_mech = [0] * (k + 1)

    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        pilot_phases[x].append(z)
        pilot_mech[x] = y

    # Check feasibility: every pilot must have at least one phase
    for x in range(1, k + 1):
        if not pilot_phases[x]:
            print("NO")
            return

    # Build bipartite graph: left = pilots (1..k), right = phases (1..k)
    # We need a perfect matching where sum of pilot IDs = total and sum of phase IDs = total.
    # Since both sets are {1..k}, any perfect matching automatically has both sums equal to total.
    # So we just need any perfect matching.

    # Use Hopcroft-Karp for efficiency
    # adj[pilot] = list of phases
    adj = [[] for _ in range(k + 1)]
    for x in range(1, k + 1):
        adj[x] = pilot_phases[x]

    # Hopcroft-Karp
    INF = float('inf')
    pair_u = [0] * (k + 1)  # pair_u[pilot] = phase
    pair_v = [0] * (k + 1)  # pair_v[phase] = pilot
    dist = [0] * (k + 1)

    from collections import deque

    def bfs():
        queue = deque()
        found = False
        for u in range(1, k + 1):
            if pair_u[u] == 0:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = INF
        dist[0] = INF
        while queue:
            u = queue.popleft()
            if dist[u] < dist[0]:
                for v in adj[u]:
                    pu = pair_v[v]
                    if dist[pu] == INF:
                        dist[pu] = dist[u] + 1
                        queue.append(pu)
        return dist[0] != INF

    def dfs(u):
        if u == 0:
            return True
        for v in adj[u]:
            pu = pair_v[v]
            if dist[pu] == dist[u] + 1:
                if dfs(pu):
                    pair_u[u] = v
                    pair_v[v] = u
                    return True
        dist[u] = INF
        return False

    matching = 0
    while bfs():
        for u in range(1, k + 1):
            if pair_u[u] == 0:
                if dfs(u):
                    matching += 1

    if matching != k:
        print("NO")
        return

    print("YES")
    for x in range(1, k + 1):
        z = pair_u[x]
        y = pilot_mech[x]
        print(f"{x} {y} {z}")

solve()