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

    colors = [-1] * n          # -1 uncolored, 0/1/2 for shifts
    # order vertices by degree descending for initial heuristic
    order = sorted(range(n), key=lambda x: -len(neigh[x]))
    # map from position in order to vertex
    pos2v = order
    # for fast selection of next vertex, we will recompute each step
    def select_vertex():
        # choose uncolored vertex with most colored neighbours (DSATUR)
        best = -1
        best_sat = -1
        best_deg = -1
        for v in range(n):
            if colors[v] != -1:
                continue
            used = 0
            deg = 0
            for nb in neigh[v]:
                if colors[nb] != -1:
                    used |= 1 << colors[nb]
                deg += 1
            sat = used.bit_count()
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
        for c in range(3):
            if forbid & (1 << c):
                continue
            colors[v] = c
            if dfs(colored_cnt + 1):
                return True
            colors[v] = -1
        return False

    possible = dfs(0)
    if not possible:
        print("NO")
    else:
        print("YES")
        # convert 0/1/2 to 1/2/3
        print(' '.join(str(c + 1) for c in colors))

if __name__ == "__main__":
    solve()