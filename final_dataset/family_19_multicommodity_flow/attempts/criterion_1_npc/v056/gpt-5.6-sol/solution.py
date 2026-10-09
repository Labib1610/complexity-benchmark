import sys
import random
sys.setrecursionlimit(1_000_000)

EPS = 1e-8
INF = float("inf")


class Dinic:
    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]

    def add_edge(self, u, v, c):
        ui = len(self.g[u])
        vi = len(self.g[v])
        self.g[u].append([v, vi, c])
        self.g[v].append([u, ui, 0])
        return ui

    def max_flow(self, s, t, limit):
        if s == t:
            return limit
        total = 0
        n = self.n
        while total < limit:
            level = [-1] * n
            level[s] = 0
            q = [s]
            head = 0
            while head < len(q):
                u = q[head]
                head += 1
                for v, rev, cap in self.g[u]:
                    if cap > 0 and level[v] < 0:
                        level[v] = level[u] + 1
                        q.append(v)
            if level[t] < 0:
                break

            it = [0] * n

            def dfs(u, f):
                if u == t:
                    return f
                while it[u] < len(self.g[u]):
                    e = self.g[u][it[u]]
                    v, rev, cap = e
                    if cap > 0 and level[v] == level[u] + 1:
                        got = dfs(v, min(f, cap))
                        if got:
                            e[2] -= got
                            self.g[v][rev][2] += got
                            return got
                    it[u] += 1
                return 0

            while total < limit:
                pushed = dfs(s, limit - total)
                if pushed == 0:
                    break
                total += pushed
        return total


class LPSolver:
    def __init__(self, A, b, c):
        self.m = len(b)
        self.n = len(c)
        m, n = self.m, self.n
        self.B = [n + i for i in range(m)]
        self.N = list(range(n)) + [-1]
        self.D = [[0.0] * (n + 2) for _ in range(m + 2)]

        for i in range(m):
            row = self.D[i]
            ai = A[i]
            for j in range(n):
                row[j] = float(ai[j])
            row[n] = -1.0
            row[n + 1] = float(b[i])

        for j in range(n):
            self.D[m][j] = -float(c[j])
        self.D[m + 1][n] = 1.0

    def pivot(self, r, s):
        D = self.D
        m, n = self.m, self.n
        inv = 1.0 / D[r][s]

        for i in range(m + 2):
            if i == r:
                continue
            dis = D[i][s]
            if abs(dis) <= EPS:
                continue
            factor = dis * inv
            ri = D[i]
            rr = D[r]
            for j in range(n + 2):
                if j != s:
                    ri[j] -= rr[j] * factor

        rr = D[r]
        for j in range(n + 2):
            if j != s:
                rr[j] *= inv

        for i in range(m + 2):
            if i != r:
                D[i][s] *= -inv
        D[r][s] = inv
        self.B[r], self.N[s] = self.N[s], self.B[r]

    def simplex(self, phase):
        m, n = self.m, self.n
        xrow = m + 1 if phase == 1 else m
        D, N, B = self.D, self.N, self.B

        while True:
            s = -1
            for j in range(n + 1):
                if phase == 2 and N[j] == -1:
                    continue
                if s == -1 or D[xrow][j] < D[xrow][s] - EPS or (
                    abs(D[xrow][j] - D[xrow][s]) <= EPS and N[j] < N[s]
                ):
                    s = j

            if s == -1 or D[xrow][s] >= -EPS:
                return True

            r = -1
            for i in range(m):
                if D[i][s] <= EPS:
                    continue
                if r == -1:
                    r = i
                else:
                    lhs = D[i][n + 1] / D[i][s]
                    rhs = D[r][n + 1] / D[r][s]
                    if lhs < rhs - EPS or (
                        abs(lhs - rhs) <= EPS and B[i] < B[r]
                    ):
                        r = i

            if r == -1:
                return False
            self.pivot(r, s)

    def solve(self):
        m, n = self.m, self.n
        D = self.D

        if m:
            r = min(range(m), key=lambda i: D[i][n + 1])
            if D[r][n + 1] < -EPS:
                self.pivot(r, n)
                if not self.simplex(1) or D[m + 1][n + 1] < -1e-7:
                    return None
                if abs(D[m + 1][n + 1]) > 1e-7:
                    return None

                for i in range(m):
                    if self.B[i] == -1:
                        s = -1
                        for j in range(n + 1):
                            if s == -1 or D[i][j] < D[i][s] - EPS or (
                                abs(D[i][j] - D[i][s]) <= EPS
                                and self.N[j] < self.N[s]
                            ):
                                s = j
                        if s != -1 and abs(D[i][s]) > EPS:
                            self.pivot(i, s)

        if not self.simplex(2):
            return None

        x = [0.0] * n
        for i in range(m):
            if 0 <= self.B[i] < n:
                x[self.B[i]] = D[i][n + 1]
        return x


