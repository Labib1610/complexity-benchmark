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

    orig_adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        orig_adj[u] |= 1 << v
        orig_adj[v] |= 1 << u

    all_mask = (1 << n) - 1
    comp_adj = [0] * n
    for v in range(n):
        comp_adj[v] = all_mask ^ (1 << v) ^ orig_adj[v]

    solution_mask = None  # will hold the found clique (independent set)

    # depth‑first search for a clique of size k in the complement graph
    def dfs(cur_mask: int, cand_mask: int) -> bool:
        nonlocal solution_mask
        if solution_mask is not None:
            return True
        cur_sz = cur_mask.bit_count()
        if cur_sz == k:
            solution_mask = cur_mask
            return True
        # not enough vertices left
        if cur_sz + cand_mask.bit_count() < k:
            return False

        # iterate over candidates
        while cand_mask:
            # prune again (may have changed after previous iterations)
            if cur_sz + cand_mask.bit_count() < k:
                break
            # take least significant bit as the next vertex
            v = (cand_mask & -cand_mask).bit_length() - 1
            cand_mask ^= 1 << v
            new_cand = cand_mask & comp_adj[v]
            if dfs(cur_mask | (1 << v), new_cand):
                return True
        return False

    # start with empty set, all vertices are candidates
    dfs(0, (1 << n) - 1)

    if solution_mask is None:
        print("NO")
    else:
        ans = [str(i + 1) for i in range(n) if (solution_mask >> i) & 1]
        print("YES")
        print(" ".join(ans))

if __name__ == "__main__":
    solve()