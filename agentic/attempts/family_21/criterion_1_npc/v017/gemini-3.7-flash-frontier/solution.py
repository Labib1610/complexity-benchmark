import sys
from collections import deque

# Increase recursion depth for deep search trees
sys.setrecursionlimit(200000)

class RollbackDSU:
    def __init__(self, n, hub_list):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)
        self.hub = [0] * (n + 1)
        for h in hub_list:
            self.hub[h] = h
        self.history = []

    def find(self, i):
        while self.parent[i] != i:
            i = self.parent[i]
        return i

    def can_union(self, u, v):
        ru = self.find(u)
        rv = self.find(v)
        if ru == rv:
            return True
        if self.hub[ru] != 0 and self.hub[rv] != 0:
            return False
        return True

    def union(self, u, v):
        ru = self.find(u)
        rv = self.find(v)
        if ru == rv:
            return True
        if self.hub[ru] != 0 and self.hub[rv] != 0:
            return False
        if self.rank[ru] < self.rank[rv]:
            ru, rv = rv, ru
        self.history.append((rv, self.parent[rv], ru, self.rank[ru], self.hub[ru]))
        self.parent[rv] = ru
        if self.rank[ru] == self.rank[rv]:
            self.rank[ru] += 1
        if self.hub[ru] == 0:
            self.hub[ru] = self.hub[rv]
        return True

    def rollback(self, checkpoint):
        while len(self.history) > checkpoint:
            rv, p_rv, ru, rk_ru, h_ru = self.history.pop()
            self.parent[rv] = p_rv
            self.rank[ru] = rk_ru
            self.hub[ru] = h_ru


class Dinic:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.edges = []

    def add_edge(self, u, v, cap):
        self.graph[u].append(len(self.edges))
        self.edges.append([v, cap])
        self.graph[v].append(len(self.edges))
        self.edges.append([u, cap])

    def add_directed_edge(self, u, v, cap):
        self.graph[u].append(len(self.edges))
        self.edges.append([v, cap])
        self.graph[v].append(len(self.edges))
        self.edges.append([u, 0])

    def bfs(self, s, t):
        self.level = [-1] * self.n
        self.level[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for edge_idx in self.graph[u]:
                v, cap = self.edges[edge_idx]
                if cap > 0 and self.level[v] < 0:
                    self.level[v] = self.level[u] + 1
                    q.append(v)
        return self.level[t] >= 0

    def dfs(self, u, t, flow):
        if u == t or flow == 0:
            return flow
        for i in range(self.ptr[u], len(self.graph[u])):
            self.ptr[u] = i
            edge_idx = self.graph[u][i]
            v, cap = self.edges[edge_idx]
            if self.level[v] == self.level[u] + 1 and cap > 0:
                pushed = self.dfs(v, t, min(flow, cap))
                if pushed > 0:
                    self.edges[edge_idx][1] -= pushed
                    self.edges[edge_idx ^ 1][1] += pushed
                    return pushed
        return 0

    def max_flow(self, s, t):
        flow = 0
        while self.bfs(s, t):
            self.ptr = [0] * self.n
            while True:
                pushed = self.dfs(s, t, float('inf'))
                if pushed == 0:
                    break
                flow += pushed
        return flow


def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))
    k = int(next(iterator))
    B = int(next(iterator))

    hubs = [int(next(iterator)) for _ in range(k)]
    edges = []
    adj = [[] for _ in range(n + 1)]
    for i in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        w = int(next(iterator))
        edges.append((u, v, w, i))
        adj[u].append((v, i))
        adj[v].append((u, i))

    dsu = RollbackDSU(n, hubs)
    edge_status = [0] * m  # 0: undecided, 2: cut
    cut_edges = []
    best_solution = None

    def compute_lower_bound():
        # Map current DSU components to nodes
        comp_map = {}
        terminals = []
        for h in hubs:
            root = dsu.find(h)
            if root not in comp_map:
                comp_map[root] = len(comp_map)
            terminals.append(comp_map[root])

        if len(set(terminals)) <= 1:
            return 0

        num_terminals = len(terminals)
        total_cut_lb = 0

        # Build base edges between components
        comp_edges = []
        for u, v, w, idx in edges:
            if edge_status[idx] == 0:
                ru = dsu.find(u)
                rv = dsu.find(v)
                if ru != rv:
                    if ru not in comp_map:
                        comp_map[ru] = len(comp_map)
                    if rv not in comp_map:
                        comp_map[rv] = len(comp_map)
                    comp_edges.append((comp_map[ru], comp_map[rv], w))

        num_comps = len(comp_map)
        sink = num_comps

        for i in range(num_terminals):
            ti = terminals[i]
            dinic = Dinic(num_comps + 1)
            for u_c, v_c, w in comp_edges:
                dinic.add_edge(u_c, v_c, w)
            for j in range(num_terminals):
                if i != j:
                    dinic.add_directed_edge(terminals[j], sink, float('inf'))
            f = dinic.max_flow(ti, sink)
            total_cut_lb += f

        return (total_cut_lb + 1) // 2

    def find_shortest_hub_path():
        min_path = None
        min_len = float('inf')

        for start_hub in hubs:
            start_root = dsu.find(start_hub)
            visited = {start_hub}
            parent = {start_hub: (None, None)}
            queue = deque([start_hub])
            found_hub = None

            while queue:
                u = queue.popleft()
                ru = dsu.find(u)
                if ru != start_root and dsu.hub[ru] != 0:
                    found_hub = u
                    break

                for v, e_idx in adj[u]:
                    if edge_status[e_idx] == 0 or edge_status[e_idx] == 1:
                        if v not in visited:
                            visited.add(v)
                            parent[v] = (u, e_idx)
                            queue.append(v)

            if found_hub is not None:
                path = []
                curr = found_hub
                while parent[curr][0] is not None:
                    p, e_idx = parent[curr]
                    path.append(e_idx)
                    curr = p
                if len(path) < min_len:
                    min_len = len(path)
                    min_path = path

        return min_path

    def search(cost):
        nonlocal best_solution
        if cost > B:
            return False

        path_edges = find_shortest_hub_path()
        if path_edges is None:
            best_solution = [edges[i] for i in cut_edges]
            return True

        lb = compute_lower_bound()
        if cost + lb > B:
            return False

        undecided = [e for e in path_edges if edge_status[e] == 0]
        if not undecided:
            return False

        cp = len(dsu.history)
        for i, e_cut in enumerate(undecided):
            dsu.rollback(cp)
            valid = True
            for j in range(i):
                e_merge = undecided[j]
                u, v, _, _ = edges[e_merge]
                if not dsu.union(u, v):
                    valid = False
                    break
            if not valid:
                break

            edge_status[e_cut] = 2
            cut_edges.append(e_cut)

            if search(cost + edges[e_cut][2]):
                return True

            cut_edges.pop()
            edge_status[e_cut] = 0

        dsu.rollback(cp)
        return False

    if search(0):
        print("YES")
        print(len(best_solution))
        for u, v, w, _ in best_solution:
            print(f"{u} {v}")
    else:
        print("NO")


if __name__ == "__main__":
    main()