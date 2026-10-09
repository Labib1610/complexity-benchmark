import sys
sys.setrecursionlimit(10000)

def solve():
    input_data = sys.stdin.read().strip().split()
    n, m = int(input_data[0]), int(input_data[1])
    edges = []
    adj = [[] for _ in range(n)]
    idx = 0
    ptr = 2
    for i in range(m):
        u = int(input_data[ptr]) - 1
        v = int(input_data[ptr+1]) - 1
        ptr += 2
        edges.append((u, v))
        adj[u].append((v, i))
        adj[v].append((u, i))

    # Check for bridges using DFS
    visited = [False] * n
    tin = [-1] * n
    low = [-1] * n
    timer = [0]
    has_bridge = [False]

    def dfs(v, p_edge):
        visited[v] = True
        tin[v] = low[v] = timer[0]
        timer[0] += 1
        for to, eid in adj[v]:
            if eid == p_edge:
                continue
            if visited[to]:
                low[v] = min(low[v], tin[to])
            else:
                dfs(to, eid)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    has_bridge[0] = True

    dfs(0, -1)
    if has_bridge[0]:
        print("NO")
        return

    # Now 3-edge-color the cubic bridgeless graph
    color = [-1] * m
    # For each vertex, keep which colors are already used
    used_at = [set() for _ in range(n)]

    # Sort edges by adjacency? Use backtracking with MRV
    edge_list = list(range(m))
    # simple heuristic: order by degree constraints
    edge_order = sorted(edge_list, key=lambda e: len(adj[edges[e][0]]) + len(adj[edges[e][1]]))

    def backtrack(ei):
        if ei == m:
            return True
        e = edge_order[ei]
        u, v = edges[e]
        possible = [c for c in (0,1,2) if c not in used_at[u] and c not in used_at[v]]
        for c in possible:
            color[e] = c
            used_at[u].add(c)
            used_at[v].add(c)
            if backtrack(ei+1):
                return True
            used_at[u].remove(c)
            used_at[v].remove(c)
            color[e] = -1
        return False

    if backtrack(0):
        print("YES")
        print(' '.join(str(c+1) for c in color))
    else:
        print("NO")

if __name__ == "__main__":
    solve()