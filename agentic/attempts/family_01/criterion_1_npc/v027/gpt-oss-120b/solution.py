import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [set() for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].add(v)
        adj[v].add(u)

    colors = [-1] * n  # -1 uncolored, 0,1,2 for vaults 1,2,3

    # precompute degrees
    degree = [len(adj[i]) for i in range(n)]

    # order of selection: dynamic DSATUR
    def select_vertex():
        # choose uncolored vertex with max saturation (different colors among colored neighbors)
        best = -1
        best_sat = -1
        best_deg = -1
        for v in range(n):
            if colors[v] != -1:
                continue
            neigh_colors = {colors[u] for u in adj[v] if colors[u] != -1}
            sat = len(neigh_colors)
            if sat > best_sat or (sat == best_sat and degree[v] > best_deg):
                best = v
                best_sat = sat
                best_deg = degree[v]
        return best

    sys.setrecursionlimit(10000)
    found = False

    def dfs(colored_cnt: int):
        nonlocal found
        if found:
            return
        if colored_cnt == n:
            found = True
            return
        v = select_vertex()
        used = {colors[u] for u in adj[v] if colors[u] != -1}
        for c in range(3):
            if c in used:
                continue
            colors[v] = c
            dfs(colored_cnt + 1)
            if found:
                return
            colors[v] = -1

    dfs(0)

    out = []
    if not found:
        out.append("NO")
    else:
        out.append("YES")
        out.append(' '.join(str(c + 1) for c in colors))
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()