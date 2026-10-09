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

    # order vertices by descending degree for better pruning
    order = sorted(range(n), key=lambda x: -len(adj[x]))
    pos_in_order = [0]*n
    for i, v in enumerate(order):
        pos_in_order[v] = i

    colors = [-1]*n
    sys.setrecursionlimit(10000)
    found = False

    def dfs(idx: int):
        nonlocal found
        if found:
            return
        if idx == n:
            found = True
            return
        v = order[idx]
        # try each color
        for c in range(3):
            conflict = False
            for nb in adj[v]:
                if colors[nb] == c:
                    conflict = True
                    break
            if not conflict:
                colors[v] = c
                dfs(idx+1)
                if found:
                    return
                colors[v] = -1

    dfs(0)

    out = []
    if not found:
        out.append("NO")
    else:
        out.append("YES")
        out.append(' '.join(str(c+1) for c in colors))
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()