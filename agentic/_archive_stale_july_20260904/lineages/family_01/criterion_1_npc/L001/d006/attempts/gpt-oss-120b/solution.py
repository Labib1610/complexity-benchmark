import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n  # bitmask of neighbors
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    colors = [0] * n
    found = False

    # For quick conflict check, maintain for each color a bitmask of vertices already colored with that color
    color_mask = [0, 0, 0, 0]  # index 1..3

    def dfs(v: int):
        nonlocal found
        if found:
            return
        if v == n:
            found = True
            return
        # try colors 1..3
        neighbor_mask = adj[v]
        for c in (1, 2, 3):
            if neighbor_mask & color_mask[c]:
                continue  # conflict
            colors[v] = c
            color_mask[c] |= 1 << v
            dfs(v + 1)
            if found:
                return
            color_mask[c] ^= 1 << v
            colors[v] = 0

    dfs(0)

    out = sys.stdout
    if not found:
        out.write("NO")
    else:
        out.write("YES\n")
        out.write(" ".join(map(str, colors)))

if __name__ == "__main__":
    solve()