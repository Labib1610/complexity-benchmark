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

    color = [0] * n
    found = False

    def dfs(v: int):
        nonlocal found
        if found:
            return
        if v == n:
            found = True
            return
        for c in (1, 2, 3):
            ok = True
            for nb in adj[v]:
                if nb < v and color[nb] == c:  # only already colored neighbors
                    ok = False
                    break
            if ok:
                color[v] = c
                dfs(v + 1)
                if found:
                    return
                color[v] = 0

    dfs(0)

    out = []
    if not found:
        out.append("NO")
    else:
        out.append("YES")
        out.append(" ".join(map(str, color)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()