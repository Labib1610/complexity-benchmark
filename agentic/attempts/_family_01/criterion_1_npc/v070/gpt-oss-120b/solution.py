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
    pos_in_order = [0]*n
    for i, v in enumerate(order):
        pos_in_order[v] = i

    colors = [-1]*n
    found = False

    def dfs(idx: int) -> bool:
        nonlocal found
        if idx == n:
            return True
        v = order[idx]
        # try each color that does not conflict with already colored neighbors
        used = [False]*3
        for nb in adj[v]:
            c = colors[nb]
            if c != -1:
                used[c] = True
        for col in range(3):
            if not used[col]:
                colors[v] = col
                if dfs(idx+1):
                    return True
                colors[v] = -1
        return False

    if dfs(0):
        print("YES")
        print(' '.join(str(c+1) for c in colors))
    else:
        print("NO")

if __name__ == "__main__":
    solve()