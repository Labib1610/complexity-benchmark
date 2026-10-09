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
    sys.setrecursionlimit(10000)

    from functools import lru_cache

    @lru_cache(maxsize=None)
    def popcnt(x: int) -> int:
        return x.bit_count()

    # depth‑first search with pruning
    def dfs(chosen_mask: int, avail_mask: int) -> int:
        # chosen_mask holds vertices already selected
        cnt = popcnt(chosen_mask)
        if cnt == k:
            return chosen_mask
        # not enough vertices left
        if cnt + popcnt(avail_mask) < k:
            return -1
        # pick a vertex (lowest set bit)
        v = (avail_mask & -avail_mask).bit_length() - 1
        # branch 1: take v
        new_chosen = chosen_mask | (1 << v)
        new_avail = avail_mask & ~((1 << v) | adj[v])
        res = dfs(new_chosen, new_avail)
        if res != -1:
            return res
        # branch 2: skip v
        return dfs(chosen_mask, avail_mask & ~(1 << v))

    result_mask = dfs(0, ALL)
    if result_mask == -1:
        print("NO")
    else:
        ans = [str(i + 1) for i in range(n) if (result_mask >> i) & 1]
        print("YES")
        print(" ".join(ans))

if __name__ == "__main__":
    solve()