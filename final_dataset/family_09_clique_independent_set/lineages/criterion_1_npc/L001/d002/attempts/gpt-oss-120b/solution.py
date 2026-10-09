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

    all_mask = (1 << n) - 1
    answer = []

    # precompute popcount for speed
    popcnt = int.bit_count

    # ordering vertices by degree descending may help
    order = sorted(range(n), key=lambda x: popcnt(adj[x]), reverse=True)
    # map original index to ordered position
    pos = [0] * n
    for i, v in enumerate(order):
        pos[v] = i
    # rebuild adjacency in ordered space
    adj2 = [0] * n
    for i in range(n):
        oi = order[i]
        mask = 0
        for j in range(n):
            if adj[oi] >> order[j] & 1:
                mask |= 1 << j
        adj2[i] = mask

    # initial candidates: all vertices in ordered space
    candidates = (1 << n) - 1
    chosen = []

    found = False

    def dfs(cand_mask: int):
        nonlocal found, answer
        if found:
            return
        if len(chosen) == k:
            # success
            answer = [order[v] + 1 for v in chosen]  # convert back to original numbers
            found = True
            return
        # prune
        if len(chosen) + popcnt(cand_mask) < k:
            return
        # select a vertex (heuristic: vertex with max degree in cand)
        # simple: take first bit
        v = (cand_mask & -cand_mask).bit_length() - 1

        # branch include v
        new_cand = cand_mask & ~adj2[v] & ~(1 << v)
        chosen.append(v)
        dfs(new_cand)
        chosen.pop()
        if found:
            return
        # branch exclude v
        dfs(cand_mask & ~(1 << v))

    dfs(candidates)

    if found:
        print("YES")
        print(' '.join(map(str, answer)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()