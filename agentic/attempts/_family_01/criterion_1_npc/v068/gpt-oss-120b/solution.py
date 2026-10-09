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

    colors = [0] * n  # 0 = uncolored, else 1..3

    # Precompute order: start with highest degree
    order = sorted(range(n), key=lambda x: -len(adj[x]))

    # Helper to pick next vertex: MRV heuristic
    def select_vertex():
        best = -1
        best_options = 4  # more than max colors
        for v in order:
            if colors[v] == 0:
                used = {colors[u] for u in adj[v] if colors[u] != 0}
                options = 3 - len(used)
                if options == 0:
                    return v, []  # dead end
                if options < best_options:
                    best_options = options
                    best = v
                    if options == 1:
                        break
        if best == -1:
            return None, None
        used = {colors[u] for u in adj[best] if colors[u] != 0}
        avail = [c for c in (1, 2, 3) if c not in used]
        return best, avail

    def dfs(colored_cnt: int) -> bool:
        if colored_cnt == n:
            return True
        v, avail = select_vertex()
        if v is None:
            return True
        if not avail:  # no available colors
            return False
        for c in avail:
            colors[v] = c
            if dfs(colored_cnt + 1):
                return True
            colors[v] = 0
        return False

    if dfs(0):
        print("YES")
        print(' '.join(map(str, colors)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()