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
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))

    # order vertices by decreasing degree
    order = sorted(range(n), key=lambda x: -len(adj[x]))
    pos_in_order = [0] * n
    for i, v in enumerate(order):
        pos_in_order[v] = i

    col = [-1] * n
    found = False

    def dfs(idx: int) -> bool:
        nonlocal found
        if idx == n:
            return True
        v = order[idx]
        for c in range(3):
            ok = True
            for nb in adj[v]:
                if col[nb] == c:
                    ok = False
                    break
            if not ok:
                continue
            col[v] = c
            if dfs(idx + 1):
                return True
            col[v] = -1
        return False

    if dfs(0):
        print("YES")
        # convert 0/1/2 to 1/2/3
        print(' '.join(str(col[i] + 1) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()