import sys

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
    # initial candidates: all vertices
    sys.setrecursionlimit(10000)

    # order vertices by degree descending for better pruning
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

    # recursive search
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def dfs(cand_mask: int, need: int):
        if need == 0:
            return 0  # empty set representation
        if cand_mask == 0:
            return None
        # bound
        if cand_mask.bit_count() < need:
            return None
        # choose a vertex: pick the one with highest degree in candidates
        # simple: take least significant bit
        v = (cand_mask & -cand_mask).bit_length() - 1
        # branch include v
        new_cand = cand_mask & ~adj2[v] & ~(1 << v)
        res = dfs(new_cand, need - 1)
        if res is not None:
            return (1 << v) | res
        # branch exclude v
        res = dfs(cand_mask & ~(1 << v), need)
        if res is not None:
            return res
        return None

    full_mask = (1 << n) - 1
    ans_mask = dfs(full_mask, k)
    if ans_mask is None:
        print("NO")
        return
    # translate back to original indices
    result = []
    for i in range(n):
        if (ans_mask >> i) & 1:
            result.append(order[i] + 1)
    print("YES")
    print(" ".join(map(str, result)))

if __name__ == "__main__":
    solve()