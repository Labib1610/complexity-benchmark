import sys

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    colors = [0] * n  # 0 uncolored, 1..3 colors
    order = sorted(range(n), key=lambda x: bin(adj[x]).count('1'), reverse=True)

    # Precompute neighbor lists for quick check
    neigh = [ [j for j in range(n) if (adj[i] >> j) & 1] for i in range(n) ]

    # Choose next vertex: first uncolored in order
    def dfs(pos: int) -> bool:
        if pos == n:
            return True
        v = order[pos]
        if colors[v]:
            return dfs(pos + 1)
        # try colors
        for c in (1, 2, 3):
            conflict = False
            for nb in neigh[v]:
                if colors[nb] == c:
                    conflict = True
                    break
            if not conflict:
                colors[v] = c
                if dfs(pos + 1):
                    return True
                colors[v] = 0
        return False

    possible = dfs(0)
    out = []
    if not possible:
        out.append("NO")
    else:
        out.append("YES")
        out.append(' '.join(str(colors[i]) for i in range(n)))
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()