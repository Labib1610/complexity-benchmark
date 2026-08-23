import sys
from sys import setrecursionlimit
setrecursionlimit(10000)

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

    # Precompute popcount for 0..7
    popcnt = [0] * 8
    for i in range(8):
        popcnt[i] = (i & 1) + popcnt[i >> 1]

    # AC-3 propagation after fixing a vertex to a single color
    def propagate(dom, v, color):
        # dom[v] is already a singleton containing color
        stack = [v]
        while stack:
            x = stack.pop()
            c = dom[x]
            # c is a power of two
            mask = adj[x]
            u = 0
            while mask:
                lsb = mask & -mask
                u = (lsb.bit_length() - 1)
                if dom[u] & c:
                    dom[u] &= ~c
                    if dom[u] == 0:
                        return False
                    if popcnt[dom[u]] == 1:
                        stack.append(u)
                mask ^= lsb
        return True

    # Decide whether current domains allow a proper 3-coloring
    def feasible(dom):
        # Find unassigned vertex with smallest domain size (>1)
        v = -1
        best = 4
        for i in range(n):
            d = dom[i]
            if d not in (1, 2, 4):
                pc = popcnt[d]
                if pc < best:
                    best = pc
                    v = i
                    if pc == 2:
                        pass
        if v == -1:
            # all assigned, check consistency (propagation already ensures it)
            return True
        # try colors in increasing order
        d = dom[v]
        if d & 1:
            nd = dom[:]
            nd[v] = 1
            if propagate(nd, v, 1) and feasible(nd):
                return True
        if d & 2:
            nd = dom[:]
            nd[v] = 2
            if propagate(nd, v, 2) and feasible(nd):
                return True
        if d & 4:
            nd = dom[:]
            nd[v] = 4
            if propagate(nd, v, 4) and feasible(nd):
                return True
        return False

    answer = [0] * n
    dom = [7] * n
    for i in range(n):
        placed = False
        for color_bit, color_id in ((1, 1), (2, 2), (4, 3)):
            nd = dom[:]
            nd[i] = color_bit
            if not propagate(nd, i, color_bit):
                continue
            if feasible(nd):
                answer[i] = color_id
                dom = nd
                placed = True
                break
        if not placed:
            print("NO")
            return

    print("YES")
    print(' '.join(map(str, answer)))

solve()