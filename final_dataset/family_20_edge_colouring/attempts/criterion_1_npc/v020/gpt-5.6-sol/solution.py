import sys
import heapq

sys.setrecursionlimit(1000000)


class SATSolver:
    def __init__(self, num_vars):
        self.num_vars = num_vars
        self.clauses = []
        self.watches = [[] for _ in range(2 * num_vars)]
        self.units = []

        self.value = [-1] * num_vars
        self.level = [0] * num_vars
        self.reason = [-1] * num_vars
        self.phase = [0] * num_vars

        self.trail = []
        self.trail_lim = []
        self.qhead = 0

        self.activity = [0.0] * num_vars
        self.var_inc = 1.0
        self.var_decay = 0.95
        self.heap = [(0.0, v) for v in range(num_vars)]
        heapq.heapify(self.heap)

    @staticmethod
    def watch_index(lit):
        v = abs(lit) - 1
        return 2 * v + (1 if lit < 0 else 0)

    def lit_value(self, lit):
        val = self.value[abs(lit) - 1]
        if val == -1:
            return -1
        return val if lit > 0 else 1 - val

    def add_clause(self, clause):
        ci = len(self.clauses)
        self.clauses.append(clause)

        for lit in clause:
            self.activity[abs(lit) - 1] += 0.001

        if len(clause) == 1:
            self.units.append((clause[0], ci))
        else:
            self.watches[self.watch_index(clause[0])].append(ci)
            self.watches[self.watch_index(clause[1])].append(ci)
        return ci

    def enqueue(self, lit, reason):
        v = abs(lit) - 1
        wanted = 1 if lit > 0 else 0
        if self.value[v] != -1:
            return self.value[v] == wanted

        self.value[v] = wanted
        self.phase[v] = wanted
        self.level[v] = len(self.trail_lim)
        self.reason[v] = reason
        self.trail.append(lit)
        return True

    def propagate(self):
        while self.qhead < len(self.trail):
            true_lit = self.trail[self.qhead]
            self.qhead += 1
            false_lit = -true_lit
            wi = self.watch_index(false_lit)
            old_watch = self.watches[wi]
            new_watch = []
            pos = 0

            while pos < len(old_watch):
                ci = old_watch[pos]
                pos += 1
                clause = self.clauses[ci]

                if clause[0] != false_lit:
                    clause[0], clause[1] = clause[1], clause[0]

                other = clause[1]
                if self.lit_value(other) == 1:
                    new_watch.append(ci)
                    continue

                replacement = -1
                for k in range(2, len(clause)):
                    if self.lit_value(clause[k]) != 0:
                        replacement = k
                        break

                if replacement != -1:
                    clause[0], clause[replacement] = clause[replacement], clause[0]
                    self.watches[self.watch_index(clause[0])].append(ci)
                    continue

                new_watch.append(ci)
                other_value = self.lit_value(other)
                if other_value == 0:
                    new_watch.extend(old_watch[pos:])
                    self.watches[wi] = new_watch
                    return ci

                if not self.enqueue(other, ci):
                    new_watch.extend(old_watch[pos:])
                    self.watches[wi] = new_watch
                    return ci

            self.watches[wi] = new_watch

        return -1

    def bump_variable(self, v):
        self.activity[v] += self.var_inc
        heapq.heappush(self.heap, (-self.activity[v], v))

        if self.activity[v] > 1e100:
            for i in range(self.num_vars):
                self.activity[i] *= 1e-100
            self.var_inc *= 1e-100
            self.heap = [(-self.activity[v], v) for v in range(self.num_vars)
                         if self.value[v] == -1]
            heapq.heapify(self.heap)

    def analyze(self, conflict_clause):
        seen = [False] * self.num_vars
        learned = [0]
        path_count = 0
        trail_pos = len(self.trail) - 1
        clause = self.clauses[conflict_clause]
        current_level = len(self.trail_lim)
        skip_var = -1

        while True:
            for lit in clause:
                v = abs(lit) - 1
                if v == skip_var or seen[v] or self.level[v] == 0:
                    continue
                seen[v] = True
                self.bump_variable(v)
                if self.level[v] == current_level:
                    path_count += 1
                else:
                    learned.append(lit)

            while True:
                p = self.trail[trail_pos]
                trail_pos -= 1
                pv = abs(p) - 1
                if seen[pv]:
                    break

            seen[pv] = False
            path_count -= 1

            if path_count == 0:
                learned[0] = -p
                break

            skip_var = pv
            reason = self.reason[pv]
            clause = self.clauses[reason]

        backtrack_level = 0
        if len(learned) > 1:
            best = 1
            for i in range(2, len(learned)):
                if self.level[abs(learned[i]) - 1] > self.level[abs(learned[best]) - 1]:
                    best = i
            learned[1], learned[best] = learned[best], learned[1]
            backtrack_level = self.level[abs(learned[1]) - 1]

        self.var_inc /= self.var_decay
        return learned, backtrack_level

    def backtrack(self, target_level):
        if len(self.trail_lim) <= target_level:
            return

        cutoff = self.trail_lim[target_level]
        for i in range(len(self.trail) - 1, cutoff - 1, -1):
            v = abs(self.trail[i]) - 1
            self.value[v] = -1
            self.reason[v] = -1
            self.level[v] = 0
            heapq.heappush(self.heap, (-self.activity[v], v))

        del self.trail[cutoff:]
        del self.trail_lim[target_level:]
        self.qhead = len(self.trail)

    def choose_variable(self):
        while self.heap:
            neg_activity, v = heapq.heappop(self.heap)
            if self.value[v] != -1:
                continue
            if neg_activity != -self.activity[v]:
                continue
            return v
        return -1

    def solve(self):
        for lit, reason in self.units:
            if not self.enqueue(lit, reason):
                return False

        if self.propagate() != -1:
            return False

        conflicts_since_restart = 0
        restart_limit = 100

        while True:
            conflict = self.propagate()

            if conflict != -1:
                if len(self.trail_lim) == 0:
                    return False

                learned, backtrack_level = self.analyze(conflict)
                self.backtrack(backtrack_level)
                ci = self.add_clause(learned)

                if not self.enqueue(learned[0], ci):
                    return False

                conflicts_since_restart += 1
                if conflicts_since_restart >= restart_limit:
                    self.backtrack(0)
                    conflicts_since_restart = 0
                    restart_limit = int(restart_limit * 1.5) + 1
                continue

            v = self.choose_variable()
            if v == -1:
                return True

            self.trail_lim.append(len(self.trail))
            lit = (v + 1) if self.phase[v] == 1 else -(v + 1)
            self.enqueue(lit, -1)


