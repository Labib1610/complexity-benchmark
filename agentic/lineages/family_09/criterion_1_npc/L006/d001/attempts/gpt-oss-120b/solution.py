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
    def dfs(cand_mask: int, cur: list):
        nonlocal solution
        if solution:  # already found
            return
        cur_len = len(cur)
        if cur_len == k:
            # translate back to original numbering
            solution = [order[i] + 1 for i in cur]
            return
        # pruning: not enough candidates left
        if cur_len + cand_mask.bit_count() < k:
            return
        # choose a vertex with max degree in candidates (simple heuristic)
        # pick first set bit
        v = (cand_mask & -cand_mask).bit_length() - 1
        # branch: include v
        dfs(cand_mask & ~adj2[v] & ~(1 << v), cur + [v])
        # branch: exclude v
        dfs(cand_mask & ~(1 << v), cur)

    dfs(ALL, [])
    out = sys.stdout
    if solution:
        out.write("YES\n")
        out.write(" ".join(map(str, solution)) + "\n")
    else:
        out.write("NO\n")

if __name__ == "__main__":
    solve()