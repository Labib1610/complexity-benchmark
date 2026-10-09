import sys
import random
from collections import deque

sys.setrecursionlimit(1_000_000)

EPS = 1e-9
INT_EPS = 1e-6


class Dinic:
    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]
        self.level = [0] * n
        self.it = [0] * n

    def add_edge(self, u, v, cap):
        idx = len(self.g[u])
        self.g[u].append([v, len(self.g[v]), cap])
        self.g[v].append([u, idx, 0])
        return idx

    def bfs(self, s, t):
        self.level = [-1] * self.n
        self.level[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for v, rev, cap in self.g[u]:
                if cap > 0 and self.level[v] < 0:
                    self.level[v] = self.level[u] + 1
                    q.append(v)
        return self.level[t] >= 0

    def dfs(self, u, t, pushed):
        if u == t:
            return pushed
        while self.it[u] < len(self.g[u]):
            idx = self.it[u]
            e = self.g[u][idx]
            v, rev, cap = e
            if cap > 0 and self.level[v] == self.level[u] + 1:
                got = self.dfs(v, t, min(pushed, cap))
                if got:
                    e[2] -= got
                    self.g[v][rev][2] += got
                    return got
            self.it[u] += 1
        return 0

    def max_flow(self, s, t, limit):
        if s == t:
            return limit
        total = 0
        while total < limit and self.bfs(s, t):
            self.it = [0] * self.n
            while total < limit:
                got = self.dfs(s, t, limit - total)
                if not got:
                    break
                total += got
        return total


def sequential_attempt(n, m, commodities, edges, order):
    remaining = [cap for _, _, cap in edges]
    answer = [[0] * m for _ in commodities]

    for ci in order:
        s, t, demand = commodities[ci]
        if demand == 0 or s == t:
            continue

        dinic = Dinic(n)
        refs = []
        for e, (u, v, _) in enumerate(edges):
            idx = dinic.add_edge(u, v, remaining[e])
            refs.append((u, idx, remaining[e]))

        sent = dinic.max_flow(s, t, demand)
        if sent != demand:
            return None

        row = answer[ci]
        for e, (u, idx, initial) in enumerate(refs):
            used = initial - dinic.g[u][idx][2]
            row[e] = used
            remaining[e] -= used

    return answer


def lp_feasible(base_a, base_b, var_count, lower, upper):
    rows = len(base_a) + len(lower) + len(upper)
    cols = var_count
    d = []

    for row, rhs in zip(base_a, base_b):
        d.append(row[:] + [-1.0, float(rhs)])

    for var, value in lower.items():
        row = [0.0] * (cols + 2)
        row[var] = -1.0
        row[cols] = -1.0
        row[cols + 1] = -float(value)
        d.append(row)

    for var, value in upper.items():
        row = [0.0] * (cols + 2)
        row[var] = 1.0
        row[cols] = -1.0
        row[cols + 1] = float(value)
        d.append(row)

    d.append([0.0] * (cols + 2))
    d.append([0.0] * (cols + 2))
    d[rows + 1][cols] = 1.0

    basic = [cols + i for i in range(rows)]
    nonbasic = list(range(cols)) + [-1]

    def pivot(r, s):
        pivot_value = d[r][s]
        inv = 1.0 / pivot_value
        pivot_row = d[r]

        for i in range(rows + 2):
            if i == r:
                continue
            row_i = d[i]
            coefficient = row_i[s] * inv
            if abs(coefficient) > EPS:
                for j in range(cols + 2):
                    if j != s:
                        row_i[j] -= pivot_row[j] * coefficient

        for j in range(cols + 2):
            if j != s:
                pivot_row[j] *= inv

        for i in range(rows + 2):
            if i != r:
                d[i][s] *= -inv

        pivot_row[s] = inv
        basic[r], nonbasic[s] = nonbasic[s], basic[r]

    if rows:
        r = min(range(rows), key=lambda i: (d[i][cols + 1], basic[i]))
        if d[r][cols + 1] < -EPS:
            pivot(r, cols)

            while True:
                objective_row = d[rows + 1]
                s = -1
                for j in range(cols + 1):
                    if s == -1:
                        s = j
                    elif objective_row[j] < objective_row[s] - EPS:
                        s = j
                    elif abs(objective_row[j] - objective_row[s]) <= EPS:
                        if nonbasic[j] < nonbasic[s]:
                            s = j

                if s == -1 or objective_row[s] >= -EPS:
                    break

                chosen = -1
                best_ratio = 0.0
                for i in range(rows):
                    coefficient = d[i][s]
                    if coefficient > EPS:
                        ratio = d[i][cols + 1] / coefficient
                        if chosen == -1 or ratio < best_ratio - EPS:
                            chosen = i
                            best_ratio = ratio
                        elif abs(ratio - best_ratio) <= EPS and basic[i] < basic[chosen]:
                            chosen = i

                if chosen == -1:
                    return None
                pivot(chosen, s)

            if d[rows + 1][cols + 1] < -1e-7:
                return None

    result = [0.0] * cols
    for i in range(rows):
        if 0 <= basic[i] < cols:
            result[basic[i]] = d[i][cols + 1]

    for i, x in enumerate(result):
        if abs(x) < INT_EPS:
            result[i] = 0.0
    return result


def validate_solution(n, m, commodities, edges, answer):
    totals = [0] * m
    for i, (s, t, demand) in enumerate(commodities):
        if s == t:
            continue
        balance = [0] * n
        for e, (u, v, _) in enumerate(edges):
            x = answer[i][e]
            if x < 0:
                return False
            totals[e] += x
            balance[u] += x
            balance[v] -= x
        for v in range(n):
            expected = demand if v == s else (-demand if v == t else 0)
            if balance[v] != expected:
                return False

    for e, (_, _, cap) in enumerate(edges):
        if totals[e] > cap:
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
        demand = next(it)
        commodities.append((s, t, demand))

    edges = []
    for _ in range(m):
        u = next(it) - 1
        v = next(it) - 1
        cap = next(it)
        edges.append((u, v, cap))

    orders = []
    seen_orders = set()

    def add_order(order):
        key = tuple(order)
        if key not in seen_orders:
            seen_orders.add(key)
            orders.append(list(order))

    base_order = list(range(k))
    add_order(base_order)
    add_order(sorted(base_order, key=lambda i: -commodities[i][2]))
    add_order(sorted(base_order, key=lambda i: commodities[i][2]))

    rng = random.Random(712367821)
    extra_attempts = 12 if k * max(1, m) <= 200000 else 3
    for _ in range(extra_attempts):
        order = base_order[:]
        rng.shuffle(order)
        add_order(order)

    for order in orders:
        answer = sequential_attempt(n, m, commodities, edges, order)
        if answer is not None and validate_solution(n, m, commodities, edges, answer):
            out = ["YES"]
            out.extend(" ".join(map(str, row)) for row in answer)
            sys.stdout.write("\n".join(out))
            return

    active = [
        i for i, (s, t, demand) in enumerate(commodities)
        if demand > 0 and s != t
    ]

    if not active:
        answer = [[0] * m for _ in range(k)]
        out = ["YES"]
        out.extend(" ".join(map(str, row)) for row in answer)
        sys.stdout.write("\n".join(out))
        return

    active_count = len(active)
    var_count = active_count * m
    base_a = []
    base_b = []

    # Shared edge capacities.
    for e, (_, _, cap) in enumerate(edges):
        row = [0.0] * var_count
        for ai in range(active_count):
            row[ai * m + e] = 1.0
        base_a.append(row)
        base_b.append(cap)

    outgoing = [[] for _ in range(n)]
    incoming = [[] for _ in range(n)]
    for e, (u, v, _) in enumerate(edges):
        outgoing[u].append(e)
        incoming[v].append(e)

    # Flow conservation equalities, with one redundant vertex omitted.
    for ai, original_i in enumerate(active):
        s, t, demand = commodities[original_i]
        offset = ai * m
        for v in range(max(0, n - 1)):
            row = [0.0] * var_count
            for e in outgoing[v]:
                row[offset + e] += 1.0
            for e in incoming[v]:
                row[offset + e] -= 1.0

            rhs = demand if v == s else (-demand if v == t else 0)
            base_a.append(row)
            base_b.append(rhs)
            base_a.append([-x for x in row])
            base_b.append(-rhs)

    stack = [({}, {})]

    while stack:
        lower, upper = stack.pop()
        solution = lp_feasible(base_a, base_b, var_count, lower, upper)
        if solution is None:
            continue

        branch_var = -1
        branch_fraction = -1.0
        rounded_values = [0] * var_count

        for j, x in enumerate(solution):
            nearest = round(x)
            diff = abs(x - nearest)
            rounded_values[j] = int(nearest)
            if diff > INT_EPS:
                score = min(x - int(x), int(x) + 1 - x)
                if score > branch_fraction:
                    branch_fraction = score
                    branch_var = j

        if branch_var == -1:
            answer = [[0] * m for _ in range(k)]
            for ai, original_i in enumerate(active):
                answer[original_i] = rounded_values[ai * m:(ai + 1) * m]

            if validate_solution(n, m, commodities, edges, answer):
                out = ["YES"]
                out.extend(" ".join(map(str, row)) for row in answer)
                sys.stdout.write("\n".join(out))
                return
            continue

        x = solution[branch_var]
        floor_value = int(x // 1)
        ceil_value = floor_value + 1

        current_low = lower.get(branch_var, 0)
        current_up = upper.get(branch_var, None)

        # Push less promising branch first because the stack is LIFO.
        if x - floor_value < 0.5:
            branch_sequence = ("lower", "upper")
        else:
            branch_sequence = ("upper", "lower")

        for kind in branch_sequence:
            if kind == "upper":
                new_up = floor_value if current_up is None else min(current_up, floor_value)
                if new_up >= current_low:
                    child_upper = upper.copy()
                    child_upper[branch_var] = new_up
                    stack.append((lower.copy(), child_upper))
            else:
                new_low = max(current_low, ceil_value)
                if current_up is None or new_low <= current_up:
                    child_lower = lower.copy()
                    child_lower[branch_var] = new_low
                    stack.append((child_lower, upper.copy()))

    sys.stdout.write("NO")


if __name__ == "__main__":
    main()