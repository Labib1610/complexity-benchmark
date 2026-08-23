import sys
sys.setrecursionlimit(1000000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u = int(next(it)); v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)

    color = [0]*(n+1)           # 0 = uncolored, 1/2/3 = colors
    nodes = list(range(1, n+1))  # lexicographic order

    def dfs(pos):
        if pos == n:
            return True
        u = nodes[pos]
        for c in (1, 2, 3):
            ok = True
            for v in adj[u]:
                if color[v] == c:
                    ok = False
                    break
            if ok:
                color[u] = c
                if dfs(pos + 1):
                    return True
                color[u] = 0
        return False

    if dfs(0):
        out = ["YES", " ".join(str(color[i]) for i in range(1, n+1))]
    else:
        out = ["NO"]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()