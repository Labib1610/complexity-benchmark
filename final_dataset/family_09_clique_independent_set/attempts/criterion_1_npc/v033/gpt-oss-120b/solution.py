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

    # order vertices by degree descending for better pruning
    order = sorted(range(n), key=lambda x: bin(adj[x]).count("1"), reverse=True)
    # map original index to position in ordered list
    pos = [0] * n
    for i, v in enumerate(order):
        pos[v] = i
    # rebuild adjacency in ordered space
    adj2 = [0] * n
    for i in range(n):
        v = order[i]
        mask = 0
        for u in range(n):
            if (adj[v] >> u) & 1:
                mask |= 1 << pos[u]
        adj2[i] = mask

    # recursive search
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def popcnt(x: int) -> int:
        return x.bit_count()

    def dfs(cand_mask: int, size: int, chosen_mask: int):
        # size = current independent set size, chosen_mask records chosen vertices in ordered space
        if size == k:
            # construct answer list in original numbering
            res = []
            for i in range(n):
                if (chosen_mask >> i) & 1:
                    res.append(order[i] + 1)
            return res
        if size + popcnt(cand_mask) < k:
            return None
        # pick a vertex (heuristic: first bit)
        v = (cand_mask & -cand_mask).bit_length() - 1
        # branch: include v
        new_cand = cand_mask & ~adj2[v] & ~(1 << v)
        ans = dfs(new_cand, size + 1, chosen_mask | (1 << v))
        if ans is not None:
            return ans
        # branch: exclude v
        cand_mask ^= 1 << v
        return dfs(cand_mask, size, chosen_mask)

    initial_cand = (1 << n) - 1
    result = dfs(initial_cand, 0, 0)
    if result is None:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, result)))

if __name__ == "__main__":
    solve()