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

    # order vertices by decreasing degree
    order = sorted(range(n), key=lambda x: -len(adj[x]))
    pos_in_order = [0] * n
    for idx, v in enumerate(order):
        pos_in_order[v] = idx

    colors = [0] * n  # 0 = uncolored, else 1..3

    def dfs(pos: int) -> bool:
        if pos == n:
            return True
        v = order[pos]
        # try colors 1..3
        for c in (1, 2, 3):
            ok = True
            for nb in adj[v]:
                if colors[nb] == c:
                    ok = False
                    break
            if ok:
                colors[v] = c
                if dfs(pos + 1):
                    return True
                colors[v] = 0
        return False

    if dfs(0):
        print("YES")
        print(' '.join(str(colors[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()