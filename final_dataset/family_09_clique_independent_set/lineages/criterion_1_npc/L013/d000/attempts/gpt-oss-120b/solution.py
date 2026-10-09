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
    result = []

    # backtracking for independent set of size k
    def dfs(cur_mask: int, cand_mask: int) -> bool:
        """cur_mask: vertices already chosen
           cand_mask: vertices that can still be added (no edges to cur)"""
        nonlocal result
        cur_size = cur_mask.bit_count()
        if cur_size == k:
            # extract vertices
            res = []
            for v in range(n):
                if cur_mask >> v & 1:
                    res.append(v + 1)
            result = res
            return True
        # prune
        if cur_size + cand_mask.bit_count() < k:
            return False

        # choose a vertex (simple heuristic: vertex with max degree in candidates)
        # to improve pruning, pick vertex with largest adjacency within candidates
        # compute degrees
        # we can just pick the first vertex
        v = (cand_mask & -cand_mask).bit_length() - 1  # least significant bit
        # branch: include v
        new_cur = cur_mask | (1 << v)
        new_cand = cand_mask & ~adj[v] & ~(1 << v)
        if dfs(new_cur, new_cand):
            return True
        # branch: exclude v
        cand_mask_without_v = cand_mask & ~(1 << v)
        if dfs(cur_mask, cand_mask_without_v):
            return True
        return False

    if dfs(0, all_vertices):
        print("YES")
        print(" ".join(map(str, result)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()