from collections import deque
import sys


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))
    k = int(next(iterator))
    B = int(next(iterator))

    terminals = [int(next(iterator)) - 1 for _ in range(k)]
    term_set = set(terminals)

    edges = []
    adj = [[] for _ in range(n)]
    for i in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        w = int(next(iterator))
        edges.append((u, v, w, i))
        adj[u].append((v, w, i))
        adj[v].append((u, w, i))

    if k <= 1:
        print("YES")
        print(0)
        return

    # Dinic's Algorithm for Min-Cut
    class Dinic:

        def __init__(self, size):
            self.size = size
            self.head = [-1] * size
            self.to = []
            self.cap = []
            self.flow = []
            self.nxt = []
            self.level = [-1] * size
            self.ptr = [0] * size

        def add_edge(self, u, v, c):
            self.nxt.append(self.head[u])
            self.head[u] = len(self.to)
            self.to.append(v)
            self.cap.append(c)
            self.flow.append(0)

            self.nxt.append(self.head[v])
            self.head[v] = len(self.to)
            self.to.append(u)
            self.cap.append(0)
            self.flow.append(0)

        def bfs(self, s, t):
            self.level = [-1] * self.size
            self.level[s] = 0
            q = deque([s])
            while q:
                u = q.popleft()
                e = self.head[u]
                while e != -1:
                    v = self.to[e]
                    if self.cap[e] - self.flow[e] > 0 and self.level[v] < 0:
                        self.level[v] = self.level[u] + 1
                        q.append(v)
                    e = self.nxt[e]
            return self.level[t] >= 0

        def dfs(self, u, t, pushed):
            if pushed == 0 or u == t:
                return pushed
            e = self.ptr[u]
            while e != -1:
                v = self.to[e]
                tr = self.cap[e] - self.flow[e]
                if self.level[v] == self.level[u] + 1 and tr > 0:
                    push = self.dfs(v, t, min(pushed, tr))
                    if push > 0:
                        self.flow[e] += push
                        self.flow[e ^ 1] -= push
                        return push
                e = self.nxt[e]
                self.ptr[u] = e
            return 0

        def max_flow(self, s, t):
            flow = 0
            while self.bfs(s, t):
                self.ptr = list(self.head)
                while True:
                    pushed = self.dfs(s, t, float("inf"))
                    if pushed == 0:
                        break
                    flow += pushed
            return flow

        def get_reachable(self, s):
            visited = [False] * self.size
            visited[s] = True
            q = deque([s])
            while q:
                u = q.popleft()
                e = self.head[u]
                while e != -1:
                    v = self.to[e]
                    if self.cap[e] - self.flow[e] > 0 and not visited[v]:
                        visited[v] = True
                        q.append(v)
                    e = self.nxt[e]
            return visited

    def evaluate_cut(labels):
        cost = 0
        cut_edges = []
        for u, v, w, idx in edges:
            if labels[u] != labels[v]:
                cost += w
                cut_edges.append((u, v))
        return cost, cut_edges

    best_cost = float("inf")
    best_labels = None

    # 1. Isolating cuts heuristic
    iso_cuts = []
    for i, t in enumerate(terminals):
        dinic = Dinic(n + 2)
        s = n
        target = n + 1
        dinic.add_edge(s, t, float("inf"))
        for j, ot in enumerate(terminals):
            if i != j:
                dinic.add_edge(ot, target, float("inf"))
        for u, v, w, _ in edges:
            dinic.add_edge(u, v, w)
            dinic.add_edge(v, u, w)

        cost = dinic.max_flow(s, target)
        reachable = dinic.get_reachable(s)
        iso_cuts.append((cost, i, reachable))

    iso_cuts.sort(key=lambda x: x[0])
    labels = [-1] * n
    for rank in range(k - 1):
        _, term_idx, reachable = iso_cuts[rank]
        for u in range(n):
            if reachable[u] and labels[u] == -1:
                labels[u] = term_idx
    last_term_idx = iso_cuts[k - 1][1]
    for u in range(n):
        if labels[u] == -1:
            labels[u] = last_term_idx

    cost, cut_e = evaluate_cut(labels)
    if cost < best_cost:
        best_cost = cost
        best_labels = list(labels)

    # 2. Local search / Alpha-expansion
    def run_alpha_expansion(cur_labels):
        nonlocal best_cost, best_labels
        improved = True
        while improved:
            improved = False
            for alpha in range(k):
                # Build graph for expansion
                # Vertices: n original, S (alpha), T (keep old)
                dinic = Dinic(n + 2)
                S = n
                T = n + 1
                for i, t in enumerate(terminals):
                    if i == alpha:
                        dinic.add_edge(S, t, float("inf"))
                    else:
                        dinic.add_edge(t, T, float("inf"))

                # For edges
                for u, v, w, _ in edges:
                    lu, lv = cur_labels[u], cur_labels[v]
                    if lu == alpha and lv == alpha:
                        continue
                    elif lu == alpha:
                        dinic.add_edge(v, T, w)
                    elif lv == alpha:
                        dinic.add_edge(u, T, w)
                    elif lu == lv:
                        # auxiliary node
                        aux = dinic.size
                        # dynamically expand dinic size
                        dinic.size += 1
                        dinic.head.append(-1)
                        dinic.level.append(-1)
                        dinic.ptr.append(0)
                        dinic.add_edge(u, aux, w)
                        dinic.add_edge(v, aux, w)
                        dinic.add_edge(aux, T, w)
                    else:
                        dinic.add_edge(u, T, w)
                        dinic.add_edge(v, T, w)

                dinic.max_flow(S, T)
                reach = dinic.get_reachable(S)
                new_labels = list(cur_labels)
                for u in range(n):
                    if reach[u]:
                        new_labels[u] = alpha
                new_cost, _ = evaluate_cut(new_labels)
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_labels = list(new_labels)
                    cur_labels = new_labels
                    improved = True
        return cur_labels

    run_alpha_expansion(best_labels)

    # 3. If best_cost > B, run Branch and Bound
    if best_cost > B:
        # Precompute terminal indices
        term_map = {terminals[i]: i for i in range(k)}
        assigned = [-1] * n
        for i, t in enumerate(terminals):
            assigned[t] = i

        unassigned = [u for u in range(n) if u not in term_map]
        # Order unassigned by max degree
        unassigned.sort(key=lambda u: len(adj[u]), reverse=True)

        def bnb(idx, current_cost):
            nonlocal best_cost, best_labels
            if current_cost >= best_cost or current_cost > B:
                return
            if idx == len(unassigned):
                if current_cost < best_cost:
                    best_cost = current_cost
                    best_labels = list(assigned)
                return

            u = unassigned[idx]

            # Try labels with smallest immediate cost addition
            choices = []
            for label in range(k):
                add_cost = 0
                for v, w, _ in adj[u]:
                    if assigned[v] != -1 and assigned[v] != label:
                        add_cost += w
                choices.append((add_cost, label))
            choices.sort(key=lambda x: x[0])

            for add_cost, label in choices:
                if current_cost + add_cost >= best_cost or current_cost + add_cost > B:
                    continue
                assigned[u] = label
                bnb(idx + 1, current_cost + add_cost)
                assigned[u] = -1

        bnb(0, 0)

    if best_cost <= B and best_labels is not None:
        cost, cut_edges = evaluate_cut(best_labels)
        print("YES")
        print(len(cut_edges))
        for u, v in cut_edges:
            print(f"{u + 1} {v + 1}")
    else:
        print("NO")


if __name__ == "__main__":
    solve()