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

    # order vertices by degree descending to improve pruning
    order = sorted(range(n), key=lambda x: bin(adj[x]).count("1"), reverse=True)
    # map original index to position in ordered list
    pos = [0] * n
    for i, v in enumerate(order):
        pos[v] = i
    # rebuild adjacency in ordered space
    adj2 = [0] * n
    for i, v in enumerate(order):
        mask = 0
        for u in range(n):
            if (adj[v] >> u) & 1:
                mask |= 1 << pos[u]
        adj2[i] = mask

    target = k
    solution = None

    from functools import lru_cache

    @lru_cache(maxsize=None)
    def popcnt(x: int) -> int:
        return x.bit_count()

    def dfs(cur_mask: int, cand_mask: int) -> bool:
        nonlocal solution
        cur_sz = popcnt(cur_mask)
        if cur_sz == target:
            # extract vertices
            res = []
            for i in range(n):
                if (cur_mask >> i) & 1:
                    res.append(order[i] + 1)  # back to 1‑based original numbering
            solution = res
            return True
        # prune
        if cur_sz + popcnt(cand_mask) < target:
            return False
        # choose a vertex (heuristic: first bit)
        v = (cand_mask & -cand_mask).bit_length() - 1
        # branch: include v
        new_cand = cand_mask & ~adj2[v] & ~(1 << v)
        if dfs(cur_mask | (1 << v), new_cand):
            return True
        # branch: exclude v
        if dfs(cur_mask, cand_mask & ~(1 << v)):
            return True
        return False

    initial_cand = ALL
    dfs(0, initial_cand)

    if solution is None:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, solution)))

if __name__ == "__main__":
    solve()