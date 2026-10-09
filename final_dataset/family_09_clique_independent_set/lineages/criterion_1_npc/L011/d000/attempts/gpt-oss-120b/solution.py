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
    answer = []

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

    target = k
    found = False

    def popcnt(x: int) -> int:
        return x.bit_count()

    def dfs(cur_mask: int, cand_mask: int, cur_list):
        nonlocal found, answer
        if found:
            return
        cur_size = popcnt(cur_mask)
        if cur_size == target:
            answer = [order[i] + 1 for i in cur_list]
            found = True
            return
        # prune if even taking all candidates we cannot reach target
        if cur_size + popcnt(cand_mask) < target:
            return
        # choose a vertex with maximum degree in candidates (heuristic)
        # simple: pick first set bit
        v = (cand_mask & -cand_mask).bit_length() - 1
        # branch: include v
        dfs(cur_mask | (1 << v),
            cand_mask & ~adj2[v] & ~(1 << v),
            cur_list + [v])
        if found:
            return
        # branch: exclude v
        dfs(cur_mask, cand_mask & ~(1 << v), cur_list)

    dfs(0, ALL, [])
    if found:
        print("YES")
        print(" ".join(map(str, answer)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()