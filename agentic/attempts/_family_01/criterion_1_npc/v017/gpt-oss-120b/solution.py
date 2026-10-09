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

    # order vertices by degree descending
    order = sorted(range(n), key=lambda x: -adj[x].bit_count())
    pos_in_order = [0] * n
    for idx, v in enumerate(order):
        pos_in_order[v] = idx

    colors = [0] * n  # 0 uncolored, else 1..3

    # For fast conflict check, maintain for each vertex a mask of colors used by its colored neighbors
    neighbor_used = [0] * n  # bitmask of colors (bits 1<<c)

    def dfs(idx: int) -> bool:
        if idx == n:
            return True
        v = order[idx]
        # compute forbidden colors from already colored neighbors
        forbidden = neighbor_used[v]
        for c in (1, 2, 3):
            if forbidden & (1 << c):
                continue
            # assign
            colors[v] = c
            # update neighbor_used for uncolored neighbors
            changed = []
            mask = 1 << c
            nb = adj[v]
            while nb:
                u = (nb & -nb).bit_length() - 1
                nb &= nb - 1
                if colors[u] == 0:
                    if not (neighbor_used[u] & mask):
                        neighbor_used[u] |= mask
                        changed.append(u)
            if dfs(idx + 1):
                return True
            # rollback
            for u in changed:
                neighbor_used[u] &= ~mask
            colors[v] = 0
        return False

    if dfs(0):
        print("YES")
        print(' '.join(str(colors[i]) for i in range(n)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()