import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    ALL = (1 << n) - 1
    solution = []

    # order vertices by degree (small to large) for better pruning
    order = sorted(range(n), key=lambda x: bin(adj[x]).count("1"))
    # map original index to position in ordered list
    pos = [0] * n
    for i, v in enumerate(order):
        pos[v] = i

    # rebuild adjacency according to new order
    adj2 = [0] * n
    for i in range(n):
        v = order[i]
        mask = 0
        for u in range(n):
            if (adj[v] >> u) & 1:
                mask |= 1 << pos[u]
        adj2[i] = mask

    # initial mask: all vertices available (in ordered indexing)
    init_mask = (1 << n) - 1

    # memoization for pruning (optional)
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def popcnt(x: int) -> int:
        return x.bit_count()

    def dfs(mask: int, size: int, chosen: tuple) -> bool:
        # prune if impossible to reach k
        if size + popcnt(mask) < k:
            return False
        if size == k:
            # translate back to original vertex numbers
            sol = [order[i] + 1 for i in chosen]
            solution.extend(sol)
            return True
        # pick a vertex with smallest degree heuristic: first bit
        v = (mask & -mask).bit_length() - 1  # index of least significant set bit
        # branch: include v
        new_mask = mask & ~ (adj2[v] | (1 << v))
        if dfs(new_mask, size + 1, chosen + (v,)):
            return True
        # branch: exclude v
        mask_without_v = mask & ~(1 << v)
        if dfs(mask_without_v, size, chosen):
            return True
        return False

    possible = dfs(init_mask, 0, ())
    if possible:
        print("YES")
        print(" ".join(map(str, solution)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()