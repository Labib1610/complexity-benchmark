import sys

def solve() -> None:
    sys.setrecursionlimit(1000000)
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj_mask = [0] * n
    bad = False
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            bad = True
        else:
            adj_mask[u] |= 1 << v
            adj_mask[v] |= 1 << u

    if bad:
        print("NO")
        return

    adj = [[] for _ in range(n)]
    for u in range(n):
        mask = adj_mask[u]
        while mask:
            lsb = mask & -mask
            v = lsb.bit_length() - 1
            adj[u].append(v)
            mask ^= lsb

    # find connected components
    visited = 0
    components = []
    for v in range(n):
        if not (visited >> v) & 1:
            stack = [v]
            visited |= 1 << v
            comp = []
            while stack:
                x = stack.pop()
                comp.append(x)
                nb = adj_mask[x] & ~visited
                while nb:
                    lsb = nb & -nb
                    y = lsb.bit_length() - 1
                    visited |= lsb
                    stack.append(y)
                    nb ^= lsb
            comp.sort()
            components.append(comp)

    # assign color c (1/2/3) to vertex v and propagate forced assignments
    def assign(v, c, record, col, avail):
        cb = 1 << (c - 1)
        if col[v]:
            return col[v] == c
        if not (avail[v] & cb):
            return False
        record.append((v, 0, avail[v]))
        col[v] = c
        avail[v] = cb
        for u in adj[v]:
            if col[u] == 0:
                if avail[u] & cb:
                    record.append((u, 0, avail[u]))
                    avail[u] &= ~cb
                    if avail[u] == 0:
                        return False
                    if avail[u] & (avail[u] - 1) == 0:
                        if not assign(u, avail[u].bit_length(), record, col, avail):
                            return False
        return True

    def undo(record, col, avail):
        for v, old_col, old_avail in reversed(record):
            col[v] = old_col
            avail[v] = old_avail

    # DSATUR existence test for a component
    def colorable(comp):
        col = [0] * n
        avail = [7] * n

        def dfs():
            v = -1
            minsize = 4
            best_deg = -1
            for x in comp:
                if col[x] == 0:
                    s = avail[x].bit_count()
                    if s < minsize or (s == minsize and len(adj[x]) > best_deg):
                        minsize = s
                        v = x
                        best_deg = len(adj[x])
            if v == -1:
                return True
            if avail[v] == 0:
                return False
            for cb in (1, 2, 4):
                if avail[v] & cb:
                    c = cb.bit_length()
                    rec = []
                    if assign(v, c, rec, col, avail):
                        if dfs():
                            return True
                        undo(rec, col, avail)
            return False

        return dfs()

    # find lexicographically smallest coloring of a component
    def lex_component(comp):
        k = len(comp)
        col = [0] * n
        avail = [7] * n
        order = comp

        def dfs(pos):
            while pos < k and col[order[pos]]:
                pos += 1
            if pos == k:
                return True
            v = order[pos]
            mask = avail[v]
            if mask == 0:
                return False
            for cb in (1, 2, 4):
                if mask & cb:
                    c = cb.bit_length()
                    rec = []
                    if assign(v, c, rec, col, avail):
                        if dfs(pos + 1):
                            return True
                        undo(rec, col, avail)
            return False

        if dfs(0):
            return [col[v] for v in comp]
        return None

    ans = [0] * n
    for comp in components:
        if not colorable(comp):
            print("NO")
            return

    for comp in components:
        colors = lex_component(comp)
        if colors is None:
            print("NO")
            return
        for v, c in zip(comp, colors):
            ans[v] = c

    print("YES")
    print(' '.join(map(str, ans)))

solve()