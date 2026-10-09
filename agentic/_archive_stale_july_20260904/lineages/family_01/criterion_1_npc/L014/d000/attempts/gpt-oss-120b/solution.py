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

    color = [0] * n          # 0 = uncoloured, else 1..3
    found = False
    answer = None

    # fast check whether a colour is allowed for vertex v
    def allowed(v, c):
        for nb in adj[v]:
            if color[nb] == c:
                return False
        return True

    # forward checking: ensure every uncoloured vertex still has at least one possible colour
    def forward_ok():
        for v in range(n):
            if color[v] == 0:
                possible = False
                for c in (1, 2, 3):
                    ok = True
                    for nb in adj[v]:
                        if color[nb] == c:
                            ok = False
                            break
                    if ok:
                        possible = True
                        break
                if not possible:
                    return False
        return True

    def dfs(v):
        nonlocal found, answer
        if found:
            return
        if v == n:
            found = True
            answer = color.copy()
            return
        for c in (1, 2, 3):
            if allowed(v, c):
                color[v] = c
                if forward_ok():
                    dfs(v + 1)
                color[v] = 0
                if found:
                    return

    dfs(0)

    out = []
    if not found:
        out.append("NO")
    else:
        out.append("YES")
        out.append(" ".join(str(x) for x in answer))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()