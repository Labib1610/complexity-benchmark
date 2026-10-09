import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # order vertices by degree descending for better pruning
    order = sorted(range(n), key=lambda x: -adj[x].bit_count())
    pos_in_order = [0] * n
    for i, v in enumerate(order):
        pos_in_order[v] = i

    colors = [-1] * n  # 0,1,2

    # neighbor colors mask for each vertex
    neigh_color_mask = [0] * n  # bit i set if neighbor has color i

    def dfs(idx: int) -> bool:
        if idx == n:
            return True
        v = order[idx]
        # try colors 0,1,2
        for c in range(3):
            if neigh_color_mask[v] & (1 << c):
                continue
            # assign
            colors[v] = c
            # update neighbors' masks
            changed = []
            nb = adj[v]
            while nb:
                u = (nb & -nb).bit_length() - 1
                nb &= nb - 1
                if colors[u] == -1:
                    if not (neigh_color_mask[u] & (1 << c)):
                        neigh_color_mask[u] |= 1 << c
                        changed.append(u)
            if dfs(idx + 1):
                return True
            # rollback
            for u in changed:
                neigh_color_mask[u] &= ~(1 << c)
            colors[v] = -1
        return False

    if dfs(0):
        out = ['YES', ' '.join(str(c + 1) for c in colors)]
    else:
        out = ['NO']
    sys.stdout.write('\n'.join(out))

if __name__ == "__main__":
    solve()