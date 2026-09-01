import sys

def solve() -> None:
    sys.setrecursionlimit(10000)
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

    colors = [0] * n
    found = False

    def dfs(v: int):
        nonlocal found
        if found:
            return
        if v == n:
            found = True
            return
        # try colors 1..3
        used = {colors[nb] for nb in adj[v] if colors[nb] != 0}
        for c in (1, 2, 3):
            if c in used:
                continue
            colors[v] = c
            dfs(v + 1)
            if found:
                return
            colors[v] = 0

    dfs(0)

    out = sys.stdout
    if not found:
        out.write("NO")
    else:
        out.write("YES\n")
        out.write(" ".join(map(str, colors)))

if __name__ == "__main__":
    solve()