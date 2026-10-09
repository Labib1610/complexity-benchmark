import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)

    # static order for tie‑break (higher degree first)
    order = sorted(range(n), key=lambda x: -len(adj[x]))

    col = [-1] * n  # -1 uncoloured, else 0,1,2

    # pre‑compute position of each vertex in 'order' for fast tie‑break
    pos_in_order = [0] * n
    for i, v in enumerate(order):
        pos_in_order[v] = i

    def dfs(coloured_cnt: int) -> bool:
        if coloured_cnt == n:
            return True

        # choose vertex with maximal degree among uncoloured
        v = -1
        best_deg = -1
        best_pos = n + 1
        for u in range(n):
            if col[u] == -1:
                d = len(adj[u])
                p = pos_in_order[u]
                if d > best_deg or (d == best_deg and p < best_pos):
                    best_deg = d
                    best_pos = p
                    v = u

        # try colours 0,1,2
        for c in range(3):
            conflict = False
            for nb in adj[v]:
                if col[nb] == c:
                    conflict = True
                    break
            if conflict:
                continue
            col[v] = c
            if dfs(coloured_cnt + 1):
                return True
            col[v] = -1
        return False

    if dfs(0):
        out = ['YES', ' '.join(str(c + 1) for c in col)]
    else:
        out = ['NO']
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()