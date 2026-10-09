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
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))

    # order vertices by degree descending for better pruning
    order = sorted(range(n), key=lambda x: -len(adj[x]))
    pos_in_order = [0]*n
    for idx, v in enumerate(order):
        pos_in_order[v] = idx

    colors = [-1]*n
    found = False

    def dfs(idx):
        nonlocal found
        if found:
            return
        if idx == n:
            found = True
            return
        v = order[idx]
        # try colors 0,1,2
        for c in range(3):
            conflict = False
            for nb in adj[v]:
                if colors[nb] == c:
                    conflict = True
                    break
            if not conflict:
                colors[v] = c
                dfs(idx+1)
                if found:
                    return
                colors[v] = -1

    dfs(0)

    if not found:
        print("NO")
    else:
        # map colors 0,1,2 to 1,2,3
        res = [str(c+1) for c in colors]
        print("YES")
        print(' '.join(res))

if __name__ == "__main__":
    solve()