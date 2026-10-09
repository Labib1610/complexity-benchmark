import sys
import math

EPS = 1e-9
INT_EPS = 1e-6


class LPSolver:
    def __init__(self, A, b, variables):
        self.m = len(b)
        self.n = variables
        m, n = self.m, self.n

        self.B = [n + i for i in range(m)]
        self.N = list(range(n)) + [-1]
        self.D = [[0.0] * (n + 2) for _ in range(m + 2)]

        for i in range(m):
            row = self.D[i]
            src = A[i]
            for j, value in enumerate(src):
                row[j] = float(value)
            row[n] = -1.0
            row[n + 1] = float(b[i])

        self.D[m + 1][n] = 1.0

    def pivot(self, r, s):
        D = self.D
        m, n = self.m, self.n
        pivot_value = D[r][s]
        inv = 1.0 / pivot_value
        row_r = D[r]

        for i in range(m + 2):
            if i == r:
                continue
            row_i = D[i]
            factor = row_i[s] * inv
            if abs(factor) <= EPS:
                row_i[s] = -factor
                continue
            for j in range(n + 2):
                if j != s:
                    row_i[j] -= row_r[j] * factor
            row_i[s] = -factor

        for j in range(n + 2):
            if j != s:
                row_r[j] *= inv
        row_r[s] = inv

        self.B[r], self.N[s] = self.N[s], self.B[r]

    def simplex(self, phase):
        D = self.D
        m, n = self.m, self.n
        objective_row = m + 1 if phase == 1 else m

        while True:
            s = -1
            for j in range(n + 1):
                if phase == 2 and self.N[j] == -1:
                    continue
                if s == -1:
                    s = j
                else:
                    a = D[objective_row][j]
                    b = D[objective_row][s]
                    if a < b - EPS or (
                        abs(a - b) <= EPS and self.N[j] < self.N[s]
                    ):
                        s = j

            if s == -1 or D[objective_row][s] >= -EPS:
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
        m, n = self.m, self.n

        if m == 0:
            return [0.0] * n

        r = min(range(m), key=lambda i: D[i][n + 1])
        if D[r][n + 1] < -EPS:
            self.pivot(r, n)
            if not self.simplex(1):
                return None
            if D[m + 1][n + 1] < -EPS:
                return None
            if abs(D[m + 1][n + 1]) > 1e-7:
                return None

            for i in range(m):
                if self.B[i] == -1:
                    s = -1
                    for j in range(n + 1):
                        if abs(D[i][j]) <= EPS:
                            continue
                        if s == -1 or self.N[j] < self.N[s]:
                            s = j
                    if s != -1:
                        self.pivot(i, s)

        if not self.simplex(2):
            return None

        result = [0.0] * n
        for i in range(m):
            if 0 <= self.B[i] < n:
                result[self.B[i]] = D[i][n + 1]
        return result


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return

    p = 0
    n, m, k = data[p], data[p + 1], data[p + 2]
    p += 3

    commodities = []
    for _ in range(k):
        s, t, d = data[p] - 1, data[p + 1] - 1, data[p + 2]
        p += 3
        commodities.append((s, t, d))

    edges = []
    graph = [[] for _ in range(n)]
    reverse_graph = [[] for _ in range(n)]

    for edge_id in range(m):
        u, v, cap = data[p] - 1, data[p + 1] - 1, data[p + 2]
        p += 3
        edges.append((u, v, cap))
        if cap > 0 and u != v:
            graph[u].append((v, edge_id))
            reverse_graph[v].append((u, edge_id))

    def reachable(start, adjacency):
        seen = [False] * n
        stack = [start]
        seen[start] = True
        while stack:
            u = stack.pop()
            for v, _ in adjacency[u]:
                if not seen[v]:
                    seen[v] = True
                    stack.append(v)
        return seen

    variable_info = []
    commodity_variables = [[] for _ in range(k)]
    edge_variables = [[] for _ in range(m)]

    for commodity_id, (s, t, demand) in enumerate(commodities):
        if demand == 0 or s == t:
            continue

        from_source = reachable(s, graph)
        if not from_source[t]:
            print("NO")
            return
        to_target = reachable(t, reverse_graph)

        for edge_id, (u, v, cap) in enumerate(edges):
            if cap > 0 and u != v and from_source[u] and to_target[v]:
                variable_id = len(variable_info)
                variable_info.append((commodity_id, edge_id))
                commodity_variables[commodity_id].append(variable_id)
                edge_variables[edge_id].append(variable_id)

    variable_count = len(variable_info)
    base_A = []
    base_b = []

    for commodity_id, (s, t, demand) in enumerate(commodities):
        if demand == 0 or s == t:
            continue

        variables = commodity_variables[commodity_id]
        incident_nodes = {s, t}
        for variable_id in variables:
            _, edge_id = variable_info[variable_id]
            u, v, _ = edges[edge_id]
            incident_nodes.add(u)
            incident_nodes.add(v)

        for node in incident_nodes:
            if node == t:
                continue

            row = [0.0] * variable_count
            for variable_id in variables:
                _, edge_id = variable_info[variable_id]
                u, v, _ = edges[edge_id]
                if u == node:
                    row[variable_id] += 1.0
                if v == node:
                    row[variable_id] -= 1.0

            rhs = demand if node == s else 0
            base_A.append(row)
            base_b.append(rhs)
            base_A.append([-x for x in row])
            base_b.append(-rhs)

    for edge_id, variables in enumerate(edge_variables):
        if not variables:
            continue
        row = [0.0] * variable_count
        for variable_id in variables:
            row[variable_id] = 1.0
        base_A.append(row)
        base_b.append(edges[edge_id][2])

    if variable_count == 0:
        for s, t, demand in commodities:
            if demand != 0 and s != t:
                print("NO")
                return
        print("YES")
        zero_line = " ".join(["0"] * m)
        for _ in range(k):
            print(zero_line)
        return

    def solve_with_branches(branches):
        A = list(base_A)
        b = list(base_b)
        for variable_id, coefficient, rhs in branches:
            row = [0.0] * variable_count
            row[variable_id] = coefficient
            A.append(row)
            b.append(rhs)
        return LPSolver(A, b, variable_count).solve()

    def verify(values):
        result = [[0] * m for _ in range(k)]
        for variable_id, value in enumerate(values):
            commodity_id, edge_id = variable_info[variable_id]
            result[commodity_id][edge_id] = value

        for edge_id, (_, _, cap) in enumerate(edges):
            if sum(result[c][edge_id] for c in range(k)) > cap:
                return None

        for commodity_id, (s, t, demand) in enumerate(commodities):
            if s == t:
                continue
            balance = [0] * n
            for edge_id, (u, v, _) in enumerate(edges):
                value = result[commodity_id][edge_id]
                balance[u] += value
                balance[v] -= value

            for node in range(n):
                required = demand if node == s else (-demand if node == t else 0)
                if balance[node] != required:
                    return None

        return result

    stack = [tuple()]

    while stack:
        branches = stack.pop()
        solution = solve_with_branches(branches)
        if solution is None:
            continue

        fractional_variable = -1
        best_fractionality = -1.0

        for i, value in enumerate(solution):
            nearest = round(value)
            difference = abs(value - nearest)
            if difference > INT_EPS:
                fractionality = min(value - math.floor(value), math.ceil(value) - value)
                if fractionality > best_fractionality:
                    best_fractionality = fractionality
                    fractional_variable = i

        if fractional_variable == -1:
            integer_values = [max(0, int(round(x))) for x in solution]
            result = verify(integer_values)
            if result is not None:
                out = ["YES"]
                out.extend(" ".join(map(str, row)) for row in result)
                sys.stdout.write("\n".join(out))
                return

            fractional_variable = max(
                range(variable_count),
                key=lambda i: abs(solution[i] - round(solution[i]))
            )

        value = solution[fractional_variable]
        lower = math.floor(value)
        upper = lower + 1

        left_branch = branches + ((fractional_variable, 1.0, lower),)
        right_branch = branches + ((fractional_variable, -1.0, -upper),)

        stack.append(right_branch)
        stack.append(left_branch)

    print("NO")


if __name__ == "__main__":
    main()