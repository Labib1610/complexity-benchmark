import sys

sys.setrecursionlimit(10000)

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

    colors = [-1] * n
    order = sorted(range(n), key=lambda x: -len(adj[x]))  # static order by degree

    # Precompute neighbor list for fast check
    neigh = adj

    def select_vertex():
        # choose uncolored vertex with most colored neighbors (DSATUR heuristic)
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
        # try colors 0,1,2
        for c in range(3):
            ok = True
            for nb in neigh[v]:
                if colors[nb] == c:
                    ok = False
                    break
            if not ok:
                continue
            colors[v] = c
            if dfs(colored_cnt + 1):
                return True
            colors[v] = -1
        return False

    if dfs(0):
        print("YES")
        print(' '.join(str(c+1) for c in colors))
    else:
        print("NO")

if __name__ == "__main__":
    solve()