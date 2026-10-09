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
    solution = []

    # order vertices by degree descending to improve pruning
    order = sorted(range(n), key=lambda x: bin(adj[x]).count('1'), reverse=True)
    # map original index to position in ordered list
    pos = [0] * n
    for i, v in enumerate(order):
        pos[v] = i
    # rebuild adjacency in ordered space
    adj2 = [0] * n
    for i in range(n):
        v = order[i]
        mask = 0
        for u in range(n):
            if adj[v] >> u & 1:
                mask |= 1 << pos[u]
        adj2[i] = mask

    target_k = k
    found = False

    def dfs(cur_mask: int, cand_mask: int, size: int):
        nonlocal found, solution
        if found:
            return
        if size == target_k:
            # extract vertices from cur_mask
            sol = []
            for i in range(n):
                if cur_mask >> i & 1:
                    sol.append(order[i] + 1)  # back to 1‑based original numbering
            solution = sol
            found = True
            return
        # prune if not enough candidates left
        if size + cand_mask.bit_count() < target_k:
            return
        # choose a vertex (heuristic: highest degree among candidates)
        # simple: pick first set bit
        v = (cand_mask & -cand_mask).bit_length() - 1
        # branch: include v
        new_cand = cand_mask & ~adj2[v] & ~(1 << v)
        dfs(cur_mask | (1 << v), new_cand, size + 1)
        if found:
            return
        # branch: exclude v
        dfs(cur_mask, cand_mask & ~(1 << v), size)

    dfs(0, (1 << n) - 1, 0)

    out = sys.stdout
    if found:
        out.write("YES\n")
        out.write(" ".join(map(str, solution)) + "\n")
    else:
        out.write("NO\n")

if __name__ == "__main__":
    solve()