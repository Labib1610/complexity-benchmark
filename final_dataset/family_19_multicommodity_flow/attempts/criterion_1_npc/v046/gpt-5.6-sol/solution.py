import sys
import random
import itertools
from collections import deque


def verify_solution(n, m, k, orders, edges, flows):
    if flows is None or len(flows) != k:
        return False

    used = [0] * m
    for i, (s, t, d) in enumerate(orders):
        if len(flows[i]) != m:
            return False
        balance = [0] * n
        for j, (u, v, _) in enumerate(edges):
            x = flows[i][j]
            if x < 0:
                return False
            used[j] += x
            balance[u] += x
            balance[v] -= x

        for v in range(n):
            required = 0
            if v == s:
                required += d
            if v == t:
                required -= d
            if balance[v] != required:
                return False

    for j, (_, _, cap) in enumerate(edges):
        if used[j] > cap:
            return False
    return True


def solve_with_milp(n, m, k, orders, edges):
    try:
        import numpy as np
        from scipy.optimize import milp, LinearConstraint, Bounds
        from scipy.sparse import coo_matrix
    except Exception:
        return None

    variables = k * m
    if variables == 0:
        answer = [[0] * m for _ in range(k)]
        return answer if verify_solution(n, m, k, orders, edges, answer) else None

    try:
        ids = np.arange(variables, dtype=np.int64)
        commodities = ids // m
        edge_ids = ids % m

        edge_u = np.asarray([e[0] for e in edges], dtype=np.int64)
        edge_v = np.asarray([e[1] for e in edges], dtype=np.int64)

        rows = np.concatenate((
            commodities * n + edge_u[edge_ids],
            commodities * n + edge_v[edge_ids],
            k * n + edge_ids
        ))
        cols = np.concatenate((ids, ids, ids))
        data = np.concatenate((
            np.ones(variables, dtype=np.float64),
            -np.ones(variables, dtype=np.float64),
            np.ones(variables, dtype=np.float64)
        ))

        total_constraints = k * n + m
        matrix = coo_matrix(
            (data, (rows, cols)),
            shape=(total_constraints, variables)
        ).tocsc()

        del rows, cols, data, ids, commodities, edge_ids

        rhs = np.zeros(k * n, dtype=np.float64)
        for i, (s, t, d) in enumerate(orders):
            rhs[i * n + s] += d
            rhs[i * n + t] -= d

        lower = np.concatenate((
            rhs,
            np.full(m, -np.inf, dtype=np.float64)
        ))
        upper = np.concatenate((
            rhs,
            np.asarray([e[2] for e in edges], dtype=np.float64)
        ))

        objective = np.ones(variables, dtype=np.float64)
        integrality = np.ones(variables, dtype=np.uint8)

        result = milp(
            c=objective,
            integrality=integrality,
            bounds=Bounds(
                np.zeros(variables, dtype=np.float64),
                np.full(variables, np.inf, dtype=np.float64)
            ),
            constraints=LinearConstraint(matrix, lower, upper),
            options={
                "time_limit": 4.0,
                "mip_rel_gap": 0.0,
                "presolve": True
            }
        )

        if result.x is None:
            return None

        rounded = np.rint(result.x).astype(object)
        answer = [
            [int(rounded[i * m + j]) for j in range(m)]
            for i in range(k)
        ]
        return answer if verify_solution(n, m, k, orders, edges, answer) else None
    except Exception:
        return None


class Dinic:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]

    def add_edge(self, u, v, cap):
        forward = [v, len(self.graph[v]), cap]
        backward = [u, len(self.graph[u]), 0]
        self.graph[u].append(forward)
        self.graph[v].append(backward)
        return forward

    def max_flow(self, source, sink, limit):
        if source == sink:
            return limit

        total = 0
        n = self.n
        graph = self.graph

        while total < limit:
            level = [-1] * n
            level[source] = 0
            queue = deque([source])

            while queue:
                u = queue.popleft()
                for edge in graph[u]:
                    if edge[2] > 0 and level[edge[0]] < 0:
                        level[edge[0]] = level[u] + 1
                        queue.append(edge[0])

            if level[sink] < 0:
                break

            ptr = [0] * n

            def dfs(u, pushed):
                if u == sink:
                    return pushed
                while ptr[u] < len(graph[u]):
                    edge = graph[u][ptr[u]]
                    v, rev, cap = edge
                    if cap > 0 and level[v] == level[u] + 1:
                        sent = dfs(v, min(pushed, cap))
                        if sent:
                            edge[2] -= sent
                            graph[v][rev][2] += sent
                            return sent
                    ptr[u] += 1
                return 0

            while total < limit:
                sent = dfs(source, limit - total)
                if sent == 0:
                    break
                total += sent

        return total


def greedy_attempt(n, m, k, orders, edges, order, edge_order):
    remaining = [cap for _, _, cap in edges]
    answer = [[0] * m for _ in range(k)]

    for commodity in order:
        s, t, demand = orders[commodity]
        if demand == 0 or s == t:
            continue

        dinic = Dinic(n)
        references = [None] * m

        for j in edge_order:
            u, v, _ = edges[j]
            references[j] = dinic.add_edge(u, v, remaining[j])

        sent = dinic.max_flow(s, t, demand)
        if sent != demand:
            return None

        for j in range(m):
            used = remaining[j] - references[j][2]
            answer[commodity][j] = used
            remaining[j] -= used

    return answer if verify_solution(n, m, k, orders, edges, answer) else None


def solve_fallback(n, m, k, orders, edges):
    if any(d < 0 for _, _, d in orders):
        return None

    base_edges = list(range(m))
    candidate_orders = []

    natural = tuple(range(k))
    candidate_orders.append(natural)
    candidate_orders.append(tuple(sorted(range(k), key=lambda i: -orders[i][2])))

    if k <= 7:
        for permutation in itertools.permutations(range(k)):
            candidate_orders.append(permutation)
            if len(candidate_orders) >= 160:
                break
    else:
        rng = random.Random(712367821)
        for _ in range(158):
            permutation = list(range(k))
            rng.shuffle(permutation)
            candidate_orders.append(tuple(permutation))

    rng = random.Random(918273645)
    seen = set()
    for attempt, order in enumerate(candidate_orders):
        if (order, attempt == 0) in seen:
            continue
        seen.add((order, attempt == 0))

        edge_order = base_edges[:]
        if attempt:
            rng.shuffle(edge_order)

        answer = greedy_attempt(n, m, k, orders, edges, order, edge_order)
        if answer is not None:
            return answer

    return None


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 3:
        return

    pos = 0
    n, m, k = data[pos], data[pos + 1], data[pos + 2]
    pos += 3

    orders = []
    for _ in range(k):
        s, t, d = data[pos], data[pos + 1], data[pos + 2]
        pos += 3
        orders.append((s - 1, t - 1, d))

    edges = []
    for _ in range(m):
        u, v, cap = data[pos], data[pos + 1], data[pos + 2]
        pos += 3
        edges.append((u - 1, v - 1, cap))

    answer = solve_with_milp(n, m, k, orders, edges)
    if answer is None:
        answer = solve_fallback(n, m, k, orders, edges)

    if answer is None:
        sys.stdout.write("NO\n")
        return

    output = ["YES"]
    output.extend(" ".join(map(str, row)) for row in answer)
    sys.stdout.write("\n".join(output) + "\n")


if __name__ == "__main__":
    main()