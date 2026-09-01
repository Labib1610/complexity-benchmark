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

    colour = [0] * n          # 0 = unassigned, otherwise 1..3
    found = False

    def dfs(v: int) -> None:
        nonlocal found
        if found:
            return
        if v == n:
            # all vertices coloured
            found = True
            return
        # compute forbidden colours from already coloured neighbours
        forbidden = 0
        for nb in adj[v]:
            c = colour[nb]
            if c:
                forbidden |= 1 << c   # bit 1<<c
        for col in (1, 2, 3):
            if forbidden & (1 << col):
                continue
            colour[v] = col
            dfs(v + 1)
            if found:
                return
            colour[v] = 0

    dfs(0)

    out = []
    if not found:
        out.append("NO")
    else:
        out.append("YES")
        out.append(" ".join(str(c) for c in colour))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()