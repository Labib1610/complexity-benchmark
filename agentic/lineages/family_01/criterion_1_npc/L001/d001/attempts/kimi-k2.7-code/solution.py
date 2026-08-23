import sys

sys.setrecursionlimit(1000000)


def solve_component(comp, adj_global):
    k = len(comp)
    if k == 1:
        return [1]

    idx = {v: i for i, v in enumerate(comp)}
    comp_mask = 0
    for v in comp:
        comp_mask |= 1 << v

    adj = [0] * k
    for i, v in enumerate(comp):
        mask = 0
        bits = adj_global[v]
        while bits:
            lsb = bits & -bits
            u = lsb.bit_length() - 1
            if comp_mask >> u & 1:
                mask |= 1 << idx[u]
            bits ^= lsb
        adj[i] = mask

    def is_colorable(fixed):
        forbid = [0] * k
        for i in range(k):
            c = fixed[i]
            if c:
                bit = 1 << (c - 1)
                bits = adj[i]
                while bits:
                    lsb = bits & -bits
                    j = lsb.bit_length() - 1
                    if fixed[j] == c:
                        return False
                    if fixed[j] == 0:
                        forbid[j] |= bit
                    bits ^= lsb

        mask = 0
        for i in range(k):
            if fixed[i] == 0:
                mask |= 1 << i

        ad = adj
        forb = forbid

        def dfs(mask):
            if mask == 0:
                return True

            v = (mask & -mask).bit_length() - 1
            comp_mask_local = 0
            stack = [v]
            seen = 0
            while stack:
                x = stack.pop()
                if seen >> x & 1:
                    continue
                seen |= 1 << x
                new = ad[x] & mask & ~seen
                while new:
                    lsb = new & -new
                    stack.append(lsb.bit_length() - 1)
                    new ^= lsb
            comp_mask_local = seen

            if comp_mask_local != mask:
                if not dfs(comp_mask_local):
                    return False
                return dfs(mask ^ comp_mask_local)

            best_v = -1
            best_cnt = 4
            best_deg = -1
            m = mask
            while m:
                lsb = m & -m
                u = lsb.bit_length() - 1
                allowed = 7 ^ forb[u]
                cnt = allowed.bit_count()
                if cnt == 0:
                    return False
                deg = (ad[u] & mask).bit_count()
                if cnt < best_cnt or (cnt == best_cnt and deg > best_deg):
                    best_cnt = cnt
                    best_deg = deg
                    best_v = u
                    if cnt == 1:
                        break
                m ^= lsb

            v = best_v
            allowed = 7 ^ forb[v]
            bits_col = allowed
            while bits_col:
                bit = bits_col & -bits_col
                changed = []
                ok = True
                nb = ad[v] & mask
                mm = nb
                while mm:
                    lsb = mm & -mm
                    u = lsb.bit_length() - 1
                    if not (forb[u] & bit):
                        forb[u] |= bit
                        changed.append(u)
                        if forb[u] == 7:
                            ok = False
                            break
                    mm ^= lsb
                if ok:
                    if dfs(mask ^ (1 << v)):
                        return True
                for u in changed:
                    forb[u] ^= bit
                bits_col ^= bit
            return False

        return dfs(mask)

    fixed = [0] * k
    colors = [0] * k
    fixed[0] = 1
    colors[0] = 1

    if not is_colorable(fixed):
        return None

    for pos in range(1, k):
        v = pos
        found = False
        for c in (1, 2, 3):
            conflict = False
            bits = adj[v]
            while bits:
                lsb = bits & -bits
                u = lsb.bit_length() - 1
                if fixed[u] and colors[u] == c:
                    conflict = True
                    break
                bits ^= lsb
            if conflict:
                continue
            fixed[v] = c
            colors[v] = c
            if is_colorable(fixed):
                found = True
                break
            fixed[v] = 0
            colors[v] = 0
        if not found:
            return None

    return colors


def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj_global = [0] * n
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj_global[u] |= 1 << v
        adj_global[v] |= 1 << u

    visited = 0
    components = []
    for v in range(n):
        if visited >> v & 1:
            continue
        comp_mask = 0
        stack = [v]
        visited |= 1 << v
        while stack:
            x = stack.pop()
            comp_mask |= 1 << x
            new = adj_global[x] & ~visited
            while new:
                lsb = new & -new
                y = lsb.bit_length() - 1
                visited |= lsb
                stack.append(y)
                new ^= lsb
        comp = []
        bits = comp_mask
        while bits:
            lsb = bits & -bits
            comp.append(lsb.bit_length() - 1)
            bits ^= lsb
        components.append(comp)

    answer = [0] * n
    for comp in components:
        colors = solve_component(comp, adj_global)
        if colors is None:
            sys.stdout.write("NO")
            return
        for i, v in enumerate(comp):
            answer[v] = colors[i]

    sys.stdout.write("YES\n")
    sys.stdout.write(" ".join(map(str, answer)))


solve()