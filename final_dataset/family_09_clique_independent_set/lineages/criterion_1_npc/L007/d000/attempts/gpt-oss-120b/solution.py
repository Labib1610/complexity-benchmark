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

    full_mask = (1 << n) - 1
    target = k
    result_mask = 0
    found = False

    # order vertices by degree (small to large) for better pruning
    order = sorted(range(n), key=lambda x: bin(adj[x]).count("1"))
    # map original index to position in ordered list
    pos_in_order = [0] * n
    for i, v in enumerate(order):
        pos_in_order[v] = i

    # rebuild adjacency in ordered space
    adj_ord = [0] * n
    for i, v in enumerate(order):
        mask = 0
        for u in range(n):
            if (adj[v] >> u) & 1:
                mask |= 1 << pos_in_order[u]
        adj_ord[i] = mask

    # initial candidates: all vertices in ordered space
    all_cand = (1 << n) - 1

    # use stack recursion
    def dfs(cur_mask: int, cand_mask: int, cur_size: int) -> bool:
        nonlocal result_mask, found
        if cur_size == target:
            result_mask = cur_mask
            return True
        # prune
        if cur_size + cand_mask.bit_count() < target:
            return False
        # choose a vertex with smallest degree among candidates
        # simple heuristic: pick first set bit
        v = (cand_mask & -cand_mask).bit_length() - 1
        # branch 1: include v
        new_cand = cand_mask & ~adj_ord[v] & ~(1 << v)
        if dfs(cur_mask | (1 << v), new_cand, cur_size + 1):
            return True
        # branch 2: exclude v
        cand_mask &= ~(1 << v)
        if dfs(cur_mask, cand_mask, cur_size):
            return True
        return False

    if dfs(0, all_cand, 0):
        # translate result_mask back to original vertex numbers
        selected = []
        for i in range(n):
            if (result_mask >> i) & 1:
                selected.append(order[i] + 1)
        print("YES")
        print(" ".join(map(str, selected)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()