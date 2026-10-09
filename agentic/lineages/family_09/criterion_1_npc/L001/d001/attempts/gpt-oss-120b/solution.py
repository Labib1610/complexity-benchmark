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

    # order vertices by degree (small to large) for better pruning
    order = sorted(range(n), key=lambda x: bin(adj[x]).count("1"))
    # map original index to position in ordered list
    pos = [0] * n
    for i, v in enumerate(order):
        pos[v] = i

    # rebuild adjacency in ordered space
    adj2 = [0] * n
    for i in range(n):
        v = order[i]
        mask = 0
        for j in range(n):
            if adj[v] >> order[j] & 1:
                mask |= 1 << j
        adj2[i] = mask

    # recursive search
    def dfs(cand_mask: int, chosen_mask: int, chosen_cnt: int) -> bool:
        nonlocal result
        if chosen_cnt == k:
            # extract vertices
            res = []
            for i in range(n):
                if chosen_mask >> i & 1:
                    res.append(order[i] + 1)
            result = res
            return True
        # prune
        if chosen_cnt + cand_mask.bit_count() < k:
            return False
        # choose a vertex with smallest degree among candidates
        # simple heuristic: pick first set bit
        v = (cand_mask & -cand_mask).bit_length() - 1
        # branch 1: include v
        new_cand = cand_mask & ~((1 << v) | adj2[v])
        if dfs(new_cand, chosen_mask | (1 << v), chosen_cnt + 1):
            return True
        # branch 2: exclude v
        cand_mask &= ~(1 << v)
        if dfs(cand_mask, chosen_mask, chosen_cnt):
            return True
        return False

    dfs(all_vertices, 0, 0)

    if result:
        print("YES")
        print(" ".join(map(str, result)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()