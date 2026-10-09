import sys
sys.setrecursionlimit(10000)

def find_bridges(n, edges, adj):
    visited = [False] * (n + 1)
    tin = [-1] * (n + 1)
    low = [-1] * (n + 1)
    timer = 0
    bridges = []

    def dfs(v, p_edge):
        nonlocal timer
        visited[v] = True
        tin[v] = low[v] = timer
        timer += 1
        for to, eid in adj[v]:
            if eid == p_edge:
                continue
            if visited[to]:
                low[v] = min(low[v], tin[to])
            else:
                dfs(to, eid)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    bridges.append(eid)
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(i, -1)
    return bridges

def solve():
    input_data = sys.stdin.read().strip().split()
    n = int(input_data[0])
    m = int(input_data[1])
    edges = []
    adj = [[] for _ in range(n + 1)]
    idx = 2
    for eid in range(m):
        u = int(input_data[idx]); v = int(input_data[idx+1])
        idx += 2
        edges.append((u, v))
        adj[u].append((v, eid))
        adj[v].append((u, eid))

    # Check for bridges
    bridges = find_bridges(n, edges, adj)
    if bridges:
        print("NO")
        return

    # 3-edge-coloring for bridgeless cubic graph
    color = [-1] * m

    # Step 1: Find a perfect matching using simple greedy (since cubic bridgeless => has perfect matching)
    matched = [False] * (n + 1)
    matching_edges = []
    for eid, (u, v) in enumerate(edges):
        if not matched[u] and not matched[v]:
            matched[u] = matched[v] = True
            matching_edges.append(eid)
            color[eid] = 1

    # Step 2: Remove matching edges, remaining graph is 2-regular (cycles)
    # Color cycles with colors 2 and 3 alternately
    adj_left = [[] for _ in range(n + 1)]
    for eid, (u, v) in enumerate(edges):
        if color[eid] == -1:
            adj_left[u].append((v, eid))
            adj_left[v].append((u, eid))

    visited = [False] * (n + 1)
    for start in range(1, n + 1):
        if not visited[start] and adj_left[start]:
            # traverse cycle
            cur = start
            prev_e = -1
            while True:
                visited[cur] = True
                # pick next edge not used
                nxt = None
                for to, eid in adj_left[cur]:
                    if eid != prev_e:
                        nxt = (to, eid)
                        break
                if nxt is None:
                    break
                to, eid = nxt
                # assign color alternating
                if color[eid] == -1:
                    # determine color based on previous edge color
                    if prev_e != -1 and color[prev_e] == 2:
                        color[eid] = 3
                    else:
                        color[eid] = 2
                prev_e = eid
                cur = to
                if cur == start:
                    break

    # Fill any remaining uncolored edges (shouldn't happen)
    for i in range(m):
        if color[i] == -1:
            color[i] = 1

    print("YES")
    print(" ".join(str(c) for c in color))

if __name__ == "__main__":
    solve()