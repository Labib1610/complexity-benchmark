import sys

sys.setrecursionlimit(10000)


def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * n
    neighbors = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if u == v:
            continue
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        neighbors[u].append(v)
        neighbors[v].append(u)

    def propagate(domains, start, changes):
        stack = [start]
        while stack:
            v = stack.pop()
            d = domains[v]
            cbit = d.bit_length() - 1
            mask = 1 << cbit
            for u in neighbors[v]:
                if domains[u] & mask:
                    new = domains[u] & ~mask
                    if new == 0:
                        return False
                    changes.append((u, domains[u]))
                    domains[u] = new
                    if new & (new - 1) == 0:
                        stack.append(u)
        return True

    def solve_component(domains, comp):
        if comp == 0:
            return True

        # Split disconnected components.
        v = (comp & -comp).bit_length() - 1
        sub = 0
        stack = [v]
        seen = 0
        while stack:
            x = stack.pop()
            sub |= 1 << x
            seen |= 1 << x
            nb = adj[x] & comp & ~seen
            while nb:
                lsb = nb & -nb
                y = lsb.bit_length() - 1
                stack.append(y)
                seen |= 1 << y
                nb ^= lsb
        if sub != comp:
            if not solve_component(domains, sub):
                return False
            return solve_component(domains, comp ^ sub)

        # Choose the vertex with the smallest domain.
        v = -1
        best = 4
        tmp = comp
        while tmp:
            lsb = tmp & -tmp
            i = lsb.bit_length() - 1
            pc = domains[i].bit_count()
            if pc < best:
                best = pc
                v = i
            tmp ^= lsb

        if best == 0:
            return False

        d = domains[v]
        # Order colors by least constraining.
        cand = []
        comp_nb = adj[v] & comp
        for cbit in range(3):
            bit = 1 << cbit
            if d & bit:
                cnt = 0
                nb = comp_nb
                while nb:
                    lsb = nb & -nb
                    u = lsb.bit_length() - 1
                    if domains[u] & bit:
                        cnt += 1
                    nb ^= lsb
                cand.append((cnt, cbit))
        cand.sort()

        for cnt, cbit in cand:
            changes = [(v, domains[v])]
            domains[v] = 1 << cbit
            if propagate(domains, v, changes):
                new_comp = comp
                for u, _ in changes:
                    if domains[u] & (domains[u] - 1) == 0:
                        new_comp &= ~(1 << u)
                if solve_component(domains, new_comp):
                    return True
            for u, old in reversed(changes):
                domains[u] = old
        return False

    def can_extend(fixed):
        domains = [0] * n
        for v in range(n):
            if fixed[v]:
                domains[v] = 1 << (fixed[v] - 1)
            else:
                mask = 0
                for u in neighbors[v]:
                    if fixed[u]:
                        mask |= 1 << (fixed[u] - 1)
                domains[v] = 0b111 & ~mask

        stack = []
        for v in range(n):
            if domains[v] == 0:
                return False
            if domains[v] & (domains[v] - 1) == 0:
                stack.append(v)

        while stack:
            v = stack.pop()
            d = domains[v]
            cbit = d.bit_length() - 1
            mask = 1 << cbit
            for u in neighbors[v]:
                if domains[u] & mask:
                    new = domains[u] & ~mask
                    if new == 0:
                        return False
                    if new != domains[u]:
                        domains[u] = new
                        if new & (new - 1) == 0:
                            stack.append(u)

        mask_uncolored = 0
        for v in range(n):
            if domains[v] & (domains[v] - 1):
                mask_uncolored |= 1 << v

        seen = 0
        while seen != mask_uncolored:
            rem = mask_uncolored & ~seen
            v = (rem & -rem).bit_length() - 1
            comp = 0
            stack = [v]
            seen |= 1 << v
            while stack:
                x = stack.pop()
                comp |= 1 << x
                nb = adj[x] & mask_uncolored & ~seen
                while nb:
                    lsb = nb & -nb
                    y = lsb.bit_length() - 1
                    stack.append(y)
                    seen |= 1 << y
                    nb ^= lsb
            if not solve_component(domains, comp):
                return False
        return True

    colors = [0] * n
    for i in range(n):
        forb = 0
        for u in neighbors[i]:
            if colors[u]:
                forb |= 1 << (colors[u] - 1)
        avail = 0b111 & ~forb
        if avail == 0:
            print("NO")
            return

        chosen = 0
        for cbit in range(3):
            bit = 1 << cbit
            if avail & bit:
                test = colors[:]
                test[i] = cbit + 1
                if can_extend(test):
                    chosen = cbit + 1
                    break
        if chosen == 0:
            print("NO")
            return
        colors[i] = chosen

    print("YES")
    print(' '.join(map(str, colors)))


if __name__ == "__main__":
    solve()