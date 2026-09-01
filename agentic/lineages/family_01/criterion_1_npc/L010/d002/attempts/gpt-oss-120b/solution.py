import sys

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

    colors = [0] * n  # 0 = uncolored, else 1..3

    # For each vertex, keep a mask of colors used by already colored neighbors
    used = [0] * n  # bits 0,1,2 correspond to colors 1,2,3

    sys.setrecursionlimit(10000)

    def dfs(v: int) -> bool:
        if v == n:
            return True
        # compute forbidden colors from already colored neighbors
        forbid = used[v]
        for col in range(1, 4):
            if forbid & (1 << (col - 1)):
                continue
            # assign
            colors[v] = col
            # update neighbors' used masks
            changed = []
            mask = 1 << (col - 1)
            nb = adj[v]
            while nb:
                u = (nb & -nb).bit_length() - 1
                nb &= nb - 1
                if colors[u] == 0:
                    if not (used[u] & mask):
                        used[u] |= mask
                        changed.append(u)
            if dfs(v + 1):
                return True
            # backtrack
            for u in changed:
                used[u] &= ~mask
            colors[v] = 0
        return False

    possible = dfs(0)
    out = []
    if not possible:
        out.append("NO")
    else:
        out.append("YES")
        out.append(" ".join(str(c) for c in colors))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()