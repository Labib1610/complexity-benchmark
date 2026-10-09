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

    colors = [0] * n
    sys.setrecursionlimit(10000)
    found = False

    def dfs(idx: int):
        nonlocal found
        if found:
            return
        if idx == n:
            found = True
            return
        for c in (1, 2, 3):
            ok = True
            for nb in adj[idx]:
                if nb < idx and colors[nb] == c:
                    ok = False
                    break
            if ok:
                colors[idx] = c
                dfs(idx + 1)
                if found:
                    return
                colors[idx] = 0

    dfs(0)

    out = []
    if not found:
        out.append("NO")
    else:
        out.append("YES")
        out.append(" ".join(map(str, colors)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()