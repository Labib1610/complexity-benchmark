import sys
sys.setrecursionlimit(1 << 25)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    nP = int(next(it))
    nS = int(next(it))
    m = int(next(it))
    edges = [(0, 0)] * (m + 1)          # 1‑based
    adj = [[] for _ in range(nP + nS + 1)]
    for i in range(1, m + 1):
        u = int(next(it))
        v = int(next(it)) + nP          # shift secondary indices
        edges[i] = (u, v)
        adj[u].append(i)
        adj[v].append(i)

    # compute degrees and Δ
    deg = [0] * (nP + nS + 1)
    for u in range(1, nP + nS + 1):
        deg[u] = len(adj[u])
    Delta = max(deg)

    # colour structures
    col_edge = [dict() for _ in range(nP + nS + 1)]   # vertex -> {colour: edge}
    edge_colour = [0] * (m + 1)

    # helper: smallest free colour at vertex v (1..Delta)
    def free_colour(v: int) -> int:
        used = col_edge[v]
        for c in range(1, Delta + 1):
            if c not in used:
                return c
        return 1  # never reached

    # dfs to free colour `col` at vertex `v`
    def dfs(v: int, col: int, seen: set) -> bool:
        if col not in col_edge[v]:
            return True
        if v in seen:
            return False
        seen.add(v)
        e = col_edge[v][col]
        u, w = edges[e]
        other = w if v == u else u
        for c2 in range(1, Delta + 1):
            if c2 == col:
                continue
            if dfs(other, c2, seen):
                # reassign edge e from colour `col` to `c2`
                col_edge[v].pop(col, None)
                col_edge[other].pop(col, None)
                col_edge[v][c2] = e
                col_edge[other][c2] = e
                edge_colour[e] = c2
                return True
        return False

    for i in range(1, m + 1):
        u, v = edges[i]
        c = free_colour(u)
        if c not in col_edge[v]:
            # direct assignment
            col_edge[u][c] = i
            col_edge[v][c] = i
            edge_colour[i] = c
        else:
            # need to free colour c at v
            if not dfs(v, c, set()):
                print("NO")
                return
            # now c is free at v
            col_edge[u][c] = i
            col_edge[v][c] = i
            edge_colour[i] = c

    # output
    out = ["YES"]
    out.append(" ".join(str(edge_colour[i]) for i in range(1, m + 1)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()