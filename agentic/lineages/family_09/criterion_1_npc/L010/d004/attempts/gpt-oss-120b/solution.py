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

    # trivial case: empty graph
    if m == 0:
        if k <= n:
            print("YES")
            print(' '.join(str(i + 1) for i in range(k)))
        else:
            print("NO")
        return

    full_mask = (1 << n) - 1
    result = []
    found = False

    # choose vertex with maximal degree inside current candidates
    def choose_vertex(mask: int) -> int:
        best = -1
        best_deg = -1
        mm = mask
        while mm:
            v = (mm & -mm).bit_length() - 1
            deg = (adj[v] & mask).bit_count()
            if deg > best_deg:
                best_deg = deg
                best = v
            mm &= mm - 1
        return best

    def dfs(cand_mask: int, chosen):
        nonlocal found, result
        if found:
            return
        if len(chosen) == k:
            found = True
            result = chosen[:]
            return
        # prune
        if cand_mask.bit_count() + len(chosen) < k:
            return

        v = choose_vertex(cand_mask)
        # branch: take v
        new_cand = cand_mask & ~adj[v] & ~(1 << v)
        chosen.append(v)
        dfs(new_cand, chosen)
        if found:
            return
        chosen.pop()
        # branch: skip v
        dfs(cand_mask & ~(1 << v), chosen)

    dfs(full_mask, [])

    if found:
        print("YES")
        print(' '.join(str(x + 1) for x in result))
    else:
        print("NO")

if __name__ == "__main__":
    solve()