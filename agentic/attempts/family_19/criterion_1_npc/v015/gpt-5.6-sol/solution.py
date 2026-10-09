import sys
sys.setrecursionlimit(1_000_000)

EPS = 1e-8


class LPSolver:
    def __init__(self, A, b, nvars):
        self.m = len(b)
        self.n = nvars
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

        self.D[m + 1][n] = 1.0

    def pivot(self, r, s):
        D = self.D
        m, n = self.m, self.n
        inv = 1.0 / D[r][s]

        for i in range(m + 2):
            if i == r:
                continue
            factor = D[i][s] * inv
            if abs(factor) <= EPS:
                continue
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
                        abs(lhs - rhs) <= EPS and self.B[i] < self.B[r]
                    ):
                        r = i

            if r == -1:
                return False
            self.pivot(r, s)

    def solve(self):
        D = self.D
        m, n = self.m, self.n

        if m:
            r = min(range(m), key=lambda i: D[i][n + 1])
            if D[r][n + 1] < -EPS:
                self.pivot(r, n)
                if not self.simplex(1):
                    return None
                if D[m + 1][n + 1] < -EPS:
                    return None
                if abs(D[m + 1][n + 1]) > 1e-6:
                    return None

                for i in range(m):
                    if self.B[i] == -1:
                        s = -1
                        for j in range(n + 1):
                            if abs(D[i][j]) <= EPS:
                                continue
                            if s == -1 or D[i][j] < D[i][s] - EPS or (
                                abs(D[i][j] - D[i][s]) <= EPS
                                and self.N[j] < self.N[s]
                            ):
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

    contracts = []
    for _ in range(k):
        s, t, d = data[p] - 1, data[p + 1] - 1, data[p + 2]
        p += 3
        contracts.append((s, t, d))

    edges = []
    capacities = []
    for _ in range(m):
        u, v, c = data[p] - 1, data[p + 1] - 1, data[p + 2]
        p += 3
        edges.append((u, v))
        capacities.append(c)

    if any(d < 0 for _, _, d in contracts) or any(c < 0 for c in capacities):
        print("NO")
        return

    active = [
        i for i, (s, t, d) in enumerate(contracts)
        if d > 0 and s != t
    ]
    q = len(active)

    if q == 0:
        out = ["YES"]
        zero_line = " ".join(["0"] * m)
        for _ in range(k):
            out.append(zero_line)
        print("\n".join(out))
        return

    if m == 0:
        print("NO")
        return

    var_count = q * m
    base_A = []
    base_b = []

    outgoing = [[] for _ in range(n)]
    incoming = [[] for _ in range(n)]
    for e, (u, v) in enumerate(edges):
        outgoing[u].append(e)
        incoming[v].append(e)

    for a, original_idx in enumerate(active):
        s, t, d = contracts[original_idx]
        balance = [0] * n
        balance[s] += d
        balance[t] -= d
        offset = a * m

        for node in range(max(0, n - 1)):
            row = [0] * var_count
            for e in outgoing[node]:
                row[offset + e] += 1
            for e in incoming[node]:
                row[offset + e] -= 1

            rhs = balance[node]
            base_A.append(row)
            base_b.append(rhs)
            base_A.append([-x for x in row])
            base_b.append(-rhs)

    for e in range(m):
        row = [0] * var_count
        for a in range(q):
            row[a * m + e] = 1
        base_A.append(row)
        base_b.append(capacities[e])

    lower = {}
    upper = {}

    def validate(values):
        loads = [0] * m
        for a, original_idx in enumerate(active):
            s, t, d = contracts[original_idx]
            bal = [0] * n
            off = a * m
            for e, (u, v) in enumerate(edges):
                x = values[off + e]
                if x < 0:
                    return False
                loads[e] += x
                bal[u] += x
                bal[v] -= x

            for node in range(n):
                required = d if node == s else (-d if node == t else 0)
                if bal[node] != required:
                    return False

        return all(loads[e] <= capacities[e] for e in range(m))

    def search():
        A = list(base_A)
        b = list(base_b)

        for idx, val in lower.items():
            if val > 0:
                row = [0] * var_count
                row[idx] = -1
                A.append(row)
                b.append(-val)

        for idx, val in upper.items():
            default_ub = capacities[idx % m]
            if val < default_ub:
                row = [0] * var_count
                row[idx] = 1
                A.append(row)
                b.append(val)

        solver = LPSolver(A, b, var_count)
        solution = solver.solve()
        if solution is None:
            return None

        rounded = [int(round(x)) for x in solution]
        if validate(rounded):
            return rounded

        branch_idx = -1
        best_fraction = -1.0
        for i, x in enumerate(solution):
            fraction = abs(x - round(x))
            if fraction > best_fraction:
                best_fraction = fraction
                branch_idx = i

        if branch_idx < 0:
            return None

        x = solution[branch_idx]
        floor_x = int(x // 1)
        if x < floor_x:
            floor_x -= 1
        ceil_x = floor_x + 1

        old_lo = lower.get(branch_idx, 0)
        old_hi = upper.get(branch_idx, capacities[branch_idx % m])

        branches = []
        if x - floor_x <= ceil_x - x:
            branches = [("upper", floor_x), ("lower", ceil_x)]
        else:
            branches = [("lower", ceil_x), ("upper", floor_x)]

        del solver, A, b, solution

        for kind, bound in branches:
            if kind == "upper":
                new_hi = min(old_hi, bound)
                if new_hi < old_lo:
                    continue
                upper[branch_idx] = new_hi
                result = search()
                if old_hi == capacities[branch_idx % m]:
                    upper.pop(branch_idx, None)
                else:
                    upper[branch_idx] = old_hi
            else:
                new_lo = max(old_lo, bound)
                if new_lo > old_hi:
                    continue
                lower[branch_idx] = new_lo
                result = search()
                if old_lo == 0:
                    lower.pop(branch_idx, None)
                else:
                    lower[branch_idx] = old_lo

            if result is not None:
                return result

        return None

    answer = search()
    if answer is None:
        print("NO")
        return

    full = [[0] * m for _ in range(k)]
    for a, original_idx in enumerate(active):
        off = a * m
        full[original_idx] = answer[off:off + m]

    out = ["YES"]
    out.extend(" ".join(map(str, row)) for row in full)
    print("\n".join(out))


if __name__ == "__main__":
    main()