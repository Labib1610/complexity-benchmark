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

    all_vertices = (1 << n) - 1

    # depth‑first search for an independent set of exact size k
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def popcnt(x: int) -> int:
        return x.bit_count()

    def dfs(cur_mask: int, cand_mask: int):
        cur_sz = popcnt(cur_mask)
        if cur_sz == k:
            return cur_mask
        # not enough vertices left
        if cur_sz + popcnt(cand_mask) < k:
            return None
        # pick a vertex (least significant bit)
        v = (cand_mask & -cand_mask).bit_length() - 1

        # branch: include v
        new_cand = cand_mask & ~adj[v] & ~(1 << v)
        res = dfs(cur_mask | (1 << v), new_cand)
        if res is not None:
            return res

        # branch: exclude v
        res = dfs(cur_mask, cand_mask & ~(1 << v))
        return res

    result_mask = dfs(0, all_vertices)
    if result_mask is None:
        print("NO")
    else:
        ans = [str(i + 1) for i in range(n) if (result_mask >> i) & 1]
        print("YES")
        print(" ".join(ans))

if __name__ == "__main__":
    solve()