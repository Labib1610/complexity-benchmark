import sys
import random

sys.setrecursionlimit(1_000_000)


class Dinic:
    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]
        self.refs = []

    def add_edge(self, u, v, c, idx):
        fwd = [v, c, None, c, idx]
        rev = [u, 0, fwd, 0, -1]
        fwd[2] = rev
        self.g[u].append(fwd)
        self.g[v].append(rev)
        self.refs.append(fwd)

    def max_flow(self, s, t, limit):
        if limit <= 0 or s == t:
            return 0

        total = 0
        n = self.n

        while total < limit:
            level = [-1] * n
            level[s] = 0
            queue = [s]
            head = 0

            while head < len(queue):
                u = queue[head]
                head += 1
                for e in self.g[u]:
                    if e[1] > 0 and level[e[0]] < 0:
                        level[e[0]] = level[u] + 1
                        queue.append(e[0])

            if level[t] < 0:
                break

            it = [0] * n

            def dfs(u, pushed):
                if u == t:
                    return pushed
                gu = self.g[u]
                while it[u] < len(gu):
                    e = gu[it[u]]
                    if e[1] > 0 and level[e[0]] == level[u] + 1:
                        got = dfs(e[0], min(pushed, e[1]))
                        if got:
                            e[1] -= got
                            e[2][1] += got
                            return got
                    it[u] += 1
                return 0

            while total < limit:
                pushed = dfs(s, limit - total)
                if not pushed:
                    break
                total += pushed

        return total


def get_flow(n, edges, capacities, s, t, demand, need_vector=False):
    if demand == 0 or s == t:
        return (demand, [0] * len(edges)) if need_vector else demand

    dinic = Dinic(n)
    for j, (u, v) in enumerate(edges):
        c = capacities[j]
        if c > 0:
            dinic.add_edge(u, v, c, j)

    value = dinic.max_flow(s, t, demand)

    if not need_vector:
        return value

    result = [0] * len(edges)
    for e in dinic.refs:
        result[e[4]] = e[3] - e[1]
    return value, result


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
    original_cap = []
    adjacency = [[] for _ in range(n)]

    for j in range(m):
        u = next(it) - 1
        v = next(it) - 1
        c = next(it)
        edges.append((u, v))
        original_cap.append(c)
        if c > 0:
            adjacency[u].append((v, j))

    for s, t, d in commodities:
        if d < 0:
            print("NO")
            return
        if s != t and get_flow(n, edges, original_cap, s, t, d) < d:
            print("NO")
            return

    if all(d == 0 or s == t for s, t, d in commodities):
        print("YES")
        zero = " ".join(["0"] * m)
        for _ in range(k):
            print(zero)
        return

    def greedy(order):
        residual = original_cap[:]
        answer = [[0] * m for _ in range(k)]

        for ci in order:
            s, t, d = commodities[ci]
            if d == 0 or s == t:
                continue
            value, flow = get_flow(n, edges, residual, s, t, d, True)
            if value < d:
                return None
            answer[ci] = flow
            for j, x in enumerate(flow):
                residual[j] -= x

        return answer

    orders = []
    orders.append(list(range(k)))
    orders.append(sorted(range(k), key=lambda i: -commodities[i][2]))
    orders.append(sorted(range(k), key=lambda i: commodities[i][2]))

    rng = random.Random(712367821)
    for _ in range(min(24, max(4, k * 2))):
        order = list(range(k))
        rng.shuffle(order)
        orders.append(order)

    seen_orders = set()
    for order in orders:
        key = tuple(order)
        if key in seen_orders:
            continue
        seen_orders.add(key)
        answer = greedy(order)
        if answer is not None:
            out = ["YES"]
            out.extend(" ".join(map(str, row)) for row in answer)
            sys.stdout.write("\n".join(out))
            return

    paths_by_commodity = [[] for _ in range(k)]

    def enumerate_paths(s, t):
        if s == t:
            return [()]
        paths = []
        visited = [False] * n
        visited[s] = True
        current = []

        def dfs(u):
            if u == t:
                paths.append(tuple(current))
                return
            for v, eid in adjacency[u]:
                if not visited[v]:
                    visited[v] = True
                    current.append(eid)
                    dfs(v)
                    current.pop()
                    visited[v] = False

        dfs(s)
        return paths

    for i, (s, t, d) in enumerate(commodities):
        if d == 0 or s == t:
            paths_by_commodity[i] = [()]
        else:
            paths = enumerate_paths(s, t)
            if not paths:
                print("NO")
                return
            paths.sort(
                key=lambda p: (
                    -min(original_cap[e] for e in p),
                    len(p),
                    p
                )
            )
            paths_by_commodity[i] = paths

    order = sorted(
        range(k),
        key=lambda i: (
            0 if commodities[i][2] > 0 and commodities[i][0] != commodities[i][1] else 1,
            len(paths_by_commodity[i]),
            -commodities[i][2]
        )
    )

    residual = original_cap[:]
    answer = [[0] * m for _ in range(k)]
    failed_boundary = set()
    allocation_memo = set()

    def remaining_feasible(pos):
        for q in range(pos, k):
            ci = order[q]
            s, t, d = commodities[ci]
            if d and s != t and get_flow(n, edges, residual, s, t, d) < d:
                return False
        return True

    def solve_commodity(pos):
        if pos == k:
            return True

        boundary_key = (pos, tuple(residual))
        if boundary_key in failed_boundary:
            return False

        if not remaining_feasible(pos):
            failed_boundary.add(boundary_key)
            return False

        ci = order[pos]
        s, t, demand = commodities[ci]

        if demand == 0 or s == t:
            if solve_commodity(pos + 1):
                return True
            failed_boundary.add(boundary_key)
            return False

        paths = paths_by_commodity[ci]
        local_flow = [0] * m

        def allocate(path_index, rem):
            if rem == 0:
                answer[ci] = local_flow[:]
                if solve_commodity(pos + 1):
                    return True
                return False

            if path_index >= len(paths):
                return False

            memo_key = (ci, path_index, rem, tuple(residual))
            if memo_key in allocation_memo:
                return False

            if get_flow(n, edges, residual, s, t, rem) < rem:
                allocation_memo.add(memo_key)
                return False

            path = paths[path_index]
            maximum = rem
            for eid in path:
                if residual[eid] < maximum:
                    maximum = residual[eid]

            for amount in range(maximum, -1, -1):
                if amount:
                    for eid in path:
                        residual[eid] -= amount
                        local_flow[eid] += amount

                if allocate(path_index + 1, rem - amount):
                    return True

                if amount:
                    for eid in path:
                        residual[eid] += amount
                        local_flow[eid] -= amount

            if len(allocation_memo) > 250000:
                allocation_memo.clear()
            allocation_memo.add(memo_key)
            return False

        if allocate(0, demand):
            return True

        failed_boundary.add(boundary_key)
        return False

    if solve_commodity(0):
        out = ["YES"]
        out.extend(" ".join(map(str, row)) for row in answer)
        sys.stdout.write("\n".join(out))
    else:
        print("NO")


if __name__ == "__main__":
    main()