import sys
from sys import setrecursionlimit
setrecursionlimit(1000000)

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

    # feasibility test for a partial assignment:
    # color[i] = -1 (free) or 0/1/2; forbidden[i] is bitmask of colors already used by colored neighbours.
    def feasible(forbidden, uncolored_mask):
        # stack of states for backtracking
        # state: (forbidden tuple? too slow). Use lists and manual save/restore.
        # We'll use recursion with copying of small lists? n<=40, copying list of length n is cheap.
        # But we may call feasible many times, so implement iterative recursion with copy.
        # Use local variables for speed.
        forb = list(forbidden)
        mask = uncolored_mask
        # unit propagation queue
        # assign color c to vertex v means forb[v] becomes (1<<c) and mask cleared.
        # We maintain that forb[v] never zero for uncolored vertices.
        # propagate:
        stack = [(forb, mask)]
        while stack:
            forb, mask = stack.pop()
            if mask == 0:
                return True
            # unit propagation
            changed = True
            while changed:
                changed = False
                # find vertices with only one allowed color
                v = 0
                mm = mask
                while mm:
                    lsb = mm & -mm
                    i = (lsb.bit_length() - 1)
                    if forb[i] & (forb[i] - 1) == 0 and forb[i] != 0:
                        # single color
                        c = (forb[i].bit_length() - 1)
                        # assign i color c
                        mask &= ~(1 << i)
                        # remove c from uncolored neighbors
                        nb = adj[i] & mask
                        while nb:
                            lsb2 = nb & -nb
                            j = (lsb2.bit_length() - 1)
                            if (forb[j] >> c) & 1:
                                forb[j] &= ~(1 << c)
                                if forb[j] == 0:
                                    break
                                if forb[j] & (forb[j] - 1) == 0:
                                    changed = True
                            nb &= nb - 1
                        else:
                            changed = True
                            continue
                        # conflict
                        break
                    mm &= mm - 1
                else:
                    continue
                # conflict occurred
                break
            else:
                # no conflict and no more unit propagation
                if mask == 0:
                    return True
                # choose vertex with smallest domain (>=2)
                v = -1
                best = 4
                mm = mask
                while mm:
                    lsb = mm & -mm
                    i = (lsb.bit_length() - 1)
                    cnt = forb[i].bit_count()
                    if cnt < best:
                        best = cnt
                        v = i
                        if cnt == 2:
                            break
                    mm &= mm - 1
                if v == -1 or best == 0:
                    continue  # infeasible branch
                # branch on colors of v
                # try colors in some order; for pure feasibility any order, but try 0,1,2
                av = forb[v]
                # push branches
                # To reduce memory, we can loop and push copies.
                # But recursion depth <= n, copying list each branch O(n) -> fine.
                c = 0
                while av:
                    if av & 1:
                        nforb = forb.copy()
                        nmask = mask
                        nforb[v] = 1 << c
                        nmask &= ~(1 << v)
                        # propagate removal of c from neighbors
                        nb = adj[v] & nmask
                        ok = True
                        while nb:
                            lsb2 = nb & -nb
                            j = (lsb2.bit_length() - 1)
                            if (nforb[j] >> c) & 1:
                                nforb[j] &= ~(1 << c)
                                if nforb[j] == 0:
                                    ok = False
                                    break
                            nb &= nb - 1
                        if ok:
                            stack.append((nforb, nmask))
                    av >>= 1
                    c += 1
        return False

    # initial feasibility with no colors assigned
    init_forb = [7] * n  # bits 0,1,2 allowed
    init_mask = (1 << n) - 1
    if not feasible(init_forb, init_mask):
        print("NO")
        return

    ans = [0] * n
    forbidden = [7] * n
    uncolored = (1 << n) - 1

    for i in range(n):
        placed = False
        for c in range(3):
            # check if color c is allowed for i given current colored neighbors
            if not ((forbidden[i] >> c) & 1):
                continue
            # tentatively assign i = c
            nforb = forbidden.copy()
            nmask = uncolored & ~(1 << i)
            nforb[i] = 1 << c
            ok = True
            nb = adj[i] & nmask
            while nb:
                lsb = nb & -nb
                j = (lsb.bit_length() - 1)
                if (nforb[j] >> c) & 1:
                    nforb[j] &= ~(1 << c)
                    if nforb[j] == 0:
                        ok = False
                        break
                nb &= nb - 1
            if not ok:
                continue
            if feasible(nforb, nmask):
                ans[i] = c
                forbidden = nforb
                uncolored = nmask
                placed = True
                break
        if not placed:
            # should not happen
            print("NO")
            return

    print("YES")
    print(' '.join(str(x + 1) for x in ans))

solve()