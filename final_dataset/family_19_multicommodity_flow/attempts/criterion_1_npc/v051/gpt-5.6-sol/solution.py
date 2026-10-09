import sys
from collections import deque

EPS = 1e-8
INF = 10**30


class Dinic:
    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]

    def add_edge(self, u, v, cap):
        f = [v, len(self.g[v]), cap, cap]
        r = [u, len(self.g[u]), 0, 0]
        self.g[u].append(f)
        self.g[v].append(r)
        return f

    def max_flow(self, s, t, limit=INF):
        if s == t:
            return limit
        total = 0
        n = self.n

        while total < limit:
            level = [-1] * n
            level[s] = 0
            q = deque([s])
            while q:
                u = q.popleft()
                for e in self.g[u]:
                    if e[2] > 0 and level[e[0]] < 0:
                        level[e[0]] = level[u] + 1
                        q.append(e[0])

            if level[t] < 0:
                break

            it = [0] * n

            def dfs(u, pushed):
                if u == t:
                    return pushed
                while it[u] < len(self.g[u]):
                    e = self.g[u][it[u]]
                    if e[2] > 0 and level[e[0]] == level[u] + 1:
                        got = dfs(e[0], min(pushed, e[2]))
                        if got:
                            e[2] -= got
                            self.g[e[0]][e[1]][2] += got
                            return got
                    it[u] += 1
                return 0

            while total < limit:
                pushed = dfs(s, limit - total)
                if not pushed:
                    break
                total += pushed

        return total


class LPSolver:
    def __init__(self, A, b, variables):
        self.m = len(b)
        self.n = variables
        m, n = self.m, self.n
        self.B = [n + i for i in range(m)]
        self.N = list(range(n)) + [-1]
        self.D = [[0.0] * (n + 2) for _ in range(m + 2)]

        for i in range(m):
            row = A[i]
            di = self.D[i]
            for j, val in enumerate(row):
                di[j] = float(val)
            di[n] = -1.0
            di[n + 1] = float(b[i])

        self.D[m + 1][n] = 1.0

    def pivot(self, r, s):
        D = self.D
        m, n = self.m, self.n
        inv = 1.0 / D[r][s]

        for i in range(m + 2):
            if i == r or abs(D[i][s]) <= EPS:
                continue
            factor = D[i][s] * inv
            di = D[i]
            dr = D[r]
            for j in range(n + 2):
                if j != s:
                    di[j] -= dr[j] * factor
            di[s] = -factor

        dr = D[r]
        for j in range(n + 2):
            if j != s:
                dr[j] *= inv
        dr[s] = inv
        self.B[r], self.N[s] = self.N[s], self.B[r]

    def simplex(self, phase):
        D = self.D
        m, n = self.m, self.n
        xrow = m + 1 if phase == 1 else m

        while True:
            s = -1
            for j in range(n + 1):
                if phase == 2 and self.N[j] == -1:
                    continue
                if s == -1 or D[xrow][j] < D[xrow][s] - EPS or (
                    abs(D[xrow][j] - D[xrow][s]) <= EPS
                    and self.N[j] < self.N[s]
                ):
                    s = j

            if D[xrow][s] >= -EPS:
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
                        abs(lhs - rhs) <= EPS and self.B[i] < self.B[r]
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
                if not self.simplex(1):
                    return None
                if abs(D[m + 1][n + 1]) > 1e-7:
                    return None

                for i in range(m):
                    if self.B[i] == -1:
                        s = -1
                        for j in range(n + 1):
                            if s == -1 or abs(D[i][j]) > abs(D[i][s]) + EPS or (
                                abs(abs(D[i][j]) - abs(D[i][s])) <= EPS
                                and self.N[j] < self.N[s]
                            ):
                                s = j
                        if s != -1 and abs(D[i][s]) > EPS:
                            self.pivot(i, s)

        self.simplex(2)

        x = [0.0] * n
        for i in range(m):
            if 0 <= self.B[i] < n:
                x[self.B[i]] = D[i][n + 1]
        return x


def greedy_solution(n, m, commodities, edges, order):
    residual = [c for _, _, c in edges]
    answer = [[0] * m for _ in commodities]

    for ci in order:
        s, t, d = commodities[ci]
        if d == 0 or s == t:
            continue

        dinic = Dinic(n)
        refs = [None] * m
        for ei, (u, v, _) in enumerate(edges):
            if residual[ei] > 0:
                refs[ei] = dinic.add_edge(u, v, residual[ei])

        flow = dinic.max_flow(s, t, d)
        if flow != d:
            return None

        for ei, ref in enumerate(refs):
            if ref is not None:
                used = ref[3] - ref[2]
                if used:
                    answer[ci][ei] = used
                    residual[ei] -= used

    return answer


