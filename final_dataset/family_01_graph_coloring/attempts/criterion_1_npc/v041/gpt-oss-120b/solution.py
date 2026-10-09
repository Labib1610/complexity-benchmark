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

    # order vertices by degree descending for better pruning
    order = sorted(range(n), key=lambda x: -len(adj[x]))
    # map position in order to vertex id and reverse
    pos2v = order
    v2pos = [0] * n
    for p, v in enumerate(pos2v):
        v2pos[v] = p

    colors = [0] * n
    found = False

    def dfs(idx: int):
        nonlocal found
        if found:
            return
        if idx == n:
            found = True
            return
        v = pos2v[idx]
        # try colors 1..3
        for c in (1, 2, 3):
            conflict = False
            for nb in adj[v]:
                if colors[nb] == c:
                    conflict = True
                    break
            if not conflict:
                colors[v] = c
                dfs(idx + 1)
                if found:
                    return
                colors[v] = 0

    dfs(0)

    out = sys.stdout
    if not found:
        out.write("NO")
    else:
        out.write("YES\n")
        out.write(" ".join(str(colors[i]) for i in range(n)))

if __name__ == "__main__":
    solve()