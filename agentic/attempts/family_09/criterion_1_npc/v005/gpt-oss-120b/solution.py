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

    # memoization could be added, but simple backtrack works for n<=46
    from functools import lru_cache

    @lru_cache(maxsize=None)
    def dfs(mask: int, taken: int):
        # mask: available vertices
        # taken: number of vertices already chosen
        if taken == k:
            return 0  # success, empty suffix
        if mask == 0:
            return None
        # pruning: not enough vertices left
        if taken + mask.bit_count() < k:
            return None

        # choose a vertex (least significant bit)
        v = (mask & -mask).bit_length() - 1

        # Try to include v
        new_mask = mask & ~adj[v] & ~(1 << v)
        res = dfs(new_mask, taken + 1)
        if res is not None:
            # encode chosen vertices in result bits
            return (1 << v) | res

        # Exclude v
        return dfs(mask & ~(1 << v), taken)

    result_bits = dfs(all_vertices, 0)
    if result_bits is None:
        print("NO")
    else:
        ans = []
        for i in range(n):
            if result_bits >> i & 1:
                ans.append(str(i + 1))
                if len(ans) == k:
                    break
        print("YES")
        print(" ".join(ans))

if __name__ == "__main__":
    solve()