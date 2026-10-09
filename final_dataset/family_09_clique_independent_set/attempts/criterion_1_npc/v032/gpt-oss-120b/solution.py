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

    all_mask = (1 << n) - 1

    # depth‑first search with pruning
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def dfs(chosen_mask: int, cand_mask: int):
        cur = chosen_mask.bit_count()
        if cur == k:
            return chosen_mask
        if cur + cand_mask.bit_count() < k:
            return None

        # pick the lowest vertex in cand_mask
        v_bit = cand_mask & -cand_mask
        v = (v_bit.bit_length() - 1)

        # include v
        new_cand = cand_mask & ~adj[v] & ~v_bit
        res = dfs(chosen_mask | v_bit, new_cand)
        if res is not None:
            return res

        # exclude v
        return dfs(chosen_mask, cand_mask & ~v_bit)

    result_mask = dfs(0, all_mask)

    if result_mask is None:
        print("NO")
    else:
        ans = [str(i + 1) for i in range(n) if (result_mask >> i) & 1]
        print("YES")
        print(" ".join(ans))

if __name__ == "__main__":
    solve()