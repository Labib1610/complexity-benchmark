import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
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
            sys.stdout.write("NO")
            return
        adj[u] |= 1 << v
        adj[v] |= 1 << u

    # Quick NO: K4 is not 3-colorable
    if n >= 4:
        for u in range(n):
            high = adj[u] & ~((1 << (u + 1)) - 1)
            mv = high
            while mv:
                lsb = mv & -mv
                v = lsb.bit_length() - 1
                common = adj[u] & adj[v]
                mx = common
                while mx:
                    lsb2 = mx & -mx
                    x = lsb2.bit_length() - 1
                    if adj[x] & common:
                        sys.stdout.write("NO")
                        return
                    mx ^= lsb2
                mv ^= lsb

    # Connected components
    visited = 0
    components = []
    for v in range(n):
        if visited >> v & 1:
            continue
        stack = [v]
        visited |= 1 << v
        mask = 0
        while stack:
            x = stack.pop()
            mask |= 1 << x
            nb = adj[x] & ~visited
            while nb:
                lsb = nb & -nb
                y = lsb.bit_length() - 1
                visited |= 1 << y
                stack.append(y)
                nb ^= lsb
        comp = []
        mm = mask
        while mm:
            lsb = mm & -mm
            comp.append(lsb.bit_length() - 1)
            mm ^= lsb
        components.append(comp)

    # Solve larger components first to detect impossibility earlier
    components.sort(key=len, reverse=True)
    answer = [0] * n

    def solve_component(comp):
        k = len(comp)
        if k == 1:
            return [1]
        idx = [-1] * n
        for i, v in enumerate(comp):
            idx[v] = i
        local_adj = [[] for _ in range(k)]
        comp_mask = 0
        for v in comp:
            comp_mask |= 1 << v
        for i, v in enumerate(comp):
            nb = adj[v] & comp_mask & ~(1 << v)
            while nb:
                lsb = nb & -nb
                u = lsb.bit_length() - 1
                local_adj[i].append(idx[u])
                nb ^= lsb

        assign = [-1] * k
        domain = [7] * k   # bits 0,1,2 correspond to colors 1,2,3
        dom_ch = []
        ass_ch = []

        def set_color(v, c):
            ass_ch.append((v, domain[v]))
            assign[v] = c
            domain[v] = 1 << c
            stack = [v]
            while stack:
                cur = stack.pop()
                cc = assign[cur]
                bit = 1 << cc
                for u in local_adj[cur]:
                    if assign[u] == -1:
                        old = domain[u]
                        if old & bit:
                            new = old & ~bit
                            if new == 0:
                                return False
                            dom_ch.append((u, old))
                            domain[u] = new
                            if new & (new - 1) == 0:
                                col = new.bit_length() - 1
                                ass_ch.append((u, new))
                                assign[u] = col
                                stack.append(u)
            return True

        def dfs(pos):
            while pos < k and assign[pos] != -1:
                pos += 1
            if pos == k:
                return True
            d = domain[pos]
            for c in range(3):
                if d >> c & 1:
                    dlen = len(dom_ch)
                    alen = len(ass_ch)
                    if set_color(pos, c) and dfs(pos + 1):
                        return True
                    while len(ass_ch) > alen:
                        u, old = ass_ch.pop()
                        assign[u] = -1
                        domain[u] = old
                    while len(dom_ch) > dlen:
                        u, old = dom_ch.pop()
                        domain[u] = old
            return False

        if not dfs(0):
            return None
        return [a + 1 for a in assign]

    for comp in components:
        colors = solve_component(comp)
        if colors is None:
            sys.stdout.write("NO")
            return
        for v, c in zip(comp, colors):
            answer[v] = c

    out = ["YES", " ".join(map(str, answer))]
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    solve()