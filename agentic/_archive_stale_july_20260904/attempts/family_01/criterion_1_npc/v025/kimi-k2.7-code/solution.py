import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * n
    bad = False
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            bad = True
            continue
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    if bad:
        print("NO")
        return

    neighbors = [[] for _ in range(n)]
    for u in range(n):
        mask = adj[u]
        while mask:
            lsb = mask & -mask
            v = lsb.bit_length() - 1
            mask ^= lsb
            neighbors[u].append(v)

    degree = [len(neighbors[i]) for i in range(n)]

    popcnt = [0] * 8
    bits = [[] for _ in range(8)]
    single = [-1] * 8
    for mask in range(8):
        cnt = 0
        for c in range(3):
            if mask >> c & 1:
                bits[mask].append(c)
                cnt += 1
        popcnt[mask] = cnt
    for c in range(3):
        single[1 << c] = c

    def propagate(dom, col, stack):
        while stack:
            v = stack.pop()
            cm = 1 << col[v]
            for w in neighbors[v]:
                cw = col[w]
                if cw == -1:
                    if dom[w] & cm:
                        dom[w] &= ~cm
                        if dom[w] == 0:
                            return False
                        c2 = single[dom[w]]
                        if c2 != -1:
                            col[w] = c2
                            dom[w] = 1 << c2
                            stack.append(w)
                elif cw == col[v]:
                    return False
        return True

    def assign_and_propagate(v, c, dom, col, changes):
        changes.append((v, dom[v], col[v]))
        dom[v] = 1 << c
        col[v] = c
        stack = [v]
        while stack:
            x = stack.pop()
            cm = 1 << col[x]
            for w in neighbors[x]:
                cw = col[w]
                if cw == -1:
                    if dom[w] & cm:
                        changes.append((w, dom[w], col[w]))
                        dom[w] &= ~cm
                        if dom[w] == 0:
                            return False
                        c2 = single[dom[w]]
                        if c2 != -1:
                            col[w] = c2
                            dom[w] = 1 << c2
                            stack.append(w)
                elif cw == col[x]:
                    return False
        return True

    def search(dom, col):
        v = -1
        best = 4
        best_deg = -1
        for i in range(n):
            if col[i] == -1:
                pc = popcnt[dom[i]]
                if pc < best or (pc == best and degree[i] > best_deg):
                    best = pc
                    v = i
                    best_deg = degree[i]
        if v == -1:
            return True
        if best == 0:
            return False
        d = dom[v]
        for c in bits[d]:
            changes = []
            if assign_and_propagate(v, c, dom, col, changes):
                if search(dom, col):
                    return True
            for x, old_dom, old_col in reversed(changes):
                dom[x] = old_dom
                col[x] = old_col
        return False

    def can_color(fixed):
        dom = [7] * n
        col = [-1] * n
        stack = []
        for v in range(n):
            c = fixed[v]
            if c != -1:
                dom[v] = 1 << c
                col[v] = c
                stack.append(v)
        if not propagate(dom, col, stack):
            return False
        return search(dom, col)

    if not can_color([-1] * n):
        print("NO")
        return

    ans = [-1] * n
    for i in range(n):
        blocked = 0
        for j in neighbors[i]:
            if ans[j] != -1:
                blocked |= 1 << ans[j]
        chosen = False
        for c in range(3):
            if blocked >> c & 1:
                continue
            ans[i] = c
            if can_color(ans):
                chosen = True
                break
        if not chosen:
            print("NO")
            return

    for u in range(n):
        for v in neighbors[u]:
            if ans[u] == ans[v]:
                print("NO")
                return

    sys.stdout.write("YES\n")
    sys.stdout.write(' '.join(str(x + 1) for x in ans))

solve()