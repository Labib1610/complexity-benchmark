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

    # order vertices by descending degree for better pruning
    order = sorted(range(n), key=lambda x: -len(adj[x]))
    color = [0] * n
    found = False

    def dfs(pos: int):
        nonlocal found
        if found:
            return
        if pos == n:
            found = True
            return
        v = order[pos]
        # try colors 1..3
        for c in (1, 2, 3):
            ok = True
            for nb in adj[v]:
                if color[nb] == c:
                    ok = False
                    break
            if ok:
                color[v] = c
                dfs(pos + 1)
                if found:
                    return
                color[v] = 0

    dfs(0)

    if not found:
        print("NO")
    else:
        print("YES")
        # output in original order
        print(' '.join(str(color[i]) for i in range(n)))

if __name__ == "__main__":
    solve()