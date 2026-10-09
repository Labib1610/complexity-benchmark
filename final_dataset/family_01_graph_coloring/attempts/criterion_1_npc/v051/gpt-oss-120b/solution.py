import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n          # bitmask of neighbours
    neigh = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        neigh[u].append(v)
        neigh[v].append(u)

    colors = [-1] * n          # -1 uncolored, else 0,1,2
    order = sorted(range(n), key=lambda x: -len(neigh[x]))  # static order by degree

    # For dynamic selection, we will pick the uncolored vertex with most colored neighbours (DSATUR)
    def select_vertex():
        best = -1
        best_sat = -1
        best_deg = -1
        for v in range(n):
            if colors[v] != -1:
                continue
            used = 0
            for nb in neigh[v]:
                c = colors[nb]
                if c != -1:
                    used |= 1 << c
            sat = bin(used).count("1")
            deg = len(neigh[v])
            if sat > best_sat or (sat == best_sat and deg > best_deg):
                best_sat = sat
                best_deg = deg
                best = v
        return best

    def dfs(colored_cnt: int) -> bool:
        if colored_cnt == n:
            return True
        v = select_vertex()
        # compute forbidden colors from already colored neighbours
        forbid = 0
        for nb in neigh[v]:
            c = colors[nb]
            if c != -1:
                forbid |= 1 << c
        for col in range(3):
            if forbid & (1 << col):
                continue
            colors[v] = col
            if dfs(colored_cnt + 1):
                return True
            colors[v] = -1
        return False

    possible = dfs(0)
    if not possible:
        print("NO")
    else:
        print("YES")
        # convert to 1..3
        print(' '.join(str(c+1) for c in colors))

if __name__ == "__main__":
    solve()