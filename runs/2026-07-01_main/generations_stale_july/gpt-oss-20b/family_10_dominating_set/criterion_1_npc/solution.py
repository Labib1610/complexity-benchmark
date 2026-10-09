import sys
sys.setrecursionlimit(10000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    neighbors = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        neighbors[u].append(v)
        neighbors[v].append(u)

    # adjacency mask including self
    adj_mask = [0] * n
    for i in range(n):
        mask = 1 << i
        for v in neighbors[i]:
            mask |= 1 << v
        adj_mask[i] = mask

    all_mask = (1 << n) - 1
    max_cover = max((mask.bit_count() for mask in adj_mask), default=0)

    best = {}

    def dfs(covered, used, chosen):
        if covered == all_mask:
            return chosen
        if used == k:
            return None
        # lower bound pruning
        uncovered = all_mask ^ covered
        uncovered_count = uncovered.bit_count()
        if used + (uncovered_count + max_cover - 1) // max_cover > k:
            return None
        # memoization
        prev = best.get(covered)
        if prev is not None and prev <= used:
            return None
        best[covered] = used
        # pick first uncovered vertex
        v = (uncovered & -uncovered).bit_length() - 1
        cand = [v] + neighbors[v]
        # sort by coverage size descending
        cand.sort(key=lambda u: adj_mask[u].bit_count(), reverse=True)
        for u in cand:
            new_covered = covered | adj_mask[u]
            res = dfs(new_covered, used + 1, chosen + [u])
            if res is not None:
                return res
        return None

    result = dfs(0, 0, [])
    if result is None:
        print("NO")
    else:
        print("YES")
        # output at most k sensors
        out = [str(v + 1) for v in result[:k]]
        print(" ".join(out))

if __name__ == "__main__":
    solve()