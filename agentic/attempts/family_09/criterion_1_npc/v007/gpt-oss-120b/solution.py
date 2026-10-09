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

    # all vertices mask
    all_mask = (1 << n) - 1

    from functools import lru_cache

    @lru_cache(maxsize=None)
    def popcnt(x):
        return x.bit_count()

    # depth‑first search for independent set of size k
    def dfs(cur_mask: int, cur_size: int, cand_mask: int):
        if cur_size == k:
            return cur_mask
        # prune if not enough candidates left
        if cur_size + popcnt(cand_mask) < k:
            return None
        # choose a vertex (heuristic: vertex with max degree in candidates)
        # simple choice: least significant bit
        v = (cand_mask & -cand_mask).bit_length() - 1

        # try to include v
        new_cand = cand_mask & ~adj[v] & ~(1 << v)
        res = dfs(cur_mask | (1 << v), cur_size + 1, new_cand)
        if res is not None:
            return res

        # try to exclude v
        cand_mask_without_v = cand_mask & ~(1 << v)
        return dfs(cur_mask, cur_size, cand_mask_without_v)

    start_mask = 0
    start_size = 0
    candidates = all_mask
    ans_mask = dfs(start_mask, start_size, candidates)

    if ans_mask is None:
        print("NO")
    else:
        res = []
        for i in range(n):
            if ans_mask >> i & 1:
                res.append(str(i + 1))
        print("YES")
        print(" ".join(res))

if __name__ == "__main__":
    solve()