def greedy_attempt(n, m, contracts, edges, capacities, order):
    remaining = capacities[:]
    answer = [[0] * m for _ in contracts]

    for ci in order:
        s, t, demand = contracts[ci]
        if demand == 0 or s == t:
            continue

        dinic = Dinic(n)
        refs = [None] * m
        for ei, (u, v, _) in enumerate(edges):
            if remaining[ei] > 0:
                pos = dinic.add_edge(u, v, remaining[ei])
                refs[ei] = (u, pos, remaining[ei])

        if dinic.max_flow(s, t, demand) != demand:
            return None

        for ei, ref in enumerate(refs):
            if ref is not None:
                u, pos, initial = ref
                used = initial - dinic.g[u][pos][2]
                if used:
                    answer[ci][ei] = used
                    remaining[ei] -= used

    return answer


def validate(n, m, contracts, edges, ans, capacities):
    totals = [0] * m
    for ci, (s, t, demand) in enumerate(contracts):
        bal = [0] * n
        for ei, (u, v, _) in enumerate(edges):
            x = ans[ci][ei]
            if x < 0:
                return False
            totals[ei] += x
            bal[u] += x
            bal[v] -= x
        for v in range(n):
            required = (demand if v == s else 0) - (demand if v == t else 0)
            if bal[v] != required:
                return False
    return all(totals[i] <= capacities[i] for i in range(m))


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)
    k = next(it)

    contracts = []
    for _ in range(k):
        s = next(it) - 1
        t = next(it) - 1
        d = next(it)
        contracts.append((s, t, d))

    edges = []
    capacities = []
    out_adj = [[] for _ in range(n)]
    rev_adj = [[] for _ in range(n)]
    for ei in range(m):
        u = next(it) - 1
        v = next(it) - 1
        c = next(it)
        edges.append((u, v, c))
        capacities.append(c)
        if c > 0:
            out_adj[u].append((v, ei))
            rev_adj[v].append((u, ei))

    for s, t, d in contracts:
        if d < 0:
            print("NO")
            return
        if s == t and d != 0:
            # The net-balance interpretation makes a same-node contract trivial.
            continue

    orders = [list(range(k))]
    if k > 1:
        orders.append(sorted(range(k), key=lambda i: contracts[i][2], reverse=True))
        rng = random.Random(712367821)
        for _ in range(min(3, k)):
            order = list(range(k))
            rng.shuffle(order)
            orders.append(order)

    seen = set()
    for order in orders:
        key = tuple(order)
        if key in seen:
            continue
        seen.add(key)
        ans = greedy_attempt(n, m, contracts, edges, capacities, order)
        if ans is not None and validate(n, m, contracts, edges, ans, capacities):
            out = ["YES"]
            out.extend(" ".join(map(str, row)) for row in ans)
            sys.stdout.write("\n".join(out))
            return

    var_info = []
    commodity_vars = [[] for _ in range(k)]
    edge_vars = [[] for _ in range(m)]

    for ci, (s, t, demand) in enumerate(contracts):
        if demand == 0 or s == t:
            continue

        forward = [False] * n
        forward[s] = True
        q = [s]
        head = 0
        while head < len(q):
            u = q[head]
            head += 1
            for v, ei in out_adj[u]:
                if not forward[v]:
                    forward[v] = True
                    q.append(v)

        if not forward[t]:
            print("NO")
            return

        backward = [False] * n
        backward[t] = True
        q = [t]
        head = 0
        while head < len(q):
            v = q[head]
            head += 1
            for u, ei in rev_adj[v]:
                if not backward[u]:
                    backward[u] = True
                    q.append(u)

        for ei, (u, v, c) in enumerate(edges):
            if c > 0 and forward[u] and backward[v]:
                idx = len(var_info)
                var_info.append((ci, ei))
                commodity_vars[ci].append(idx)
                edge_vars[ei].append(idx)

    V = len(var_info)
    if V == 0:
        ans = [[0] * m for _ in range(k)]
        if validate(n, m, contracts, edges, ans, capacities):
            out = ["YES"] + [" ".join(map(str, row)) for row in ans]
            sys.stdout.write("\n".join(out))
        else:
            print("NO")
        return

    base_A = []
    base_b = []

    for ei in range(m):
        if not edge_vars[ei]:
            continue
        row = [0.0] * V
        for idx in edge_vars[ei]:
            row[idx] = 1.0
        base_A.append(row)
        base_b.append(capacities[ei])

    for ci, (s, t, demand) in enumerate(contracts):
        if not commodity_vars[ci]:
            if demand != 0 and s != t:
                print("NO")
                return
            continue

        node_coeffs = {}
        for idx in commodity_vars[ci]:
            _, ei = var_info[idx]
            u, v, _ = edges[ei]
            if u not in node_coeffs:
                node_coeffs[u] = {}
            if v not in node_coeffs:
                node_coeffs[v] = {}
            node_coeffs[u][idx] = node_coeffs[u].get(idx, 0.0) + 1.0
            node_coeffs[v][idx] = node_coeffs[v].get(idx, 0.0) - 1.0

        relevant = set(node_coeffs)
        relevant.add(s)
        relevant.add(t)
        omit = next(iter(relevant))
        for node in relevant:
            if node == omit:
                continue
            rhs = (demand if node == s else 0) - (demand if node == t else 0)
            coeff = node_coeffs.get(node, {})
            row = [0.0] * V
            for idx, val in coeff.items():
                row[idx] = val
            base_A.append(row)
            base_b.append(rhs)
            base_A.append([-x for x in row])
            base_b.append(-rhs)

    objective = [
        (((i * 1103515245 + 12345) & 2047) - 1024) / 1024.0
        for i in range(V)
    ]

    stack = [[]]
    solution = None

    while stack:
        branches = stack.pop()
        A = base_A[:]
        b = base_b[:]

        for idx, sign, bound in branches:
            row = [0.0] * V
            row[idx] = sign
            A.append(row)
            b.append(bound)

        x = LPSolver(A, b, objective).solve()
        if x is None:
            continue

        fractional = -1
        best_score = -1.0
        for i, value in enumerate(x):
            nearest = round(value)
            dist = abs(value - nearest)
            if dist > 1e-7:
                frac = value - int(value)
                score = min(frac, 1.0 - frac)
                if score > best_score:
                    best_score = score
                    fractional = i

        if fractional == -1:
            vals = [int(round(max(0.0, z))) for z in x]
            ans = [[0] * m for _ in range(k)]
            for idx, value in enumerate(vals):
                ci, ei = var_info[idx]
                ans[ci][ei] = value
            if validate(n, m, contracts, edges, ans, capacities):
                solution = ans
                break
            continue

        value = x[fractional]
        lo = int(value // 1)
        hi = lo + 1

        lower_branch = branches + [(fractional, 1.0, lo)]
        upper_branch = branches + [(fractional, -1.0, -hi)]

        if value - lo <= hi - value:
            stack.append(upper_branch)
            stack.append(lower_branch)
        else:
            stack.append(lower_branch)
            stack.append(upper_branch)

    if solution is None:
        print("NO")
    else:
        out = ["YES"]
        out.extend(" ".join(map(str, row)) for row in solution)
        sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()