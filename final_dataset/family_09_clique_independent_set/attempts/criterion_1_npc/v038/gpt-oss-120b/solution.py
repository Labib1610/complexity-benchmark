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
    solution = []

    # simple recursive backtracking with pruning
    def dfs(cur_mask: int, cand_mask: int, size: int, chosen: list) -> bool:
        if size == k:
            solution.extend(chosen)
            return True
        # not enough vertices left
        if size + cand_mask.bit_count() < k:
            return False
        # choose a vertex (heuristic: vertex with max degree in candidates)
        # pick first vertex
        v = (cand_mask & -cand_mask).bit_length() - 1

        # branch: include v
        new_cand = cand_mask & ~adj[v] & ~(1 << v)
        if dfs(cur_mask | (1 << v), new_cand, size + 1, chosen + [v]):
            return True
        # branch: exclude v
        cand_mask_without_v = cand_mask & ~(1 << v)
        if dfs(cur_mask, cand_mask_without_v, size, chosen):
            return True
        return False

    if dfs(0, ALL, 0, []):
        print("YES")
        print(' '.join(str(x + 1) for x in solution))
    else:
        print("NO")

if __name__ == "__main__":
    solve()