def validate(answer, n, commodities, edges):
    m = len(edges)
    usage = [0] * m

    for ci, (s, t, d) in enumerate(commodities):
        bal = [0] * n
        row = answer[ci]
        for ei, x in enumerate(row):
            if x < 0:
                return False
            u, v, _ = edges[ei]
            bal[u] += x
            bal[v] -= x
            usage[ei] += x

        for v in range(n):
            expected = 0
            if s != t:
                if v == s:
                    expected += d
                if v == t:
                    expected -= d
            if bal[v] != expected:
                return False

    for ei, (_, _, c) in enumerate(edges):
        if usage[ei] > c:
            return False
    return True


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
    graph = [[] for _ in range(n)]
    rev_graph = [[] for _ in range(n)]
    for ei in range(m):
        u = next(it) - 1
        v = next(it) - 1
        c = next(it)
        edges.append((u, v, c))
        if c > 0:
            graph[u].append((v, ei))
            rev_graph[v].append((u, ei))

    if all(d == 0 or s == t for s, t, d in commodities):
        print("YES")
        zero = " ".join(["0"] * m)
        for _ in range(k):
            print(zero)
        return

    orders = []
    natural = tuple(range(k))
    candidates = [
        natural,
        tuple(reversed(range(k))),
        tuple(sorted(range(k), key=lambda i: -commodities[i][2])),
        tuple(sorted(range(k), key=lambda i: commodities[i][2])),
    ]
    seen = set()
    for order in candidates:
        if order not in seen:
            seen.add(order)
            orders.append(order)

    if k * max(1, m) > 2_000_000:
        orders = orders[:1]

    for order in orders:
        answer = greedy_solution(n, m, commodities, edges, order)
        if answer is not None and validate(answer, n, commodities, edges):
            out = ["YES"]
            out.extend(" ".join(map(str, row)) for row in answer)
            sys.stdout.write("\n".join(out))
            return

    if k == 1:
        print("NO")
        return

    variable_pairs = []
    commodity_vertices = {}

    for ci, (s, t, d) in enumerate(commodities):
        if d == 0 or s == t:
            continue

        reachable = [False] * n
        reachable[s] = True
        q = deque([s])
        while q:
            u = q.popleft()
            for v, _ in graph[u]:
                if not reachable[v]:
                    reachable[v] = True
                    q.append(v)

        can_reach_t = [False] * n
        can_reach_t[t] = True
        q = deque([t])
        while q:
            v = q.popleft()
            for u, _ in rev_graph[v]:
                if not can_reach_t[u]:
                    can_reach_t[u] = True
                    q.append(u)

        if not reachable[t]:
            print("NO")
            return

        relevant = [
            v for v in range(n)
            if reachable[v] and can_reach_t[v]
        ]
        commodity_vertices[ci] = relevant

        for ei, (u, v, c) in enumerate(edges):
            if c > 0 and reachable[u] and can_reach_t[v]:
                variable_pairs.append((ci, ei))

    var_count = len(variable_pairs)
    if var_count == 0:
        print("NO")
        return

    rows = []
    bounds = []
    conservation_rows = {}

    for ci, vertices in commodity_vertices.items():
        s, t, d = commodities[ci]
        for v in vertices:
            if v == t:
                continue
            p = len(rows)
            rows.append([0] * var_count)
            bounds.append(d if v == s else 0)
            qidx = len(rows)
            rows.append([0] * var_count)
            bounds.append(-d if v == s else 0)
            conservation_rows[(ci, v)] = (p, qidx)

    capacity_rows = {}
    used_edges = sorted({ei for _, ei in variable_pairs})
    for ei in used_edges:
        capacity_rows[ei] = len(rows)
        rows.append([0] * var_count)
        bounds.append(edges[ei][2])

    for j, (ci, ei) in enumerate(variable_pairs):
        u, v, _ = edges[ei]

        if (ci, u) in conservation_rows:
            p, qidx = conservation_rows[(ci, u)]
            rows[p][j] += 1
            rows[qidx][j] -= 1

        if (ci, v) in conservation_rows:
            p, qidx = conservation_rows[(ci, v)]
            rows[p][j] -= 1
            rows[qidx][j] += 1

        rows[capacity_rows[ei]][j] = 1

    base_rows = rows
    base_bounds = bounds
    stack = [[]]

    while stack:
        branch_constraints = stack.pop()
        A = list(base_rows)
        b = list(base_bounds)

        for var, sign, rhs in branch_constraints:
            row = [0] * var_count
            row[var] = sign
            A.append(row)
            b.append(rhs)

        solution = LPSolver(A, b, var_count).solve()
        if solution is None:
            continue

        fractional = -1
        best_score = -1.0
        for j, value in enumerate(solution):
            nearest = round(value)
            diff = abs(value - nearest)
            if diff > 1e-7:
                score = min(value - int(value), 1.0 - (value - int(value)))
                if score > best_score:
                    best_score = score
                    fractional = j

        if fractional == -1:
            answer = [[0] * m for _ in range(k)]
            for j, (ci, ei) in enumerate(variable_pairs):
                answer[ci][ei] = max(0, int(round(solution[j])))

            if validate(answer, n, commodities, edges):
                out = ["YES"]
                out.extend(" ".join(map(str, row)) for row in answer)
                sys.stdout.write("\n".join(out))
                return

            for j, value in enumerate(solution):
                if abs(value - round(value)) > 1e-10:
                    fractional = j
                    break
            if fractional == -1:
                continue

        value = solution[fractional]
        floor_value = int(value // 1)
        if value < 0 and value != floor_value:
            floor_value -= 1
        ceil_value = floor_value + 1

        high_branch = branch_constraints + [(fractional, -1, -ceil_value)]
        low_branch = branch_constraints + [(fractional, 1, floor_value)]
        stack.append(high_branch)
        stack.append(low_branch)

    print("NO")


if __name__ == "__main__":
    main()