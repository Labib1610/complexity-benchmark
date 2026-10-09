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

    color = [0] * n          # 0 = unassigned, else 1..3
    found = False

    def dfs(v: int):
        nonlocal found
        if found:
            return
        if v == n:
            found = True
            return
        # try colours 1,2,3 in order
        for col in (1, 2, 3):
            ok = True
            for nb in adj[v]:
                if nb < v and color[nb] == col:
                    ok = False
                    break
            if not ok:
                continue
            color[v] = col
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
        out.append(" ".join(str(c) for c in color))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()