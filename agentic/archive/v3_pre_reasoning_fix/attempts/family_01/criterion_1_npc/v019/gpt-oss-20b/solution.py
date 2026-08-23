import sys
sys.setrecursionlimit(1000000)

def main():
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

    color = [0] * n
    found = False

    def dfs(idx):
        nonlocal found
        if found:
            return
        if idx == n:
            found = True
            return
        for c in (1, 2, 3):
            ok = True
            for nb in adj[idx]:
                if color[nb] == c:
                    ok = False
                    break
            if ok:
                color[idx] = c
                dfs(idx + 1)
                if found:
                    return
                color[idx] = 0

    dfs(0)

    out = sys.stdout
    if not found:
        out.write("NO\n")
    else:
        out.write("YES\n")
        out.write(' '.join(str(c) for c in color))
        out.write('\n')

if __name__ == "__main__":
    main()