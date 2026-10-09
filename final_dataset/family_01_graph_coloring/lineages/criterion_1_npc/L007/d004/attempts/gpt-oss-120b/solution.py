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

    # order vertices by degree descending
    order = sorted(range(n), key=lambda x: bin(adj[x]).count('1'), reverse=True)
    pos_in_order = [0] * n
    for i, v in enumerate(order):
        pos_in_order[v] = i

    # adjacency in order indices for fast check
    adj_order = [0] * n
    for i, v in enumerate(order):
        mask = 0
        nb = adj[v]
        while nb:
            lsb = nb & -nb
            u = (lsb.bit_length() - 1)
            mask |= 1 << pos_in_order[u]
            nb ^= lsb
        adj_order[i] = mask

    colors = [-1] * n  # in order indices
    # bitmask of vertices colored with each color
    col_mask = [0, 0, 0]

    def dfs(idx: int) -> bool:
        if idx == n:
            return True
        # choose vertex idx
        neigh = adj_order[idx]
        # try colors
        for c in range(3):
            if col_mask[c] & neigh:   # conflict with same color neighbor
                continue
            colors[idx] = c
            col_mask[c] |= 1 << idx
            if dfs(idx + 1):
                return True
            col_mask[c] ^= 1 << idx
            colors[idx] = -1
        return False

    possible = dfs(0)
    if not possible:
        print("NO")
        return

    # map back to original vertex order
    ans = [0] * n
    for i, v in enumerate(order):
        ans[v] = colors[i] + 1
    print("YES")
    print(' '.join(map(str, ans)))

if __name__ == "__main__":
    solve()