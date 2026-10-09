import sys
from collections import deque

def add_edge(graph, u, v, cap):
    graph[u].append([v, cap, len(graph[v])])
    graph[v].append([u, 0, len(graph[u]) - 1])

def bfs_level(graph, s, t, level):
    for i in range(len(level)):
        level[i] = -1
    q = deque([s])
    level[s] = 0
    while q:
        u = q.popleft()
        for v, cap, rev in graph[u]:
            if cap > 0 and level[v] == -1:
                level[v] = level[u] + 1
                q.append(v)
    return level[t] != -1

def dfs_flow(graph, u, t, f, level, it):
    if u == t:
        return f
    for i in range(it[u], len(graph[u])):
        it[u] = i
        v, cap, rev = graph[u][i]
        if cap > 0 and level[v] == level[u] + 1:
            ret = dfs_flow(graph, v, t, min(f, cap), level, it)
            if ret > 0:
                graph[u][i][1] -= ret
                graph[v][rev][1] += ret
                return ret
    return 0

def max_flow(graph, s, t):
    n = len(graph)
    flow = 0
    level = [-1] * n
    INF = 10**18
    while bfs_level(graph, s, t, level):
        it = [0] * n
        while True:
            f = dfs_flow(graph, s, t, INF, level, it)
            if f == 0:
                break
            flow += f
    return flow

def main():
    input_data = sys.stdin.read().strip().split()
    it = iter(input_data)
    n = int(next(it)); m = int(next(it)); k = int(next(it))
    mandates = []
    for _ in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        mandates.append((s, t, d))
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        edges.append((u, v, cap))

    total_demand = sum(d for _, _, d in mandates)

    # Step 1: check feasibility using super source/sink
    N = n + 2
    S = n
    T = n + 1
    graph = [[] for _ in range(N)]
    balance = [0] * n
    for (s, t, d) in mandates:
        balance[s] += d
        balance[t] -= d
    for u, v, cap in edges:
        add_edge(graph, u, v, cap)
    for i in range(n):
        if balance[i] > 0:
            add_edge(graph, S, i, balance[i])
        elif balance[i] < 0:
            add_edge(graph, i, T, -balance[i])

    flow = max_flow(graph, S, T)
    if flow != total_demand:
        print("NO")
        return

    # Now we must extract per-mandate flows.
    # We will run separate max flow for each mandate on the residual capacities.
    # Copy the original capacities (since the previous max_flow destroyed graph).
    # We use shortest path? We'll just run max_flow again per mandate.

    # Build fresh graph for each mandate but reserve capacities used by previous mandates.
    assigned = [[0]*m for _ in range(k)]
    capacities = [cap for (_,_,cap) in edges]

    for idx, (s, t, d) in enumerate(mandates):
        # Build fresh graph with current remaining capacities
        g = [[] for _ in range(n)]
        for eidx, (u, v, _) in enumerate(edges):
            # remaining capacity = original cap - sum assigned so far on that edge
            used = sum(assigned[j][eidx] for j in range(k))
            rem = capacities[eidx] - used
            if rem > 0:
                add_edge(g, u, v, rem)
        flow_val = max_flow(g, s, t)
        if flow_val != d:
            print("NO")
            return
        # Extract flow for this mandate: differences in residual graph
        # We can inspect the forward edges and get how much was used.
        # We stored edges in same order, and added to g in same order. But indices shift because of reverse edges.
        # Easier: re-read flow by running max_flow on a fresh graph with source/sink and then subtract.
        # Actually, since max_flow modifies g, flow used on each original edge = original cap - remaining cap.
        # We'll keep original_cap list.
        for eidx, (u, v, cap_orig) in enumerate(edges):
            # Find the forward edge in g: it was added as first edge for this pair.
            # The forward edge is at index 2*eidx in g[u]? Actually we add edges sequentially.
            # We can reconstruct: after max_flow, the remaining forward edge capacity is stored in g[u][eidx][1]?
            # Let's store mapping: For each edge we add at position list index.
            pass

        # The above extraction is tricky. Better approach: after max_flow, use the residual to compute flow on edge:
        # For edge e: original_cap[e] - remaining_capacity_on_forward_edge = flow.
        # We'll compute it by scanning g[u] each time.
        for eidx, (u, v, cap_orig) in enumerate(edges):
            # find forward edge
            for edge in g[u]:
                if edge[0] == v and edge[1] > 0:
                    # Edge capacity after flow = remaining
                    rem = edge[1]
                    flow_on_edge = cap_orig - rem
                    assigned[idx][eidx] = flow_on_edge
                    break
            else:
                # edge full? forward edge cap might be 0
                assigned[idx][eidx] = cap_orig

    print("YES")
    for row in assigned:
        print(' '.join(map(str, row)))

if __name__ == "__main__":
    main()