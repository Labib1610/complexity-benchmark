import sys
from sys import setrecursionlimit
setrecursionlimit(10000)

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
        if u == v:
            continue
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # color[v] = -1 unassigned, else 0..2
    color = [-1] * n
    # available colors bitmask: bit 0 -> color 1, bit 1 -> color 2, bit 2 -> color 3
    avail = [7] * n
    found = False
    answer = [1] * n

    # undo stack: list of (vertex, old_avail) for avail changes, and (vertex, -1) for color assignment markers
    # Actually we can just save list of modified vertices and restore avail; color set to -1 on undo.
    # We'll implement propagation with a manual stack.

    def assign(v, c, changes):
        """assign color c (0..2) to v, append undo records to changes, propagate singletons.
           returns False if contradiction occurs."""
        stack = [(v, c)]
        while stack:
            x, col = stack.pop()
            if color[x] != -1:
                if color[x] != col:
                    return False
                continue
            # check color is still available
            if not (avail[x] >> col) & 1:
                return False
            color[x] = col
            changes.append((x, avail[x]))  # save old avail for undo
            avail[x] = 1 << col
            # remove col from uncolored neighbors
            nb = adj[x] & ~0  # all neighbors
            # iterate only uncolored neighbors
            mask = nb
            while mask:
                lsb = mask & -mask
                u = (lsb.bit_length() - 1)
                mask ^= lsb
                if color[u] != -1:
                    continue
                if (avail[u] >> col) & 1:
                    changes.append((u, avail[u]))
                    avail[u] &= ~(1 << col)
                    if avail[u] == 0:
                        return False
                    # if singleton, force
                    if avail[u] & (avail[u] - 1) == 0:
                        # determine the single color bit
                        forced_col = (avail[u].bit_length() - 1)
                        stack.append((u, forced_col))
        return True

    def undo(changes):
        for v, old in reversed(changes):
            if old == -1:
                color[v] = -1
            else:
                avail[v] = old

    # We need a marker for color assignment in undo. Simpler: keep separate list of assigned vertices.
    # Let's redesign assign to return list of (vertex, old_avail) for avail changes, and list of assigned vertices.
    # Undo: restore avail for all changed, then color[assigned] = -1.

    sys.setrecursionlimit(10000)
    assigned_stack = []

    def assign2(v, c):
        """returns (success, changed_avails, assigned_vertices)"""
        changed = []
        assigned = []
        stack = [(v, c)]
        while stack:
            x, col = stack.pop()
            if color[x] != -1:
                if color[x] != col:
                    return False, changed, assigned
                continue
            if not ((avail[x] >> col) & 1):
                return False, changed, assigned
            color[x] = col
            assigned.append(x)
            changed.append((x, avail[x]))
            avail[x] = 1 << col
            nb = adj[x]
            mask = nb
            while mask:
                lsb = mask & -mask
                u = lsb.bit_length() - 1
                mask ^= lsb
                if color[u] != -1:
                    continue
                if (avail[u] >> col) & 1:
                    changed.append((u, avail[u]))
                    avail[u] &= ~(1 << col)
                    if avail[u] == 0:
                        return False, changed, assigned
                    if avail[u] & (avail[u] - 1) == 0:
                        fc = avail[u].bit_length() - 1
                        stack.append((u, fc))
        return True, changed, assigned

    def undo2(changed, assigned):
        for v, old in changed:
            avail[v] = old
        for v in assigned:
            color[v] = -1

    # DFS in lexicographic order
    def dfs(pos):
        nonlocal found
        if found:
            return True
        # find next unassigned vertex from pos onward
        while pos < n and color[pos] != -1:
            pos += 1
        if pos == n:
            found = True
            for i in range(n):
                answer[i] = color[i] + 1
            return True
        # try colors in increasing order
        mask = avail[pos]
        # iterate bits in order 0,1,2
        for col in range(3):
            if (mask >> col) & 1:
                ok, changed, assigned = assign2(pos, col)
                if ok:
                    if dfs(pos + 1):
                        return True
                undo2(changed, assigned)
                if found:
                    return True
        return False

    if dfs(0):
        print("YES")
        print(' '.join(map(str, answer)))
    else:
        print("NO")

solve()