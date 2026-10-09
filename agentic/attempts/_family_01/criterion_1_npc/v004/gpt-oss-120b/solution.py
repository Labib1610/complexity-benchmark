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
    for idx, v in enumerate(order):
        pos_in_order[v] = idx

    # remap adjacency to order indices
    adj_order = [0] * n
    for i, v in enumerate(order):
        mask = adj[v]
        # keep only bits of vertices that appear later in order
        later = 0
        for j in range(i + 1, n):
            later |= 1 << j if (mask >> order[j]) & 1 else 0
        adj_order[i] = later

    colors = [0] * n  # colors in order indices, 0=uncolored

    def dfs(idx: int) -> bool:
        if idx == n:
            return True
        # try colors 1..3
        forbidden = 0
        # check already colored neighbors (only earlier ones)
        for j in range(idx):
            if (adj_order[j] >> idx) & 1:
                forbidden |= 1 << colors[j]
        for c in (1, 2, 3):
            if not (forbidden >> c) & 1:
                colors[idx] = c
                if dfs(idx + 1):
                    return True
                colors[idx] = 0
        return False

    if dfs(0):
        # map back to original vertex order
        ans = [0] * n
        for i, v in enumerate(order):
            ans[v] = colors[i]
        print("YES")
        print(' '.join(map(str, ans)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()