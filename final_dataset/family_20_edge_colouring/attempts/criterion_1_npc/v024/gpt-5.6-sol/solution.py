import sys
import heapq

sys.setrecursionlimit(10000)


class SATSolver:
    def __init__(self, num_vars):
        self.n = num_vars
        self.clauses = []
        self.watch = [[] for _ in range(2 * num_vars)]
        self.assign = [-1] * num_vars
        self.level = [0] * num_vars
        self.reason = [-1] * num_vars
        self.phase = [1] * num_vars
        self.trail = []
        self.trail_lim = []
        self.qhead = 0

        self.activity = [0.0] * num_vars
        self.var_inc = 1.0
        self.var_decay = 0.95
        self.heap = []

    @staticmethod
    def lit_index(lit):
        v = abs(lit) - 1
        return 2 * v + (1 if lit < 0 else 0)

    def lit_value(self, lit):
        val = self.assign[abs(lit) - 1]
        if val == -1:
            return -1
        return val if lit > 0 else 1 - val

    def add_clause(self, clause, learnt=False):
        ci = len(self.clauses)
        self.clauses.append(clause)

        if not learnt:
            for lit in clause:
                self.activity[abs(lit) - 1] += 1.0

        if len(clause) >= 2:
            self.watch[self.lit_index(clause[0])].append(ci)
            self.watch[self.lit_index(clause[1])].append(ci)
        return ci

    def enqueue(self, lit, reason):
        v = abs(lit) - 1
        val = 1 if lit > 0 else 0
        if self.assign[v] != -1:
            return self.assign[v] == val

        self.assign[v] = val
        self.phase[v] = val
        self.level[v] = len(self.trail_lim)
        self.reason[v] = reason
        self.trail.append(lit)
        return True

    def propagate(self):
        while self.qhead < len(self.trail):
            true_lit = self.trail[self.qhead]
            self.qhead += 1
            false_lit = -true_lit

            ws = self.watch[self.lit_index(false_lit)]
            i = 0
            while i < len(ws):
                ci = ws[i]
                clause = self.clauses[ci]

                if clause[0] == false_lit:
                    wi = 0
                elif clause[1] == false_lit:
                    wi = 1
                else:
                    ws[i] = ws[-1]
                    ws.pop()
                    continue

                oi = 1 - wi
                other = clause[oi]

                if self.lit_value(other) == 1:
                    i += 1
                    continue

                replacement = -1
                for k in range(2, len(clause)):
                    if self.lit_value(clause[k]) != 0:
                        replacement = k
                        break

                if replacement != -1:
                    new_lit = clause[replacement]
                    clause[wi], clause[replacement] = clause[replacement], clause[wi]
                    ws[i] = ws[-1]
                    ws.pop()
                    self.watch[self.lit_index(new_lit)].append(ci)
                    continue

                if self.lit_value(other) == 0:
                    return ci

                if not self.enqueue(other, ci):
                    return ci
                i += 1

        return -1

    def bump_variable(self, v):
        self.activity[v] += self.var_inc
        heapq.heappush(self.heap, (-self.activity[v], v))

        if self.activity[v] > 1e100:
            for i in range(self.n):
                self.activity[i] *= 1e-100
            self.var_inc *= 1e-100
            self.heap = [(-self.activity[i], i) for i in range(self.n)
                         if self.assign[i] == -1]
            heapq.heapify(self.heap)

    def analyze(self, conflict_ci):
        learnt = [0]
        seen = [False] * self.n
        touched = []
        path_count = 0
        trail_pos = len(self.trail) - 1
        p = 0
        clause = self.clauses[conflict_ci]
        current_level = len(self.trail_lim)

        while True:
            pv = abs(p) - 1 if p else -1

            for q in clause:
                v = abs(q) - 1
                if v == pv or seen[v] or self.level[v] == 0:
                    continue

                seen[v] = True
                touched.append(v)
                self.bump_variable(v)

                if self.level[v] == current_level:
                    path_count += 1
                else:
                    learnt.append(q)

            while True:
                p = self.trail[trail_pos]
                trail_pos -= 1
                if seen[abs(p) - 1]:
                    break

            v = abs(p) - 1
            seen[v] = False
            path_count -= 1

            if path_count == 0:
                learnt[0] = -p
                break

            clause = self.clauses[self.reason[v]]

        for v in touched:
            seen[v] = False

        if len(learnt) == 1:
            backtrack_level = 0
        else:
            best = 1
            for i in range(2, len(learnt)):
                if self.level[abs(learnt[i]) - 1] > self.level[abs(learnt[best]) - 1]:
                    best = i
            learnt[1], learnt[best] = learnt[best], learnt[1]
            backtrack_level = self.level[abs(learnt[1]) - 1]

        self.var_inc /= self.var_decay
        return learnt, backtrack_level

    def cancel_until(self, target_level):
        current_level = len(self.trail_lim)
        if current_level <= target_level:
            return

        cutoff = self.trail_lim[target_level]
        for i in range(len(self.trail) - 1, cutoff - 1, -1):
            v = abs(self.trail[i]) - 1
            self.assign[v] = -1
            self.level[v] = 0
            self.reason[v] = -1
            heapq.heappush(self.heap, (-self.activity[v], v))

        del self.trail[cutoff:]
        del self.trail_lim[target_level:]
        self.qhead = len(self.trail)

    def choose_variable(self):
        while self.heap:
            neg_activity, v = heapq.heappop(self.heap)
            if self.assign[v] == -1 and neg_activity == -self.activity[v]:
                return v
        return -1

    def solve(self, root_literals):
        self.heap = [(-self.activity[v], v) for v in range(self.n)]
        heapq.heapify(self.heap)

        for lit in root_literals:
            if not self.enqueue(lit, -1):
                return False

        conflict = self.propagate()
        if conflict != -1:
            return False

        conflicts = 0
        restart_interval = 100
        next_restart = restart_interval

        while True:
            conflict = self.propagate()

            if conflict != -1:
                conflicts += 1
                if len(self.trail_lim) == 0:
                    return False

                learnt, backtrack_level = self.analyze(conflict)
                self.cancel_until(backtrack_level)
                ci = self.add_clause(learnt, learnt=True)

                if not self.enqueue(learnt[0], ci):
                    return False

                if conflicts >= next_restart:
                    self.cancel_until(0)
                    restart_interval = int(restart_interval * 1.5) + 1
                    next_restart = conflicts + restart_interval
                continue

            v = self.choose_variable()
            if v == -1:
                return True

            self.trail_lim.append(len(self.trail))
            lit = v + 1 if self.phase[v] else -(v + 1)
            self.enqueue(lit, -1)


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 2:
        return

    n, m = data[0], data[1]
    edges = []
    adj = [[] for _ in range(n)]
    pos = 2

    for eid in range(m):
        u = data[pos] - 1
        v = data[pos + 1] - 1
        pos += 2
        edges.append((u, v))
        adj[u].append((v, eid))
        adj[v].append((u, eid))

    if m * 2 != 3 * n or any(len(adj[v]) != 3 for v in range(n)):
        print("NO")
        return

    # A cubic graph with a bridge cannot have a proper 3-edge-coloring.
    tin = [-1] * n
    low = [0] * n
    timer = 0
    has_bridge = False

    def dfs_bridge(v, parent_eid):
        nonlocal timer, has_bridge
        tin[v] = low[v] = timer
        timer += 1

        for to, eid in adj[v]:
            if eid == parent_eid:
                continue
            if tin[to] != -1:
                low[v] = min(low[v], tin[to])
            else:
                dfs_bridge(to, eid)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    has_bridge = True

    for v in range(n):
        if tin[v] == -1:
            dfs_bridge(v, -1)

    if has_bridge:
        print("NO")
        return

    def var(eid, color):
        return eid * 3 + color + 1

    solver = SATSolver(3 * m)

    # Every edge receives exactly one color.
    for eid in range(m):
        a = var(eid, 0)
        b = var(eid, 1)
        c = var(eid, 2)
        solver.add_clause([a, b, c])
        solver.add_clause([-a, -b])
        solver.add_clause([-a, -c])
        solver.add_clause([-b, -c])

    # No two edges incident to a vertex may receive the same color.
    for v in range(n):
        incident = [eid for _, eid in adj[v]]
        for color in range(3):
            x = var(incident[0], color)
            y = var(incident[1], color)
            z = var(incident[2], color)
            solver.add_clause([-x, -y])
            solver.add_clause([-x, -z])
            solver.add_clause([-y, -z])

    # Break independent color-permutation symmetry in every connected component.
    visited = [False] * n
    root_literals = []

    for start in range(n):
        if visited[start]:
            continue

        stack = [start]
        visited[start] = True
        while stack:
            v = stack.pop()
            for to, _ in adj[v]:
                if not visited[to]:
                    visited[to] = True
                    stack.append(to)

        incident = [eid for _, eid in adj[start]]
        for color in range(3):
            root_literals.append(var(incident[color], color))

    if not solver.solve(root_literals):
        print("NO")
        return

    answer = []
    for eid in range(m):
        chosen = 0
        for color in range(3):
            if solver.assign[var(eid, color) - 1] == 1:
                chosen = color + 1
                break
        if chosen == 0:
            print("NO")
            return
        answer.append(chosen)

    print("YES")
    print(*answer)


if __name__ == "__main__":
    main()