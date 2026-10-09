import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    k = int(data[0])
    t = int(data[1])
    idx = 2
    plans = []
    for _ in range(t):
        x = int(data[idx]); y = int(data[idx+1]); z = int(data[idx+2])
        idx += 3
        plans.append((x, y, z))
    
    # Since each driver is permanently assigned to exactly one truck and no two drivers share a truck,
    # driver x and truck y are effectively the same resource. We need to select k plans such that
    # each driver/truck pair is used exactly once and each route is used exactly once.
    # This is equivalent to finding a perfect matching in a bipartite graph where left nodes are
    # driver-truck pairs (which are 1-to-1) and right nodes are routes.
    
    # Build adjacency: for each driver (1..k), list of routes available
    adj = [[] for _ in range(k+1)]
    for i, (x, y, z) in enumerate(plans):
        adj[x].append((z, i))
    
    # Hopcroft-Karp for bipartite matching
    # Left: drivers 1..k, Right: routes 1..k
    pair_u = [0] * (k+1)  # driver -> route
    pair_v = [0] * (k+1)  # route -> driver
    dist = [0] * (k+1)
    INF = float('inf')
    
    from collections import deque
    
    def bfs():
        dq = deque()
        for u in range(1, k+1):
            if pair_u[u] == 0:
                dist[u] = 0
                dq.append(u)
            else:
                dist[u] = INF
        dist[0] = INF
        while dq:
            u = dq.popleft()
            if dist[u] < dist[0]:
                for v, _ in adj[u]:
                    if dist[pair_v[v]] == INF:
                        dist[pair_v[v]] = dist[u] + 1
                        dq.append(pair_v[v])
        return dist[0] != INF
    
    def dfs(u):
        if u != 0:
            for v, _ in adj[u]:
                if dist[pair_v[v]] == dist[u] + 1:
                    if dfs(pair_v[v]):
                        pair_u[u] = v
                        pair_v[v] = u
                        return True
            dist[u] = INF
            return False
        return True
    
    matching = 0
    while bfs():
        for u in range(1, k+1):
            if pair_u[u] == 0:
                if dfs(u):
                    matching += 1
    
    if matching != k:
        print("NO")
        return
    
    # We have a perfect matching. Now we need to output the selected plans.
    # For each driver u, pair_u[u] is the route. We need to find a plan with that driver and route.
    # Since driver->truck is fixed, any plan with driver u has the correct truck.
    # But we need to make sure we pick distinct plans (though with perfect matching, each driver-route pair
    # should correspond to at least one plan; if multiple, pick any).
    
    # Build a map from (driver, route) to plan index
    plan_map = {}
    for i, (x, y, z) in enumerate(plans):
        plan_map[(x, z)] = i
    
    selected = []
    for u in range(1, k+1):
        v = pair_u[u]
        i = plan_map[(u, v)]
        selected.append(plans[i])
    
    print("YES")
    out = []
    for x, y, z in selected:
        out.append(f"{x} {y} {z}")
    sys.stdout.write("\n".join(out) + "\n")

solve()