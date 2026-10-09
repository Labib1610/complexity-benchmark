import sys
sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n          # bitmask of neighbours
    neigh = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        neigh[u].append(v)
        neigh[v].append(u)

    # order vertices by degree descending for better pruning
    order = sorted(range(n), key=lambda x: -len(neigh[x]))
    pos_in_order = [0] * n
    for i, v in enumerate(order):
        pos_in_order[v] = i

    colors = [0] * n  # 0 = uncolored, else 1..3

    # For each vertex keep a mask of colors already used by its coloured neighbours
    used_mask = [0] * n  # bit 0 for color1, bit1 for color2, bit2 for color3

    def dfs(idx: int) -> bool:
        if idx == n:
            return True
        v = order[idx]
        # compute available colors from used_mask
        mask = used_mask[v]
        for col in range(1, 4):
            if mask & (1 << (col - 1)):
                continue
            # assign
            colors[v] = col
            # update neighbours' used_mask
            changed = []
            bit = 1 << (col - 1)
            for nb in neigh[v]:
                if colors[nb] == 0:
                    if not (used_mask[nb] & bit):
                        used_mask[nb] |= bit
                        changed.append(nb)
            if dfs(idx + 1):
                return True
            # backtrack
            for nb in changed:
                used_mask[nb] &= ~bit
            colors[v] = 0
        return False

    possible = dfs(0)
    out = sys.stdout
    if not possible:
        out.write("NO")
    else:
        out.write("YES\n")
        out.write(" ".join(str(colors[i]) for i in range(n)))

if __name__ == "__main__":
    solve()