import sys
sys.setrecursionlimit(1_000_000)

EPS = 1e-9
INF = float("inf")


class Dinic:
    __slots__ = ("n", "g", "level", "it")

    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]
        self.level = [-1] * n
        self.it = [0] * n

    def add_edge(self, u, v, cap):
        if u == v:
            return None
        a = [v, cap, None, cap]
        b = [u, 0, a, 0]
        a[2] = b
        self.g[u].append(a)
        self.g[v].append(b)
        return a

    def bfs(self, s, t):
        level = self.level
        for i in range(self.n):
            level[i] = -1
        level[s] = 0
        q = [s]
        head = 0
        while head < len(q):
            u = q[head]
            head += 1
            for e in self.g[u]:
                if e[1] > 0 and level[e[0]] < 0:
                    level[e[0]] = level[u] + 1
                    q.append(e[0])
        return level[t] >= 0

    def dfs(self, u, t, pushed):
        if u == t:
            return pushed
        g = self.g
        level = self.level
        i = self.it[u]
        while i < len(g[u]):
            self.it[u] = i
            e = g[u][i]
            if e[1] > 0 and level[e[0]] == level[u] + 1:
                got = self.dfs(e[0], t, min(pushed, e[1]))
                if got:
                    e[1] -= got
                    e[2][1] += got
                    return got
            i += 1
            self.it[u] = i
        return 0

    def maxflow(self, s, t, limit):
        result = 0
        while result < limit and self.bfs(s, t):
            self.it = [0] * self.n
            while result < limit:
                pushed = self.dfs(s, t, limit - result)
                if not pushed:
                    break
                result += pushed
        return result


class LPSolver:
    __slots__ = ("m", "n", "B", "N", "D")

    def __init__(self, base_a, base_b, nvars, branches):
        self.n = nvars
        self.m = len(base_b) + len(branches)
        n = self.n
        m = self.m

        self.B = [0] * m
        self.N = list(range(n)) + [-1]
        self.D = []

        for i, (row, rhs) in enumerate(zip(base_a, base_b)):
            self.B[i] = n + i
            self.D.append(row[:] + [-1.0, float(rhs)])

        offset = len(base_b)
        for q, (var, coef, rhs) in enumerate(branches):
            row = [0.0] * (n + 2)
            row[var] = float(coef)
            row[n] = -1.0
            row[n + 1] = float(rhs)
            self.B[offset + q] = n + offset + q
            self.D.append(row)

        self.D.append([0.0] * (n + 2))
        phase1 = [0.0] * (n + 2)
        phase1[n] = 1.0
        self.D.append(phase1)

    def pivot(self, r, s):
        D = self.D
        m = self.m
        n = self.n
        inv = 1.0 / D[r][s]
        pivot_row = D[r]

        for i in range(m + 2):
            if i == r:
                continue
            row = D[i]
            if abs(row[s]) <= EPS:
                continue
            factor = row[s] * inv
            for j in range(n + 2):
                if j != s:
                    row[j] -= pivot_row[j] * factor

        for j in range(n + 2):
            if j != s:
                pivot_row[j] *= inv

        for i in range(m + 2):
            if i != r:
                D[i][s] *= -inv
        pivot_row[s] = inv
        self.B[r], self.N[s] = self.N[s], self.B[r]

    def simplex(self, phase):
        D = self.D
        m = self.m
        n = self.n
        objective = m + 1 if phase == 1 else m

        while True:
            s = -1
            for j in range(n + 1):
                if phase == 2 and self.N[j] == -1:
                    continue
                if s == -1 or D[objective][j] < D[objective][s] - EPS or (
                    abs(D[objective][j] - D[objective][s]) <= EPS
                    and self.N[j] < self.N[s]
                ):
                    s = j

            if s == -1 or D[objective][s] >= -EPS:
                return True

            r = -1
            for i in range(m):
                if D[i][s] <= EPS:
                    continue
                if r == -1:
                    r = i
                else:
                    left = D[i][n + 1] / D[i][s]
                    right = D[r][n + 1] / D[r][s]
                    if left < right - EPS or (
                        abs(left - right) <= EPS and self.B[i] < self.B[r]
                    ):
                        r = i

            if r == -1:
                return False
            self.pivot(r, s)

    def solve(self):
        D = self.D
        m = self.m
        n = self.n

        if m:
            r = min(range(m), key=lambda i: D[i][n + 1])
            if D[r][n + 1] < -EPS:
                self.pivot(r, n)
                if not self.simplex(1):
                    return None
                if D[m + 1][n + 1] < -1e-7:
                    return None
                if abs(D[m + 1][n + 1]) > 1e-6:
                    return None

                for i in range(m):
                    if self.B[i] == -1:
                        s = -1
                        for j in range(n + 1):
                            if abs(D[i][j]) > EPS and (
                                s == -1 or self.N[j] < self.N[s]
                            ):
                                s = j
                        if s != -1:
                            self.pivot(i, s)
                        break

        if not self.simplex(2):
            return None

        x = [0.0] * n
        for i in range(m):
            if 0 <= self.B[i] < n:
                x[self.B[i]] = D[i][n + 1]
        return x


