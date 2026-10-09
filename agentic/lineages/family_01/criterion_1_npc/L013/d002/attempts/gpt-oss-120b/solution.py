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

    colors = [-1] * n  # -1 uncolored, 0..2 colors

    # order vertices by degree descending for initial heuristic
    order = sorted(range(n), key=lambda x: len(adj[x]), reverse=True)

    # map from position in order to vertex
    pos2v = order
    # inverse mapping
    v2pos = [0] * n
    for i, v in enumerate(pos2v):
        v2pos[v] = i

    # adjacency in terms of positions for faster checks
    adj_pos = [set(v2pos[nb] for nb in adj[v]) for v in range(n)]

    # choose next vertex: first uncolored in order
    def dfs(idx: int) -> bool:
        if idx == n:
            return True
        v = pos2v[idx]
        # compute forbidden colors from already colored neighbors
        forbidden = 0
        for nb in adj[v]:
            c = colors[nb]
            if c != -1:
                forbidden |= 1 << c
        for c in range(3):
            if not (forbidden & (1 << c)):
                colors[v] = c
                if dfs(idx + 1):
                    return True
                colors[v] = -1
        return False

    possible = dfs(0)
    if not possible:
        print("NO")
    else:
        print("YES")
        print(' '.join(str(c + 1) for c in colors))

if __name__ == "__main__":
    solve()