def main():
    data = list(map(int, sys.stdin.buffer.read().split()))
    if len(data) < 2:
        return

    n, m = data[0], data[1]
    edges = []
    incident = [[] for _ in range(n)]
    graph = [[] for _ in range(n)]

    p = 2
    for eid in range(m):
        u = data[p] - 1
        v = data[p + 1] - 1
        p += 2
        edges.append((u, v))
        incident[u].append(eid)
        incident[v].append(eid)
        graph[u].append((v, eid))
        graph[v].append((u, eid))

    if m * 2 != 3 * n or any(len(incident[v]) != 3 for v in range(n)):
        print("NO")
        return

    tin = [-1] * n
    low = [0] * n
    timer = 0
    has_bridge = False

    def dfs(v, parent_edge):
        nonlocal timer, has_bridge
        tin[v] = low[v] = timer
        timer += 1

        for to, eid in graph[v]:
            if eid == parent_edge:
                continue
            if tin[to] != -1:
                low[v] = min(low[v], tin[to])
            else:
                dfs(to, eid)
                low[v] = min(low[v], low[to])
                if low[to] > tin[v]:
                    has_bridge = True

    component_roots = []
    for v in range(n):
        if tin[v] == -1:
            component_roots.append(v)
            dfs(v, -1)

    if has_bridge:
        print("NO")
        return

    num_vars = 3 * m
    solver = SATSolver(num_vars)

    def var(eid, color):
        return 3 * eid + color + 1

    # Every edge receives at least one color.
    for eid in range(m):
        solver.add_clause([var(eid, 0), var(eid, 1), var(eid, 2)])

    # At a vertex, no two incident edges may have the same color.
    # Together with the edge clauses and degree 3, this also guarantees
    # that every edge receives exactly one color.
    for v in range(n):
        a, b, c = incident[v]
        for color in range(3):
            solver.add_clause([-var(a, color), -var(b, color)])
            solver.add_clause([-var(a, color), -var(c, color)])
            solver.add_clause([-var(b, color), -var(c, color)])

    # Remove the global color-permutation symmetry in every component.
    for root in component_roots:
        for color, eid in enumerate(incident[root]):
            solver.add_clause([var(eid, color)])

    if not solver.solve():
        print("NO")
        return

    answer = []
    for eid in range(m):
        chosen = 0
        for color in range(3):
            if solver.value[3 * eid + color] == 1:
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