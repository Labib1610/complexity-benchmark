import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))

    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        if u != v:
            adj[v].append(u)

    # Fingerprint analysis shows that for any two different tiers the
    # sum of absolute differences equals 4, while for equal tiers it is 0.
    # Hence every overlapping pair must receive different depth tiers.
    # The task is therefore the lexicographically smallest proper
    # 3-coloring of the graph.

    FULL = 7  # bits for colors 1,2,3
    color_bits = (1, 2, 4)

    deg = [len(adj[v]) for v in range(n)]
    rank = [0] * n
    for r, v in enumerate(sorted(range(n), key=lambda x: deg[x], reverse=True)):
        rank[v] = r

    sys.setrecursionlimit(10000)

    def propagate(domains, stack):
        while stack:
            v = stack.pop()
            c = domains[v]
            if c == 0:
                return False
            if c & (c - 1):
                continue
            for u in adj[v]:
                du = domains[u]
                if du & c:
                    du &= ~c
                    if du == 0:
                        return False
                    domains[u] = du
                    if du & (du - 1) == 0:
                        stack.append(u)
        return True

    def can_color(domains):
        stack = [i for i, d in enumerate(domains) if d and (d & (d - 1)) == 0]
        if not propagate(domains, stack):
            return False

        def dfs(dom):
            minv = -1
            minsize = 4
            minrank = -1
            for i, d in enumerate(dom):
                if d & (d - 1):
                    sz = d.bit_count()
                    if sz < minsize or (sz == minsize and rank[i] > minrank):
                        minsize = sz
                        minv = i
                        minrank = rank[i]
            if minv == -1:
                return True

            mask = dom[minv]
            # order colors by how constrained they are among neighbors
            choices = []
            mm = mask
            while mm:
                lsb = mm & -mm
                cnt = 0
                for u in adj[minv]:
                    if dom[u] & lsb:
                        cnt += 1
                choices.append((cnt, lsb))
                mm ^= lsb
            choices.sort()

            for _, lsb in choices:
                newdom = dom[:]
                newdom[minv] = lsb
                if propagate(newdom, [minv]):
                    if dfs(newdom):
                        return True
            return False

        return dfs(domains)

    domains = [FULL] * n
    for i in range(n):
        d = domains[i]
        if d == 0:
            print("NO")
            return
        if d & (d - 1) == 0:
            continue
        chosen = 0
        for cbit in color_bits:
            if d & cbit:
                newdom = domains[:]
                newdom[i] = cbit
                if propagate(newdom, [i]) and can_color(newdom):
                    chosen = cbit
                    domains = newdom
                    break
        if chosen == 0:
            print("NO")
            return

    bit_to_color = {1: 1, 2: 2, 4: 3}
    out = " ".join(str(bit_to_color[domains[i]]) for i in range(n))
    sys.stdout.write("YES\n" + out + "\n")

solve()