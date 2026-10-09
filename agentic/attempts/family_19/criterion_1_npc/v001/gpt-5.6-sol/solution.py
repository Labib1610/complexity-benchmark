import sys
from collections import deque, defaultdict
import math


EPS = 1e-8


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
            ri[s] = -dis * inv

        rr = D[r]
        for j in range(n + 2):
            if j != s:
                rr[j] *= inv
        rr[s] = inv
        self.B[r], self.N[s] = self.N[s], self.B[r]

    def simplex(self, phase):
        D = self.D
        m, n = self.m, self.n
        obj = m + 1 if phase == 1 else m

        while True:
            s = -1
            for j in range(n + 1):
                if phase == 2 and self.N[j] == -1:
                    continue
                if s == -1 or D[obj][j] < D[obj][s] - EPS or (
                    abs(D[obj][j] - D[obj][s]) <= EPS
                    and self.N[j] < self.N[s]
                ):
                    s = j

            if D[obj][s] >= -EPS:
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
        D = self.D
        m, n = self.m, self.n

        r = min(range(m), key=lambda i: D[i][n + 1], default=-1)
        if r != -1 and D[r][n + 1] < -EPS:
            self.pivot(r, n)
            if not self.simplex(1) or D[m + 1][n + 1] < -EPS:
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


def reachability(start, graph, n):
    seen = [False] * n
    seen[start] = True
    q = deque([start])
    while q:
        u = q.popleft()
        for v in graph[u]:
            if not seen[v]:
                seen[v] = True
                q.append(v)
    return seen


def solve_with_scipy(num_vars, edge_vars, caps, balance_rows):
    try:
        import numpy as np
        from scipy.optimize import milp, LinearConstraint, Bounds
        from scipy.sparse import coo_matrix
    except Exception:
        return None, False

    rows = []
    cols = []
    data = []
    lower = []
    upper = []
    row_id = 0

    for e, variables in enumerate(edge_vars):
        for idx in variables:
            rows.append(row_id)
            cols.append(idx)
            data.append(1.0)
        lower.append(-np.inf)
        upper.append(float(caps[e]))
        row_id += 1

    for coeffs, rhs in balance_rows:
        for idx, value in coeffs:
            rows.append(row_id)
            cols.append(idx)
            data.append(float(value))
        lower.append(float(rhs))
        upper.append(float(rhs))
        row_id += 1

    A = coo_matrix((data, (rows, cols)), shape=(row_id, num_vars)).tocsr()
    try:
        result = milp(
            c=np.zeros(num_vars),
            integrality=np.ones(num_vars, dtype=np.int8),
            bounds=Bounds(np.zeros(num_vars), np.full(num_vars, np.inf)),
            constraints=LinearConstraint(
                A, np.asarray(lower), np.asarray(upper)
            ),
            options={"presolve": True},
        )
    except Exception:
        return None, False

    if result.success and result.x is not None:
        return [int(round(v)) for v in result.x], True
    if getattr(result, "status", None) == 2:
        return None, True
    return None, False


def solve_with_custom_lp(num_vars, edge_vars, caps, balance_rows):
    base_A = []
    base_b = []

    for e, variables in enumerate(edge_vars):
        row = [0.0] * num_vars
        for idx in variables:
            row[idx] = 1.0
        base_A.append(row)
        base_b.append(float(caps[e]))

    for coeffs, rhs in balance_rows:
        row = [0.0] * num_vars
        for idx, value in coeffs:
            row[idx] += value
        base_A.append(row)
        base_b.append(float(rhs))
        base_A.append([-v for v in row])
        base_b.append(float(-rhs))

    stack = [[]]
    while stack:
        branch_constraints = stack.pop()
        A = base_A[:]
        b = base_b[:]

        for var, sign, bound in branch_constraints:
            row = [0.0] * num_vars
            row[var] = float(sign)
            A.append(row)
            b.append(float(bound))

        lp = LPSolver(A, b, [0.0] * num_vars)
        x = lp.solve()
        if x is None:
            continue

        branch_var = -1
        best_fractionality = 0.0
        for i, value in enumerate(x):
            nearest = round(value)
            diff = abs(value - nearest)
            if diff > 1e-6:
                score = min(value - math.floor(value), math.ceil(value) - value)
                if score > best_fractionality:
                    best_fractionality = score
                    branch_var = i

        if branch_var == -1:
            return [max(0, int(round(v))) for v in x]

        value = x[branch_var]
        lo = math.floor(value)
        hi = math.ceil(value)

        # x >= hi  <=>  -x <= -hi
        stack.append(branch_constraints + [(branch_var, -1, -hi)])
        # x <= lo
        stack.append(branch_constraints + [(branch_var, 1, lo)])

    return None


