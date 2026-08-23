import sys
from functools import lru_cache

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    adj = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # domains: bitmask colors 1..3 -> bits 1,2,4
    full = 0b111
    # If any edge has both ends forced same? handled during search.
    # Precompute neighbor masks maybe.
    colors = [0] * n  # 0 unassigned, else bit (1<<(c-1))
    order = list(range(n))

    # We will do recursive backtracking in index order, trying colors 1,2,3.
    # Use bitset domains for uncolored vertices to prune.
    dom = [full] * n

    # For speed, maintain arrays.
    ans = [0] * n

    # To speed up, if graph has high-degree vertices, order by index still.
    # We'll implement recursive with early exit when answer found.

    # Precompute single-bit to color number
    bit_to_col = {1:1, 2:2, 4:3}

    found = False

    # We can use simple forward checking.
    sys.setrecursionlimit(10000)

    def dfs(i):
        nonlocal found
        if found:
            return True
        if i == n:
            found = True
            return True
        v = order[i]
        mask = dom[v]
        # If already assigned? In this scheme we assign when recursing.
        # Try colors in order 1,2,3.
        # bit order: 1,2,4 corresponds to colors 1,2,3.
        for bit in (1,2,4):
            if not (mask & bit):
                continue
            c = bit_to_col[bit]
            # assign v color c
            colors[v] = bit
            old_dom = []
            ok = True
            # update neighbors
            nb = adj[v]
            # iterate uncolored neighbors
            uncolored = nb & ~((1<<n)-1)  # not needed
            # We'll loop over vertices.
            for u in range(n):
                if not (nb >> u) & 1:
                    continue
                if colors[u]:
                    if colors[u] == bit:
                        ok = False
                        break
                    continue
                if dom[u] & bit:
                    # save
                    old_dom.append((u, dom[u]))
                    dom[u] &= ~bit
                    if dom[u] == 0:
                        ok = False
                        break
            if ok:
                ans[v] = c
                if dfs(i+1):
                    return True
            # restore
            colors[v] = 0
            for u, d in old_dom:
                dom[u] = d
        return False

    if dfs(0):
        print("YES")
        print(' '.join(map(str, ans)))
    else:
        print("NO")

solve()