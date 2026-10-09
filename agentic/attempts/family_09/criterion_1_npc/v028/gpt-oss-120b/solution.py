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
    result = []

    # order vertices by degree (small to large) to improve pruning
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

    target = k
    found = False

    def dfs(cur_mask: int, cand_mask: int, size: int):
        nonlocal found, result
        if found:
            return
        if size == target:
            # extract vertices
            res = []
            for i in range(n):
                if cur_mask >> i & 1:
                    res.append(order[i] + 1)  # back to 1‑based original numbering
            result = res
            found = True
            return
        # prune if even taking all candidates we cannot reach target
        if size + cand_mask.bit_count() < target:
            return
        # choose a vertex (heuristic: smallest degree)
        # pick first set bit
        v = (cand_mask & -cand_mask).bit_length() - 1
        # branch: include v
        dfs(cur_mask | (1 << v), cand_mask & ~adj2[v] & ~(1 << v), size + 1)
        if found:
            return
        # branch: exclude v
        dfs(cur_mask, cand_mask & ~(1 << v), size)

    dfs(0, (1 << n) - 1, 0)

    out = sys.stdout
    if found:
        out.write("YES\n")
        out.write(" ".join(map(str, result)) + "\n")
    else:
        out.write("NO\n")

if __name__ == "__main__":
    solve()