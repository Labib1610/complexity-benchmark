import sys
sys.setrecursionlimit(1000000)

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

    # memoization to avoid recomputation: (cand_mask, need) -> bool
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def dfs(cand_mask: int, need: int) -> bool:
        nonlocal solution
        if need == 0:
            solution = []
            return True
        if cand_mask == 0:
            return False
        if cand_mask.bit_count() < need:
            return False

        # choose a vertex: heuristic - vertex with maximum degree in cand set
        # to reduce branching, we pick the vertex with most neighbors among candidates
        # simple: pick first bit
        v = (cand_mask & -cand_mask).bit_length() - 1

        # branch: include v
        new_cand = cand_mask & ~adj[v] & ~(1 << v)
        if dfs(new_cand, need - 1):
            solution.append(v)
            return True

        # branch: exclude v
        if dfs(cand_mask & ~(1 << v), need):
            return True

        return False

    if dfs(ALL, k):
        print("YES")
        # solution collected in reverse order of inclusion
        print(' '.join(str(v + 1) for v in solution))
    else:
        print("NO")

if __name__ == "__main__":
    solve()