import sys
from functools import lru_cache

def solve() -> None:
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

    # color: -1 uncolored, 0/1/2
    color = [-1] * n
    color_mask = [0, 0, 0]

    # Precompute popcount helper
    def popcount(x: int) -> int:
        return x.bit_count()

    sys.setrecursionlimit(10000)

    # feasibility test for the current partial coloring
    def feasible() -> bool:
        # choose uncolored vertex with max saturation, tie by degree
        best = -1
        best_sat = -1
        best_deg = -1
        cm = color_mask
        for v in range(n):
            if color[v] != -1:
                continue
            av = adj[v]
            sat = 0
            if av & cm[0]:
                sat += 1
            if av & cm[1]:
                sat += 1
            if av & cm[2]:
                sat += 1
            if sat == 3:
                return False
            deg = popcount(av)
            if sat > best_sat or (sat == best_sat and deg > best_deg):
                best_sat = sat
                best_deg = deg
                best = v
        if best == -1:
            return True

        v = best
        av = adj[v]
        # try colors in order of fewest conflicts? just 0,1,2
        for c in range(3):
            if av & cm[c]:
                continue
            color[v] = c
            color_mask[c] |= 1 << v
            # quick prune: any uncolored vertex now has all 3 colors forbidden?
            ok = True
            new_mask = color_mask[c]
            for w in range(n):
                if color[w] != -1:
                    continue
                aw = adj[w]
                if (aw & color_mask[0]) and (aw & color_mask[1]) and (aw & new_mask):
                    ok = False
                    break
            if ok and feasible():
                color[v] = -1
                color_mask[c] &= ~(1 << v)
                return True
            color[v] = -1
            color_mask[c] &= ~(1 << v)
        return False

    # lexicographically smallest coloring, vertices in order
    for v in range(n):
        chosen = -1
        for c in range(3):
            # conflict with already colored neighbors?
            if adj[v] & color_mask[c]:
                continue
            color[v] = c
            color_mask[c] |= 1 << v
            if feasible():
                chosen = c
                break
            color[v] = -1
            color_mask[c] &= ~(1 << v)
        if chosen == -1:
            print("NO")
            return

    print("YES")
    print(' '.join(str(c + 1) for c in color))

solve()