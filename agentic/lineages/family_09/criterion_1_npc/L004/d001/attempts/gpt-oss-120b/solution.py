import sys

sys.setrecursionlimit(10000)

def solve() -> None:
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it)); m = int(next(it)); k = int(next(it))
    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    all_vertices = (1 << n) - 1
    solution = []

    # order vertices by degree (small to large) to improve pruning
    order = sorted(range(n), key=lambda x: bin(adj[x]).count("1"))
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

    target_k = k
    found = False

    def dfs(cur_mask: int, cand_mask: int, cur_list):
        nonlocal found, solution
        if found:
            return
        cur_len = len(cur_list)
        if cur_len == target_k:
            solution = cur_list[:]
            found = True
            return
        # prune if not enough candidates left
        if cur_len + cand_mask.bit_count() < target_k:
            return
        # choose a vertex (heuristic: first)
        # pick vertex with smallest degree among candidates
        # simple: take least significant bit
        v = (cand_mask & -cand_mask).bit_length() - 1
        # branch: include v
        dfs(cur_mask | (1 << v), cand_mask & ~adj2[v] & ~(1 << v), cur_list + [order[v] + 1])
        if found:
            return
        # branch: exclude v
        dfs(cur_mask, cand_mask & ~(1 << v), cur_list)

    dfs(0, all_vertices, [])
    out = sys.stdout
    if found:
        out.write("YES\n")
        out.write(" ".join(map(str, solution)) + "\n")
    else:
        out.write("NO\n")

if __name__ == "__main__":
    solve()