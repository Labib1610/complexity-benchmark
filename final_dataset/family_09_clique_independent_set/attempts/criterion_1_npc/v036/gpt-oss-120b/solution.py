import sys
sys.setrecursionlimit(1000000)

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

    # order vertices by degree descending for better pruning
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
        for u in range(n):
            if (adj[v] >> u) & 1:
                mask |= 1 << pos[u]
        adj2[i] = mask

    target = k
    found = False

    def dfs(cur_mask: int, cand_mask: int, cur_list):
        nonlocal found, result
        if found:
            return
        cur_size = len(cur_list)
        if cur_size == target:
            found = True
            result = [order[i] + 1 for i in cur_list]
            return
        # prune
        if cur_size + cand_mask.bit_count() < target:
            return
        # choose a vertex (heuristic: first)
        # pick vertex with max degree among candidates
        # simple: take first bit
        v = (cand_mask & -cand_mask).bit_length() - 1
        # branch: include v
        dfs(cur_mask | (1 << v), cand_mask & ~adj2[v] & ~(1 << v), cur_list + [v])
        if found:
            return
        # branch: exclude v
        dfs(cur_mask, cand_mask & ~(1 << v), cur_list)

    dfs(0, (1 << n) - 1, [])
    out = sys.stdout
    if found:
        out.write("YES\n")
        out.write(" ".join(map(str, result)) + "\n")
    else:
        out.write("NO\n")

if __name__ == "__main__":
    solve()