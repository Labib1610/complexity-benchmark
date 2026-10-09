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

    # order vertices by degree descending for initial heuristic
    order = sorted(range(n), key=lambda x: -len(adj[x]))
    pos_in_order = {v: i for i, v in enumerate(order)}
    # we will pick next vertex dynamically (DSATUR style)
    colors = [0] * n
    # for each vertex, keep set of neighbor colors used
    neighbor_used = [set() for _ in range(n)]

    def select_vertex():
        # choose uncolored vertex with maximum number of distinct neighbor colors,
        # tie-break by degree
        best = -1
        best_cnt = -1
        best_deg = -1
        for v in range(n):
            if colors[v] != 0:
                continue
            cnt = len(neighbor_used[v])
            deg = len(adj[v])
            if cnt > best_cnt or (cnt == best_cnt and deg > best_deg):
                best = v
                best_cnt = cnt
                best_deg = deg
        return best

    def dfs(colored_cnt: int) -> bool:
        if colored_cnt == n:
            return True
        v = select_vertex()
        # possible colors are those not used by neighbors
        used = neighbor_used[v]
        for c in (1, 2, 3):
            if c in used:
                continue
            # assign
            colors[v] = c
            changed = []
            for nb in adj[v]:
                if c not in neighbor_used[nb]:
                    neighbor_used[nb].add(c)
                    changed.append(nb)
            if dfs(colored_cnt + 1):
                return True
            # backtrack
            for nb in changed:
                neighbor_used[nb].remove(c)
            colors[v] = 0
        return False

    if dfs(0):
        print("YES")
        print(' '.join(map(str, colors)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()