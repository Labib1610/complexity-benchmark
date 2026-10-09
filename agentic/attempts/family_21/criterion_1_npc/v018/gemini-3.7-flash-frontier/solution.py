import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    B = int(next(it))

    terminals = [int(next(it)) - 1 for _ in range(k)]
    
    edges = []
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        w = int(next(it))
        edges.append((u, v, w))
        adj[u].append((v, w))
        adj[v].append((u, w))

    if k <= 1:
        print("YES")
        print(0)
        return

    # Dinic's algorithm for max flow
    class Dinic:
        def __init__(self, num_nodes):
            self.n = num_nodes
            self.graph = [[] for _ in range(num_nodes)]
            self.edges = []

        def add_edge(self, u, v, cap):
            self.graph[u].append(len(self.edges))
            self.edges.append([v, cap, 0])
            self.graph[v].append(len(self.edges))
            self.edges.append([u, 0, 0])

        def max_flow(self, s, t):
            flow = 0
            while True:
                level = [-1] * self.n
                level[s] = 0
                q = deque([s])
                while q:
                    u = q.popleft()
                    for idx in self.graph[u]:
                        v, cap, f = self.edges[idx]
                        if cap - f > 0 and level[v] == -1:
                            level[v] = level[u] + 1
                            q.append(v)
                if level[t] == -1:
                    break
                ptr = [0] * self.n
                while True:
                    pushed = self.dfs(s, t, float('inf'), level, ptr)
                    if pushed == 0:
                        break
                    flow += pushed
            return flow

        def dfs(self, u, t, pushed, level, ptr):
            if pushed == 0 or u == t:
                return pushed
            for cid in range(ptr[u], len(self.graph[u])):
                ptr[u] = cid
                idx = self.graph[u][cid]
                v, cap, f = self.edges[idx]
                tr = cap - f
                if level[u] + 1 != level[v] or tr == 0:
                    continue
                tr = self.dfs(v, t, min(pushed, tr), level, ptr)
                if tr == 0:
                    continue
                self.edges[idx][2] += tr
                self.edges[idx ^ 1][2] -= tr
                return tr
            return 0

        def min_cut_source_set(self, s):
            visited = [False] * self.n
            visited[s] = True
            q = deque([s])
            while q:
                u = q.popleft()
                for idx in self.graph[u]:
                    v, cap, f = self.edges[idx]
                    if cap - f > 0 and not visited[v]:
                        visited[v] = True
                        q.append(v)
            return visited

    term_set = set(terminals)
    non_terminals = [v for v in range(n) if v not in term_set]

    # Pre-check: approximation to find quick solution and upper bound
    # For each terminal i, compute min-cut separating it from other terminals
    def get_terminal_cuts():
        cuts = []
        for i in range(k):
            # s = terminals[i], t = sink (connect all other terminals to sink with INF)
            dinic = Dinic(n + 1)
            sink = n
            for j in range(k):
                if i != j:
                    dinic.add_edge(terminals[j], sink, float('inf'))
            for u, v, w in edges:
                dinic.add_edge(u, v, w)
                dinic.add_edge(v, u, w)
            flow = dinic.max_flow(terminals[i], sink)
            in_s = dinic.min_cut_source_set(terminals[i])
            cuts.append((flow, [v for v in range(n) if in_s[v]]))
        return cuts

    term_cuts = get_terminal_cuts()
    
    # 2-approximation assignment
    approx_assignment = [-1] * n
    for idx, (fl, s_nodes) in enumerate(term_cuts):
        for node in s_nodes:
            if approx_assignment[node] == -1:
                approx_assignment[node] = idx
    for v in range(n):
        if approx_assignment[v] == -1:
            approx_assignment[v] = 0
    # Ensure terminals are assigned to themselves
    for idx, t in enumerate(terminals):
        approx_assignment[t] = idx

    def eval_assignment(ass):
        cost = 0
        for u, v, w in edges:
            if ass[u] != ass[v]:
                cost += w
        return cost

    best_cost = eval_assignment(approx_assignment)
    best_assignment = list(approx_assignment)

    # Branch and bound to find exact minimum multiway cut
    assignment = [-1] * n
    for idx, t in enumerate(terminals):
        assignment[t] = idx

    def solve_bnb(nt_idx):
        nonlocal best_cost, best_assignment
        if nt_idx == len(non_terminals):
            c = eval_assignment(assignment)
            if c < best_cost:
                best_cost = c
                best_assignment = list(assignment)
            return

        # Lower bound using sum of min-cuts
        # Build flow network
        dinic_lb = 0
        for i in range(k):
            dinic = Dinic(n + 2)
            src = n
            sink = n + 1
            for v in range(n):
                if assignment[v] == i:
                    dinic.add_edge(src, v, float('inf'))
                elif assignment[v] != -1:
                    dinic.add_edge(v, sink, float('inf'))
            for u, v, w in edges:
                dinic.add_edge(u, v, w)
                dinic.add_edge(v, u, w)
            dinic_lb += dinic.max_flow(src, sink)

        if (dinic_lb + 1) // 2 >= best_cost:
            return

        v = non_terminals[nt_idx]
        # Sort branches: try assigning to terminal with largest neighbor edge weight
        weights = [0] * k
        for to, w in adj[v]:
            if assignment[to] != -1:
                weights[assignment[to]] += w

        order = sorted(range(k), key=lambda x: weights[x], reverse=True)
        for cand in order:
            assignment[v] = cand
            solve_bnb(nt_idx + 1)
            assignment[v] = -1

    if len(non_terminals) <= 40:
        # Order non-terminals by degree to terminals
        non_terminals.sort(key=lambda x: sum(w for to, w in adj[x] if to in term_set), reverse=True)
        solve_bnb(0)

    if best_cost <= B:
        welded = []
        for u, v, w in edges:
            if best_assignment[u] != best_assignment[v]:
                welded.append((u + 1, v + 1))
        print("YES")
        print(len(welded))
        for u, v in welded:
            print(f"{u} {v}")
    else:
        print("NO")

if __name__ == '__main__':
    solve()