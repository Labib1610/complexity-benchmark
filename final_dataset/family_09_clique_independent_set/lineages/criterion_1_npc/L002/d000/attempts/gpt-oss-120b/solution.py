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

    # depth‑first search with pruning
    def dfs(selected, candidates):
        """return list of vertices (0‑based) of size k, or None"""
        if len(selected) == k:
            return selected
        # not enough vertices left
        if len(selected) + candidates.bit_count() < k:
            return None
        # pick a vertex (least significant bit)
        v = (candidates & -candidates).bit_length() - 1

        # 1) try to take v
        new_cand = candidates & ~adj[v] & ~(1 << v)
        res = dfs(selected + [v], new_cand)
        if res is not None:
            return res

        # 2) skip v
        return dfs(selected, candidates & ~(1 << v))

    answer = dfs([], ALL)

    out = []
    if answer is None:
        out.append("NO")
    else:
        out.append("YES")
        # convert to 1‑based identifiers
        out.append(" ".join(str(v + 1) for v in answer))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()