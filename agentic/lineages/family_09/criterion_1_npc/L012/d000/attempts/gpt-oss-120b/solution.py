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

    # ordering vertices by degree (descending) for better branching
    order = sorted(range(n), key=lambda x: bin(adj[x]).count("1"), reverse=True)
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

    ALL = (1 << n) - 1

    # greedy coloring bound for a set of candidates (bitmask)
    def coloring_bound(cand_mask: int) -> int:
        colors = 0
        mask = cand_mask
        while mask:
            colors += 1
            # pick a vertex with smallest degree in mask (heuristic)
            v = (mask & -mask).bit_length() - 1
            # independent set for this color: remove v and its neighbors
            mask &= ~ (adj2[v] | (1 << v))
        return colors

    result = None

    def dfs(cur_mask: int, cand_mask: int, cur_size: int):
        nonlocal result
        if result is not None:
            return True
        if cur_size == k:
            # extract vertices
            res = []
            for i in range(n):
                if cur_mask >> i & 1:
                    res.append(order[i] + 1)
            result = res
            return True
        # prune by simple size bound
        if cur_size + cand_mask.bit_count() < k:
            return False
        # coloring bound
        if cur_size + coloring_bound(cand_mask) < k:
            return False

        # choose a vertex (heuristic: first in cand)
        # we will try include then exclude
        # ordering: pick vertex with max degree in cand to reduce branching
        # compute degrees within cand
        best_v = -1
        best_deg = -1
        temp = cand_mask
        while temp:
            v = (temp & -temp).bit_length() - 1
            deg = (adj2[v] & cand_mask).bit_count()
            if deg > best_deg:
                best_deg = deg
                best_v = v
            temp &= temp - 1
        v = best_v

        # branch: include v
        new_cand = cand_mask & ~ (adj2[v] | (1 << v))
        if dfs(cur_mask | (1 << v), new_cand, cur_size + 1):
            return True
        # branch: exclude v
        cand_mask &= ~(1 << v)
        if dfs(cur_mask, cand_mask, cur_size):
            return True
        return False

    dfs(0, ALL, 0)

    if result is None:
        print("NO")
    else:
        print("YES")
        print(" ".join(map(str, result)))

if __name__ == "__main__":
    solve()