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

    colors = [-1] * n  # -1 uncolored, else 0,1,2

    # order vertices by degree descending for initial heuristic
    order = sorted(range(n), key=lambda x: len(adj[x]), reverse=True)

    # Precompute neighbor list for fast access
    neighbors = adj

    # Helper to select next vertex: MRV (fewest available colors)
    def select_vertex():
        best = -1
        best_options = 4
        for v in order:
            if colors[v] != -1:
                continue
            used = 0
            for nb in neighbors[v]:
                c = colors[nb]
                if c != -1:
                    used |= 1 << c
            options = 3 - bin(used).count('1')
            if options < best_options:
                best_options = options
                best = v
                if options == 1:
                    break
        return best

    def dfs(colored_cnt: int) -> bool:
        if colored_cnt == n:
            return True
        v = select_vertex()
        # compute used colors
        used = 0
        for nb in neighbors[v]:
            c = colors[nb]
            if c != -1:
                used |= 1 << c
        for col in range(3):
            if not (used & (1 << col)):
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
        print(' '.join(str(c + 1) for c in colors))

if __name__ == "__main__":
    solve()