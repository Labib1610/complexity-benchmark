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

    # vertices ordered by degree (ascending) for better pruning
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

    full_mask = (1 << n) - 1
    answer = []

    # simple recursive search for independent set of size k
    def dfs(cur_mask: int, cand_mask: int):
        nonlocal answer
        if answer:
            return
        cur_size = cur_mask.bit_count()
        if cur_size == k:
            # extract vertices
            ans = []
            for i in range(n):
                if cur_mask >> i & 1:
                    ans.append(order[i] + 1)  # back to 1‑based original numbering
            answer = ans
            return
        # bound check
        if cur_size + cand_mask.bit_count() < k:
            return
        # choose a vertex (heuristic: first in candidates)
        # we can also pick vertex with max degree in candidates to prune faster
        # here simple: pick first
        v = (cand_mask & -cand_mask).bit_length() - 1  # index of least set bit
        # branch 1: include v
        dfs(cur_mask | (1 << v), cand_mask & ~adj2[v] & ~(1 << v))
        # branch 2: exclude v
        dfs(cur_mask, cand_mask & ~(1 << v))

    dfs(0, full_mask)

    if answer:
        print("YES")
        print(" ".join(map(str, answer)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()