def main():
    input_data = list(map(int, sys.stdin.buffer.read().split()))
    if not input_data:
        return
    it = iter(input_data)
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
    reverse_graph = [[] for _ in range(n)]
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        cap = next(it)
        edges.append((u, v, cap))
        if u != v:
            graph[u].append(v)
            reverse_graph[v].append(u)

    groups_dict = defaultdict(list)
    for i, (s, t, d) in enumerate(commodities):
        if d > 0 and s != t:
            groups_dict[(s, t)].append(i)

    groups = []
    for (s, t), members in groups_dict.items():
        demand = sum(commodities[i][2] for i in members)
        groups.append((s, t, demand, members))

    answer = [[0] * m for _ in range(k)]

    if not groups:
        out = ["YES"]
        out.extend(" ".join(map(str, row)) for row in answer)
        sys.stdout.write("\n".join(out))
        return

    g_count = len(groups)
    var_index = [[-1] * m for _ in range(g_count)]
    var_group = []
    var_edge = []
    edge_vars = [[] for _ in range(m)]

    for g, (s, t, demand, members) in enumerate(groups):
        from_s = reachability(s, graph, n)
        to_t = reachability(t, reverse_graph, n)
        if not from_s[t]:
            print("NO")
            return

        for e, (u, v, cap) in enumerate(edges):
            if cap > 0 and u != v and from_s[u] and to_t[v]:
                idx = len(var_group)
                var_index[g][e] = idx
                var_group.append(g)
                var_edge.append(e)
                edge_vars[e].append(idx)

    num_vars = len(var_group)
    if num_vars == 0:
        print("NO")
        return

    balance_rows = []
    for g, (s, t, demand, members) in enumerate(groups):
        for node in range(n - 1):
            coeffs = []
            for e, (u, v, cap) in enumerate(edges):
                idx = var_index[g][e]
                if idx < 0:
                    continue
                value = 0
                if u == node:
                    value += 1
                if v == node:
                    value -= 1
                if value:
                    coeffs.append((idx, value))
            rhs = demand if node == s else (-demand if node == t else 0)
            balance_rows.append((coeffs, rhs))

    caps = [edge[2] for edge in edges]

    solution, scipy_decided = solve_with_scipy(
        num_vars, edge_vars, caps, balance_rows
    )
    if not scipy_decided:
        solution = solve_with_custom_lp(
            num_vars, edge_vars, caps, balance_rows
        )

    if solution is None:
        print("NO")
        return

    group_flows = [[0] * m for _ in range(g_count)]
    for idx, value in enumerate(solution):
        if value > 0:
            group_flows[var_group[idx]][var_edge[idx]] = value

    # Validate the integer solution.
    for e in range(m):
        if sum(group_flows[g][e] for g in range(g_count)) > caps[e]:
            print("NO")
            return

    for g, (s, t, demand, members) in enumerate(groups):
        balance = [0] * n
        for e, (u, v, cap) in enumerate(edges):
            f = group_flows[g][e]
            balance[u] += f
            balance[v] -= f
        for node in range(n):
            expected = demand if node == s else (-demand if node == t else 0)
            if balance[node] != expected:
                print("NO")
                return

    edge_adjacency = [[] for _ in range(n)]
    for e, (u, v, cap) in enumerate(edges):
        if u != v:
            edge_adjacency[u].append(e)

    # Decompose every grouped flow into paths and distribute them among
    # commodities having the same source and target.
    for g, (s, t, demand, members) in enumerate(groups):
        remaining_flow = group_flows[g][:]
        member_pos = 0
        member_remaining = commodities[members[0]][2]
        total_remaining = demand

        while total_remaining > 0:
            parent_edge = [-1] * n
            seen = [False] * n
            seen[s] = True
            q = deque([s])

            while q and not seen[t]:
                u = q.popleft()
                for e in edge_adjacency[u]:
                    if remaining_flow[e] <= 0:
                        continue
                    v = edges[e][1]
                    if not seen[v]:
                        seen[v] = True
                        parent_edge[v] = e
                        q.append(v)
                        if v == t:
                            break

            if not seen[t]:
                print("NO")
                return

            path = []
            v = t
            path_amount = total_remaining
            while v != s:
                e = parent_edge[v]
                if e < 0:
                    print("NO")
                    return
                path.append(e)
                path_amount = min(path_amount, remaining_flow[e])
                v = edges[e][0]
            path.reverse()

            amount_left = path_amount
            for e in path:
                remaining_flow[e] -= path_amount

            while amount_left > 0:
                while member_pos < len(members) and member_remaining == 0:
                    member_pos += 1
                    if member_pos < len(members):
                        member_remaining = commodities[members[member_pos]][2]

                if member_pos >= len(members):
                    print("NO")
                    return

                take = min(amount_left, member_remaining)
                commodity_id = members[member_pos]
                for e in path:
                    answer[commodity_id][e] += take

                amount_left -= take
                member_remaining -= take
                total_remaining -= take

    out = ["YES"]
    out.extend(" ".join(map(str, row)) for row in answer)
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()