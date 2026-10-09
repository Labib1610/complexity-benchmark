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

    # quick K4 detection -> impossible
    for a in range(n):
        na = adj[a]
        # iterate neighbors b > a
        bmask = na & ~((1 << (a + 1)) - 1)
        b = (bmask & -bmask).bit_length() - 1
        while bmask:
            bmask &= bmask - 1
            nb = adj[b] & na
            # common neighbors c > b
            cmask = nb & ~((1 << (b + 1)) - 1)
            c = (cmask & -cmask).bit_length() - 1
            while cmask:
                cmask &= cmask - 1
                nc = adj[c] & nb
                if nc & ~((1 << (c + 1)) - 1):
                    print("NO")
                    return
                # next c
                if cmask:
                    c = (cmask & -cmask).bit_length() - 1

    # domains: bitmask of available colors (bit0=color1, bit1=color2, bit2=color3)
    dom = [7] * n
    color = [0] * n
    assigned = 0

    # undo stack stores (vertex, old_domain) for domain changes
    stack = []

    def assign(v: int, c: int) -> bool:
        nonlocal assigned
        # c is 0-based color bit
        mask = 1 << c
        if not (dom[v] & mask):
            return False
        color[v] = c + 1
        assigned |= 1 << v
        # save current domain and set to chosen color
        stack.append((v, dom[v]))
        dom[v] = mask
        # propagate removal of c from neighbors
        q = []
        umask = adj[v]
        while umask:
            lsb = umask & -umask
            u = lsb.bit_length() - 1
            umask &= umask - 1
            if assigned & (1 << u):
                if color[u] == c + 1:
                    return False
                continue
            if dom[u] & mask:
                stack.append((u, dom[u]))
                dom[u] &= ~mask
                if dom[u] == 0:
                    return False
                if dom[u] & (dom[u] - 1) == 0:  # single color left
                    q.append(u)
        # process forced queue
        qi = 0
        while qi < len(q):
            u = q[qi]
            qi += 1
            if assigned & (1 << u):
                continue
            du = dom[u]
            # determine the only remaining color
            cu = (du & -du).bit_length() - 1
            color[u] = cu + 1
            assigned |= 1 << u
            stack.append((u, dom[u]))
            dom[u] = du
            wmask = adj[u]
            while wmask:
                lsb = wmask & -wmask
                w = lsb.bit_length() - 1
                wmask &= wmask - 1
                if assigned & (1 << w):
                    if color[w] == cu + 1:
                        return False
                    continue
                if dom[w] & (1 << cu):
                    stack.append((w, dom[w]))
                    dom[w] &= ~(1 << cu)
                    if dom[w] == 0:
                        return False
                    if dom[w] & (dom[w] - 1) == 0:
                        q.append(w)
        return True

    def undo(mark: int) -> None:
        nonlocal assigned
        while len(stack) > mark:
            v, old = stack.pop()
            dom[v] = old
            if old != (1 << (color[v] - 1)):
                # this was an assignment (domain narrowed to one color)
                assigned &= ~(1 << v)
                color[v] = 0

    def dfs(pos: int) -> bool:
        # find next unassigned vertex in index order
        while pos < n and (assigned & (1 << pos)):
            pos += 1
        if pos == n:
            return True
        d = dom[pos]
        # try available colors in increasing order
        for c in range(3):
            if d & (1 << c):
                mark = len(stack)
                if assign(pos, c):
                    if dfs(pos + 1):
                        return True
                undo(mark)
        return False

    if dfs(0):
        print("YES")
        print(' '.join(map(str, color)))
    else:
        print("NO")

solve()