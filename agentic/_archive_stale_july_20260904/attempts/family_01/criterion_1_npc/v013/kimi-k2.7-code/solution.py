import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [0] * n
    neigh = [[] for _ in range(n)]

    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        if (adj[u] >> v) & 1:
            continue
        adj[u] |= 1 << v
        adj[v] |= 1 << u
        neigh[u].append(v)
        neigh[v].append(u)

    # A 4-clique makes 3-coloring impossible.
    if n >= 4:
        for i in range(n):
            ai = adj[i]
            for j in range(i + 1, n):
                if not ((ai >> j) & 1):
                    continue
                aj = adj[j]
                for k in range(j + 1, n):
                    if not ((ai >> k) & 1 and (aj >> k) & 1):
                        continue
                    if adj[i] & adj[j] & adj[k]:
                        sys.stdout.write("NO\n")
                        return

    sys.setrecursionlimit(10000)

    def search(domains):
        minv = -1
        minsize = 4
        for v in range(n):
            d = domains[v]
            if d & (d - 1):
                bc = d.bit_count()
                if bc < minsize:
                    minsize = bc
                    minv = v
                    if bc == 2:
                        break
        if minv == -1:
            return True

        d = domains[minv]
        while d:
            cb = d & -d
            d ^= cb
            new = domains[:]
            new[minv] = cb
            st = [minv]
            ok = True
            while st:
                v = st.pop()
                dv = new[v]
                if dv == 0:
                    ok = False
                    break
                cbit = dv & -dv
                for u in neigh[v]:
                    if new[u] & cbit:
                        if new[u] == cbit:
                            ok = False
                            break
                        new[u] ^= cbit
                        if new[u] == 0:
                            ok = False
                            break
                        if new[u] & (new[u] - 1) == 0:
                            st.append(u)
                if not ok:
                    break
            if ok and search(new):
                return True
        return False

    def is_colorable(fixed):
        domains = [7] * n
        stack = []
        for v in range(n):
            c = fixed[v]
            if c:
                bit = 1 << (c - 1)
                if not (domains[v] & bit):
                    return False
                domains[v] = bit
                stack.append(v)

        while stack:
            v = stack.pop()
            dv = domains[v]
            if dv == 0:
                return False
            cbit = dv & -dv
            for u in neigh[v]:
                if domains[u] & cbit:
                    if domains[u] == cbit:
                        return False
                    domains[u] ^= cbit
                    if domains[u] == 0:
                        return False
                    if domains[u] & (domains[u] - 1) == 0:
                        stack.append(u)

        return search(domains)

    fixed = [0] * n
    for i in range(n):
        chosen = False
        for c in (1, 2, 3):
            conflict = False
            for u in neigh[i]:
                if fixed[u] == c:
                    conflict = True
                    break
            if conflict:
                continue
            fixed[i] = c
            if is_colorable(fixed):
                chosen = True
                break
            fixed[i] = 0
        if not chosen:
            sys.stdout.write("NO\n")
            return

    sys.stdout.write("YES\n")
    sys.stdout.write(' '.join(map(str, fixed)) + "\n")

solve()