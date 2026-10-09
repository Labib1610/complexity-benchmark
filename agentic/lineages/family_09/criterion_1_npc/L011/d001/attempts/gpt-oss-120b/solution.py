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
    for i in range(n):
        adj[i] = 1 << i          # self‑loop, convenient for removal

    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    ALL = (1 << n) - 1

    from functools import lru_cache

    @lru_cache(maxsize=None)
    def popcnt(x: int) -> int:
        return x.bit_count()

    # recursive search
    def dfs(cur: int, cand: int):
        cur_sz = popcnt(cur)
        if cur_sz == k:
            return cur
        if cur_sz + popcnt(cand) < k:
            return None
        # choose a vertex v from cand (least significant bit)
        v = (cand & -cand).bit_length() - 1  # index of lsb
        # branch 1: take v
        new_cand = cand & ~adj[v]
        res = dfs(cur | (1 << v), new_cand)
        if res is not None:
            return res
        # branch 2: skip v
        return dfs(cur, cand & ~(1 << v))

    ans_mask = dfs(0, ALL)
    if ans_mask is None:
        print("NO")
    else:
        print("YES")
        res = []
        for i in range(n):
            if ans_mask >> i & 1:
                res.append(str(i + 1))
        print(" ".join(res))

if __name__ == "__main__":
    solve()