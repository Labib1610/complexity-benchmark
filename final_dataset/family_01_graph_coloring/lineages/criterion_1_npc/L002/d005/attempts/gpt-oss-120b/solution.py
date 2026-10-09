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

    # order vertices by degree descending for better pruning
    order = sorted(range(n), key=lambda x: -len(adj[x]))
    color = [0] * n
    pos_in_order = [0] * n
    for idx, v in enumerate(order):
        pos_in_order[v] = idx

    def dfs(idx: int) -> bool:
        if idx == n:
            return True
        v = order[idx]
        # try colors 1..3
        for c in (1, 2, 3):
            ok = True
            for nb in adj[v]:
                if color[nb] == c:
                    ok = False
                    break
            if ok:
                color[v] = c
                if dfs(idx + 1):
                    return True
                color[v] = 0
        return False

    if dfs(0):
        print("YES")
        print(' '.join(map(str, color)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()