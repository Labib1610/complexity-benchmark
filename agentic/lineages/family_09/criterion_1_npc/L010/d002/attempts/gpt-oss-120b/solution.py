import sys

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
    sys.setrecursionlimit(10000)
    answer = None

    # order vertices by degree descending for better pruning
    order = sorted(range(n), key=lambda x: bin(adj[x]).count('1'), reverse=True)
    # map from position in ordered list to original vertex
    pos2v = order
    # remap adjacency to ordered indices
    new_adj = [0] * n
    idx = {v: i for i, v in enumerate(order)}
    for i, v in enumerate(order):
        mask = 0
        for u in range(n):
            if (adj[v] >> u) & 1:
                mask |= 1 << idx[u]
        new_adj[i] = mask

    def dfs(cand_mask: int, cur_mask: int, cur_sz: int):
        nonlocal answer
        if answer is not None:
            return
        if cur_sz == k:
            # translate back to original labels
            res = []
            for i in range(n):
                if (cur_mask >> i) & 1:
                    res.append(pos2v[i] + 1)
            answer = res
            return
        # prune
        if cur_sz + cand_mask.bit_count() < k:
            return
        # choose a vertex (heuristic: first set bit)
        v = (cand_mask & -cand_mask).bit_length() - 1
        # branch: include v
        dfs(cand_mask & ~new_adj[v] & ~(1 << v), cur_mask | (1 << v), cur_sz + 1)
        # branch: exclude v
        dfs(cand_mask & ~(1 << v), cur_mask, cur_sz)

    dfs((1 << n) - 1, 0, 0)

    out = []
    if answer is None:
        out.append("NO")
    else:
        out.append("YES")
        out.append(" ".join(map(str, answer)))
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()