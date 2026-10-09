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

    # recursive search for independent set of exact size k
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def popcnt(x: int) -> int:
        return x.bit_count()

    def dfs(cand: int, need: int) -> int:
        """return mask of chosen vertices of size need, or -1 if impossible"""
        if need == 0:
            return 0
        if popcnt(cand) < need:
            return -1
        # choose a vertex (heuristic: vertex with max degree in cand)
        # simple: take lowest set bit
        v = (cand & -cand).bit_length() - 1

        # try include v
        new_cand = cand & ~adj[v] & ~(1 << v)
        res = dfs(new_cand, need - 1)
        if res != -1:
            return (1 << v) | res

        # try exclude v
        cand2 = cand & ~(1 << v)
        return dfs(cand2, need)

    ans_mask = dfs(ALL, k)
    if ans_mask == -1:
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