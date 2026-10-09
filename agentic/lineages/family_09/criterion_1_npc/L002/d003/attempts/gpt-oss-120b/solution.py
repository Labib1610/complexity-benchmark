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

    # order vertices by degree descending to improve pruning
    order = sorted(range(n), key=lambda x: bin(adj[x]).count("1"), reverse=True)
    # map original index to position in ordered list
    pos = [0] * n
    for i, v in enumerate(order):
        pos[v] = i

    # rebuild adjacency in ordered space
    adj2 = [0] * n
    for i, v in enumerate(order):
        mask = 0
        for u in range(n):
            if (adj[v] >> u) & 1:
                mask |= 1 << pos[u]
        adj2[i] = mask

    # recursive search
    def dfs(idx: int, chosen_mask: int, cand_mask: int, chosen_list):
        nonlocal solution
        if solution:
            return
        cur_sz = len(chosen_list)
        if cur_sz == k:
            solution = chosen_list[:]
            return
        # not enough vertices left
        if cur_sz + cand_mask.bit_count() < k:
            return
        # select next vertex: first set bit in cand_mask
        # heuristic: pick vertex with maximum degree among candidates
        # simple: pick first
        v = (cand_mask & -cand_mask).bit_length() - 1

        # branch: include v
        new_cand = cand_mask & ~adj2[v] & ~(1 << v)
        dfs(idx + 1, chosen_mask | (1 << v), new_cand, chosen_list + [order[v] + 1])

        # branch: exclude v
        cand_mask_without_v = cand_mask & ~(1 << v)
        dfs(idx + 1, chosen_mask, cand_mask_without_v, chosen_list)

    initial_cand = (1 << n) - 1
    dfs(0, 0, initial_cand, [])

    out = sys.stdout
    if solution:
        out.write("YES\n")
        out.write(" ".join(map(str, solution)))
    else:
        out.write("NO")

if __name__ == "__main__":
    solve()