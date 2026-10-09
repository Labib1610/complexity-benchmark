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
    result_mask = None

    # depth‑first search for an independent set of size k
    def dfs(cur_mask: int, cand_mask: int) -> bool:
        nonlocal result_mask
        cur_sz = cur_mask.bit_count()
        if cur_sz == k:
            result_mask = cur_mask
            return True
        # prune if even taking all candidates we cannot reach k
        if cur_sz + cand_mask.bit_count() < k:
            return False
        # choose a vertex (heuristic: vertex with max degree in candidates)
        # simple: take lowest set bit
        v = (cand_mask & -cand_mask).bit_length() - 1

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

    dfs(0, ALL)

    if result_mask is None:
        print("NO")
    else:
        ans = [str(i + 1) for i in range(n) if (result_mask >> i) & 1]
        print("YES")
        print(" ".join(ans))

if __name__ == "__main__":
    solve()