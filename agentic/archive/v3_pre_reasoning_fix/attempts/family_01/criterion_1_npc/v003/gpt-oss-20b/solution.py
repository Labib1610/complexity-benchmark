import sys
sys.setrecursionlimit(10000)

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    color = [0] * (n + 1)
    found = False

    def dfs(v):
        nonlocal found
        if found:
            return
        if v > n:
            found = True
            return
        for c in (1, 2, 3):
            ok = True
            for u in adj[v]:
                if color[u] == c:
                    ok = False
                    break
            if not ok:
                continue
            color[v] = c
            dfs(v + 1)
            if found:
                return
            color[v] = 0

    dfs(1)

    out = []
    if not found:
        out.append("NO")
    else:
        out.append("YES")
        out.append(' '.join(str(color[i]) for i in range(1, n + 1)))
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    main()