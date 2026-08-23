import sys

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
        if u == v:
            print("NO")
            return
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # connected components
    visited = 0
    components = []
    for s in range(n):
        if not (visited >> s) & 1:
            stack = [s]
            visited |= 1 << s
            comp = []
            while stack:
                v = stack.pop()
                comp.append(v)
                nb = adj[v]
                while nb:
                    lsb = nb & -nb
                    u = lsb.bit_length() - 1
                    if not (visited >> u) & 1:
                        visited |= 1 << u
                        stack.append(u)
                    nb ^= lsb
            comp.sort()
            components.append(comp)

    answer = [0] * n

    # DSATUR to find any valid coloring of a component
    def dsatur_coloring(k: int, loc_adj: list):
        all_mask = (1 << k) - 1
        color_masks = [0, 0, 0]
        col = [-1] * k
        assigned = 0
        deg = [a.bit_count() for a in loc_adj]

        sys.setrecursionlimit(10000)

        def dfs() -> bool:
            nonlocal assigned
            if assigned == all_mask:
                return True
            um = all_mask ^ assigned
            best_v = -1
            best_sat = -1
            best_deg = -1
            mm = um
            while mm:
                lsb = mm & -mm
                v = lsb.bit_length() - 1
                nb = loc_adj[v] & assigned
                sat = 0
                if nb & color_masks[0]:
                    sat += 1
                if nb & color_masks[1]:
                    sat += 1
                if nb & color_masks[2]:
                    sat += 1
                if sat > best_sat or (sat == best_sat and deg[v] > best_deg):
                    best_v = v
                    best_sat = sat
                    best_deg = deg[v]
                mm ^= lsb
            if best_sat == 3:
                return False
            nb = loc_adj[best_v] & assigned
            forbidden = 0
            if nb & color_masks[0]:
                forbidden |= 1
            if nb & color_masks[1]:
                forbidden |= 2
            if nb & color_masks[2]:
                forbidden |= 4
            for c in range(3):
                bit = 1 << c
                if forbidden & bit:
                    continue
                col[best_v] = c
                color_masks[c] |= 1 << best_v
                assigned |= 1 << best_v
                if dfs():
                    return True
                col[best_v] = -1
                color_masks[c] ^= 1 << best_v
                assigned ^= 1 << best_v
            return False

        if dfs():
            return col
        return None

    # Lexicographically smallest coloring, given an initial valid coloring `best`
    def lex_smallest(k: int, loc_adj: list, best: list):
        if k <= 1:
            return best[:]

        # neighbor lists
        neighbors = []
        for i in range(k):
            lst = []
            mm = loc_adj[i]
            while mm:
                lsb = mm & -mm
                j = lsb.bit_length() - 1
                lst.append(j)
                mm ^= lsb
            neighbors.append(lst)

        single_color = {1: 0, 2: 1, 4: 2}

        def propagate(dom, col, v, c, tight):
            queue = [v]
            col[v] = c
            dom[v] = 1 << c
            while queue:
                x = queue.pop()
                cx = col[x]
                bit = 1 << cx
                for u in neighbors[x]:
                    cu = col[u]
                    if cu != -1:
                        if cu == cx:
                            return False, tight
                        continue
                    if dom[u] & bit:
                        nd = dom[u] & ~bit
                        if nd == 0:
                            return False, tight
                        dom[u] = nd
                        if nd in single_color:
                            c2 = single_color[nd]
                            if tight:
                                bu = best[u]
                                if c2 > bu:
                                    return False, tight
                                if c2 < bu:
                                    tight = False
                            col[u] = c2
                            queue.append(u)
            return True, tight

        result = None

        def dfs(pos, dom, col, tight):
            nonlocal result
            if result is not None:
                return True
            while pos < k and col[pos] != -1:
                pos += 1
            if pos == k:
                result = col[:]
                return True
            d = dom[pos]
            upper = best[pos] if tight else 2
            for c in range(upper + 1):
                bit = 1 << c
                if not (d & bit):
                    continue
                ntight = tight and (c == best[pos])
                ndom = dom[:]
                ncol = col[:]
                ok, ntight2 = propagate(ndom, ncol, pos, c, ntight)
                if ok and dfs(pos + 1, ndom, ncol, ntight2):
                    return True
            return False

        dfs(0, [7] * k, [-1] * k, True)
        return result if result is not None else best[:]

    for comp in components:
        k = len(comp)
        if k == 1:
            answer[comp[0]] = 1
            continue

        # build local adjacency
        loc_id = [-1] * n
        for i, v in enumerate(comp):
            loc_id[v] = i
        loc_adj = [0] * k
        for i, v in enumerate(comp):
            mask = 0
            nb = adj[v]
            while nb:
                lsb = nb & -nb
                u = lsb.bit_length() - 1
                j = loc_id[u]
                if j >= 0:
                    mask |= 1 << j
                nb ^= lsb
            loc_adj[i] = mask

        init = dsatur_coloring(k, loc_adj)
        if init is None:
            print("NO")
            return
        best = lex_smallest(k, loc_adj, init)
        for i, v in enumerate(comp):
            answer[v] = best[i] + 1

    print("YES")
    print(' '.join(map(str, answer)))

if __name__ == "__main__":
    solve()