def solve_common_terminals(n, m, commodities, edges, active):
    s = commodities[active[0]][0]
    t = commodities[active[0]][1]
    total = sum(commodities[i][2] for i in active)

    dinic = Dinic(n)
    refs = [None] * m
    for j, (u, v, cap) in enumerate(edges):
        if cap > 0:
            refs[j] = dinic.add_edge(u, v, cap)

    if dinic.maxflow(s, t, total) != total:
        return None

    remaining = [0] * m
    outgoing = [[] for _ in range(n)]
    for j, (u, v, cap) in enumerate(edges):
        if refs[j] is not None:
            used = refs[j][3] - refs[j][1]
            if used > 0:
                remaining[j] = used
                outgoing[u].append(j)

    answer = [[0] * m for _ in commodities]

    for ci in active:
        need = commodities[ci][2]
        while need > 0:
            parent_edge = [-1] * n
            q = [s]
            parent_edge[s] = -2
            head = 0
            while head < len(q) and parent_edge[t] == -1:
                u = q[head]
                head += 1
                for j in outgoing[u]:
                    if remaining[j] <= 0:
                        continue
                    v = edges[j][1]
                    if parent_edge[v] == -1:
                        parent_edge[v] = j
                        q.append(v)
                        if v == t:
                            break

            if parent_edge[t] == -1:
                return None

            amount = need
            v = t
            path = []
            while v != s:
                j = parent_edge[v]
                path.append(j)
                amount = min(amount, remaining[j])
                v = edges[j][0]

            for j in path:
                remaining[j] -= amount
                answer[ci][j] += amount
            need -= amount

    return answer


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    it = iter(data)
    n = next(it)
    m = next(it)
    k = next(it)

    commodities = []
    for _ in range(k):
        s = next(it) - 1
        t = next(it) - 1
        d = next(it)
        commodities.append((s, t, d))

    edges = []
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        cap = next(it)
        edges.append((u, v, cap))

    active_commodities = [
        i for i, (s, t, d) in enumerate(commodities)
        if d > 0 and s != t
    ]

    if not active_commodities:
        out = ["YES"]
        zero = " ".join(["0"] * m)
        out.extend(zero for _ in range(k))
        sys.stdout.write("\n".join(out))
        return

    first_s = commodities[active_commodities[0]][0]
    first_t = commodities[active_commodities[0]][1]
    if all(
        commodities[i][0] == first_s and commodities[i][1] == first_t
        for i in active_commodities
    ):
        answer = solve_common_terminals(
            n, m, commodities, edges, active_commodities
        )
        if answer is None:
            print("NO")
            return
        out = ["YES"]
        out.extend(" ".join(map(str, row)) for row in answer)
        sys.stdout.write("\n".join(out))
        return

    active_edges = [j for j, (_, _, cap) in enumerate(edges) if cap > 0]
    edge_pos = {j: p for p, j in enumerate(active_edges)}
    commodity_pos = {ci: q for q, ci in enumerate(active_commodities)}

    ke = len(active_commodities)
    me = len(active_edges)
    vcount = ke * me

    base_a = []
    base_b = []

    for q, ci in enumerate(active_commodities):
        s, t, d = commodities[ci]
        for node in range(n):
            if node == t:
                continue
            row = [0.0] * vcount
            offset = q * me
            for p, j in enumerate(active_edges):
                u, v, _ = edges[j]
                if u == node:
                    row[offset + p] += 1.0
                if v == node:
                    row[offset + p] -= 1.0

            rhs = d if node == s else 0
            base_a.append(row)
            base_b.append(rhs)
            base_a.append([-x for x in row])
            base_b.append(-rhs)

    for p, j in enumerate(active_edges):
        row = [0.0] * vcount
        for q in range(ke):
            row[q * me + p] = 1.0
        base_a.append(row)
        base_b.append(edges[j][2])

    branches = []
    result = None

    def search():
        nonlocal result
        lp = LPSolver(base_a, base_b, vcount, branches)
        x = lp.solve()
        if x is None:
            return False

        branch_var = -1
        branch_frac = 0.0
        best_score = -1.0

        for idx, value in enumerate(x):
            nearest = round(value)
            frac_dist = abs(value - nearest)
            if frac_dist > 1e-6:
                frac = value - int(value // 1)
                score = min(frac, 1.0 - frac)
                if score > best_score:
                    best_score = score
                    branch_var = idx
                    branch_frac = frac

        if branch_var == -1:
            candidate = [max(0, int(round(v))) for v in x]

            for row, rhs in zip(base_a, base_b):
                total = 0
                for idx, coef in enumerate(row):
                    if coef:
                        total += int(coef) * candidate[idx]
                if total > rhs + 1e-7:
                    return False

            result = candidate
            return True

        value = x[branch_var]
        floor_value = int(value // 1)
        ceil_value = floor_value + 1

        if branch_frac <= 0.5:
            choices = [
                (branch_var, 1, floor_value),
                (branch_var, -1, -ceil_value),
            ]
        else:
            choices = [
                (branch_var, -1, -ceil_value),
                (branch_var, 1, floor_value),
            ]

        for constraint in choices:
            branches.append(constraint)
            if search():
                return True
            branches.pop()
        return False

    if not search():
        print("NO")
        return

    answer = [[0] * m for _ in range(k)]
    for ci in active_commodities:
        q = commodity_pos[ci]
        for j in active_edges:
            p = edge_pos[j]
            answer[ci][j] = result[q * me + p]

    for ci, (s, t, d) in enumerate(commodities):
        if d == 0 or s == t:
            continue
        balance = [0] * n
        for j, (u, v, cap) in enumerate(edges):
            f = answer[ci][j]
            if f < 0 or f > cap:
                print("NO")
                return
            balance[u] += f
            balance[v] -= f
        for node in range(n):
            expected = d if node == s else (-d if node == t else 0)
            if balance[node] != expected:
                print("NO")
                return

    for j, (_, _, cap) in enumerate(edges):
        if sum(answer[i][j] for i in range(k)) > cap:
            print("NO")
            return

    out = ["YES"]
    out.extend(" ".join(map(str, row)) for row in answer)
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()