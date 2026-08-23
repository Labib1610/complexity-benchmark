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

    # quick check: any vertex with degree >= 3 is fine, K4 lower bound not needed yet

    color = [-1] * n          # assigned colors, -1 = unassigned
    sat = [0] * n             # bitmask of colors used by colored neighbours
    uncolored_mask = (1 << n) - 1

    # precompute degree for tie breaking
    deg = [bin(a).count('1') for a in adj]

    sys.setrecursionlimit(10000)

    # ---------- exact decision: can the current partial coloring be extended? ----------
    def can_extend() -> bool:
        # DSATUR backtracking with bitset operations
        # local copies of mutable state are passed as arguments to avoid global churn
        c = color[:]          # current colors, -1 = uncolored
        s = sat[:]            # saturation masks
        free = uncolored_mask

        # stack of changes for fast undo
        stack = []

        def assign(v: int, col: int) -> None:
            c[v] = col
            free &= ~(1 << v)
            nb = adj[v]
            changed = []
            w = 0
            while nb:
                lsb = nb & -nb
                u = (lsb.bit_length() - 1)
                nb ^= lsb
                if c[u] == -1:
                    old = s[u]
                    new = old | (1 << col)
                    if new != old:
                        s[u] = new
                        changed.append((u, old))
                w += 1
            stack.append((v, changed))

        def undo() -> None:
            v, changed = stack.pop()
            c[v] = -1
            free |= 1 << v
            for u, old in changed:
                s[u] = old

        # initialize fixed colors
        for v in range(n):
            if c[v] != -1:
                col = c[v]
                # update saturation of uncolored neighbours
                nb = adj[v]
                changed = []
                w = 0
                while nb:
                    lsb = nb & -nb
                    u = (lsb.bit_length() - 1)
                    nb ^= lsb
                    if c[u] == -1:
                        old = s[u]
                        new = old | (1 << col)
                        if new != old:
                            s[u] = new
                            changed.append((u, old))
                stack.append((v, changed))

        # recursive search
        def dfs() -> bool:
            if free == 0:
                return True

            # choose vertex with smallest number of available colours (MRV/DSATUR)
            best_v = -1
            best_options = None
            best_score = 10  # larger than any possible option count

            fm = free
            while fm:
                lsb = fm & -fm
                v = lsb.bit_length() - 1
                fm ^= lsb
                forbid = s[v]
                opts = (~forbid) & 0b111
                cnt = opts.bit_count()
                if cnt == 0:
                    return False
                # tie-break by degree / saturation to reduce branching
                if cnt < best_score or (cnt == best_score and
                                        (s[v].bit_count() > (s[best_v].bit_count() if best_v != -1 else -1) or
                                         deg[v] > deg[best_v])):
                    best_v = v
                    best_options = opts
                    best_score = cnt
                if cnt == 1:
                    break

            v = best_v
            opts = best_options
            # try colours in numeric order is not required for a decision procedure,
            # but a fixed order is fine
            for col in (0, 1, 2):
                if opts & (1 << col):
                    assign(v, col)
                    if dfs():
                        return True
                    undo()
            return False

        return dfs()

    # ---------- greedy construction of lexicographically smallest assignment ----------
    for v in range(n):
        chosen = -1
        for col in (0, 1, 2):
            # conflict with already coloured neighbours?
            conflict = False
            nb = adj[v]
            while nb:
                lsb = nb & -nb
                u = lsb.bit_length() - 1
                nb ^= lsb
                if color[u] == col:
                    conflict = True
                    break
            if conflict:
                continue
            color[v] = col
            # update saturation for can_extend (it reads sat)
            changed = []
            nb = adj[v]
            while nb:
                lsb = nb & -nb
                u = lsb.bit_length() - 1
                nb ^= lsb
                if color[u] == -1:
                    old = sat[u]
                    new = old | (1 << col)
                    sat[u] = new
                    changed.append((u, old))
            uncolored_mask &= ~(1 << v)
            if can_extend():
                chosen = col
                break
            # undo
            color[v] = -1
            uncolored_mask |= 1 << v
            for u, old in changed:
                sat[u] = old
        if chosen == -1:
            print("NO")
            return

    print("YES")
    print(' '.join(str(c + 1) for c in color))

solve()