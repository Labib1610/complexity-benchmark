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

    colors = [0] * n
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
                if nb < v and colors[nb] == c:
                    ok = False
                    break
            if ok:
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