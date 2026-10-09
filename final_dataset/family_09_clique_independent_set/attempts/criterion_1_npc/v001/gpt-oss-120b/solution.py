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

    # order vertices by degree (optional heuristic)
    order = sorted(range(n), key=lambda x: bin(adj[x]).count("1"))
    # map original index to ordered position
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

    # initial candidate set: all vertices
    candidates = (1 << n) - 1
    solution_mask = 0
    found = False

    # use recursion with backtracking
    def dfs(cur_mask: int, cand_mask: int, depth: int) -> bool:
        nonlocal solution_mask, found
        if depth == k:
            solution_mask = cur_mask
            return True
        # pruning
        if depth + cand_mask.bit_count() < k:
            return False
        # choose a vertex (heuristic: take vertex with max degree in cand)
        # simple: take first bit
        while cand_mask:
            v = (cand_mask & -cand_mask).bit_length() - 1  # index of lowest set bit
            # branch: include v
            new_cand = cand_mask & ~adj2[v] & ~(1 << v)
            if dfs(cur_mask | (1 << v), new_cand, depth + 1):
                return True
            # branch: exclude v
            cand_mask &= ~(1 << v)
            # prune after exclusion
            if depth + cand_mask.bit_count() < k:
                return False
        return False

    if dfs(0, candidates, 0):
        # translate back to original numbering
        res = []
        mask = solution_mask
        while mask:
            v = (mask & -mask).bit_length() - 1
            res.append(order[v] + 1)  # original index +1
            mask &= mask - 1
        print("YES")
        print(" ".join(map(str, res)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()