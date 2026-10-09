import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))
    k = int(next(iterator))
    B = int(next(iterator))
    
    terminals = [int(next(iterator)) for _ in range(k)]
    terminals_set = set(terminals)
    
    edges = []
    for i in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        w = int(next(iterator))
        edges.append((u, v, w, i))

    if k <= 1:
        print("YES")
        print(0)
        return

    # Dinic's Algorithm for Min-Cut
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

        def bfs(self, s, t):
            self.level = [-1] * self.n
            self.level[s] = 0
            q = deque([s])
            while q:
                u = q.popleft()
                for edge_idx in self.graph[u]:
                    v, cap, flow = self.edges[edge_idx]
                    if cap - flow > 0 and self.level[v] < 0:
                        self.level[v] = self.level[u] + 1
                        q.append(v)
            return self.level[t] >= 0

        def dfs(self, u, t, pushed):
            if pushed == 0:
                return 0
            if u == t:
                return pushed
            for edge_idx in self.ptr[u]:
                v, cap, flow = self.edges[edge_idx]
                tr = self.level[v] == self.level[u] + 1
                if tr and cap - flow > 0:
                    tr_pushed = self.dfs(v, t, min(pushed, cap - flow))
                    if tr_pushed > 0:
                        self.edges[edge_idx][2] += tr_pushed
                        self.edges[edge_idx ^ 1][2] -= tr_pushed
                        return tr_pushed
            return 0

        def max_flow(self, s, t):
            flow = 0
            while self.bfs(s, t):
                self.ptr = [list(self.graph[i]) for i in range(self.n)]
                while True:
                    pushed = self.dfs(s, t, float('inf'))
                    if pushed == 0:
                        break
                    flow += pushed
            return flow

        def get_reachable(self, s):
            visited = [False] * self.n
            visited[s] = True
            q = deque([s])
            while q:
                u = q.popleft()
                for edge_idx in self.graph[u]:
                    v, cap, flow = self.edges[edge_idx]
                    if cap - flow > 0 and not visited[v]:
                        visited[v] = True
                        q.append(v)
            return visited

    # Try 2-approximation via isolating cuts
    # First, build graph for isolating cuts
    isolating_cuts = []
    isolating_costs = []
    
    # Super-sink node id: n + 1
    super_sink = n + 1
    INF = 10**15

    for i in range(k):
        t_i = terminals[i]
        dinic = Dinic(n + 2)
        for u, v, w, _ in edges:
            dinic.add_edge(u, v, w)
            dinic.add_edge(v, u, w)
        for j in range(k):
            if i != j:
                dinic.add_edge(terminals[j], super_sink, INF)
        
        flow = dinic.max_flow(t_i, super_sink)
        isolating_costs.append(flow)
        reach = dinic.get_reachable(t_i)
        isolating_cuts.append(reach)

    # Initial labeling based on isolating cuts
    best_cost = INF
    best_labels = None

    # Check union of k-1 isolating cuts
    for omit in range(k):
        # Vertex label: which terminal's component does it belong to?
        labels = [0] * (n + 1)
        for i in range(k):
            if i == omit:
                continue
            reach = isolating_cuts[i]
            for v in range(1, n + 1):
                if reach[v]:
                    labels[v] = i + 1
        for v in range(1, n + 1):
            if labels[v] == 0:
                labels[v] = omit + 1
        # Check terminals have their own labels
        valid = True
        for i in range(k):
            if labels[terminals[i]] != i + 1:
                valid = False
                break
        if valid:
            cost = sum(w for u, v, w, _ in edges if labels[u] != labels[v])
            if cost < best_cost:
                best_cost = cost
                best_labels = list(labels)

    # Alpha-expansion to improve
    if best_labels is not None:
        labels = list(best_labels)
        improved = True
        for _ in range(5):
            if not improved:
                break
            improved = False
            for alpha in range(1, k + 1):
                # Build graph for alpha-expansion
                # Node for each vertex v in 1..n
                # Auxiliary nodes for edges between u, v with labels[u] != alpha and labels[v] != alpha and labels[u] != labels[v]
                dinic = Dinic(n + 2 * m + 3)
                source = 0
                sink = n + 2 * m + 2
                aux_id = n + 1
                
                # If label[v] == alpha, it must stay alpha (or cap INF to source)
                for v in range(1, n + 1):
                    if v in terminals_set:
                        t_idx = terminals.index(v) + 1
                        if t_idx == alpha:
                            dinic.add_edge(source, v, INF)
                        else:
                            dinic.add_edge(v, sink, INF)
                    else:
                        if labels[v] == alpha:
                            dinic.add_edge(source, v, INF)
                
                for u, v, w, _ in edges:
                    lu, lv = labels[u], labels[v]
                    if lu == lv:
                        if lu != alpha:
                            # Edge between vertices of same non-alpha label
                            dinic.add_edge(u, v, w)
                            dinic.add_edge(v, u, w)
                    elif lu == alpha:
                        # u is alpha, v is not
                        dinic.add_edge(u, v, w)
                    elif lv == alpha:
                        # v is alpha, u is not
                        dinic.add_edge(v, u, w)
                    else:
                        # lu != alpha, lv != alpha, lu != lv
                        # Introduce aux node
                        a = aux_id
                        aux_id += 1
                        dinic.add_edge(u, a, w)
                        dinic.add_edge(v, a, w)
                        dinic.add_edge(a, sink, w)
                
                dinic.max_flow(source, sink)
                reach = dinic.get_reachable(source)
                
                new_labels = list(labels)
                for v in range(1, n + 1):
                    if reach[v]:
                        new_labels[v] = alpha
                
                new_cost = sum(w for u, v, w, _ in edges if new_labels[u] != new_labels[v])
                if new_cost < best_cost:
                    best_cost = new_cost
                    best_labels = list(new_labels)
                    labels = list(new_labels)
                    improved = True

    if best_cost <= B:
        cut_edges = []
        for u, v, w, _ in edges:
            if best_labels[u] != best_labels[v]:
                cut_edges.append((u, v))
        print("YES")
        print(len(cut_edges))
        for u, v in cut_edges:
            print(f"{u} {v}")
        return

    # If alpha-expansion couldn't reach <= B, run Branch & Bound
    # Lower bound function for a graph state
    class DSU:
        def __init__(self, size):
            self.parent = list(range(size))
        def find(self, i):
            path = []
            while self.parent[i] != i:
                path.append(i)
                i = self.parent[i]
            for p in path:
                self.parent[p] = i
            return i
        def union(self, i, j):
            root_i = self.find(i)
            root_j = self.find(j)
            if root_i != root_j:
                self.parent[root_i] = root_j
                return True
            return False

    # Branch and bound search
    # State: active edge list, current cut cost, cut edges set
    best_sol = [None]
    best_c = [best_cost]

    def get_path(adj, terminals):
        # Find path between any two terminals
        term_map = {t: i for i, t in enumerate(terminals)}
        for start_t in terminals:
            visited = {start_t: None}
            edge_used = {}
            q = deque([start_t])
            while q:
                curr = q.popleft()
                if curr != start_t and curr in term_map:
                    # Found path
                    path_edges = []
                    curr_node = curr
                    while visited[curr_node] is not None:
                        prev_node = visited[curr_node]
                        e_idx = edge_used[curr_node]
                        path_edges.append(e_idx)
                        curr_node = prev_node
                    return path_edges
                for nxt, eid in adj[curr]:
                    if nxt not in visited:
                        visited[nxt] = curr
                        edge_used[nxt] = eid
                        q.append(nxt)
        return None

    def bnb(current_cost, active_edges, cut_edge_indices):
        if current_cost >= best_c[0] or current_cost > B:
            return
        
        # Build adjacency
        adj = [[] for _ in range(n + 1)]
        dsu = DSU(n + 1)
        for eid in active_edges:
            u, v, w, _ = edges[eid]
            adj[u].append((v, eid))
            adj[v].append((u, eid))
            dsu.union(u, v)

        # Check if all terminals separated
        term_roots = [dsu.find(t) for t in terminals]
        if len(set(term_roots)) == k:
            best_c[0] = current_cost
            best_sol[0] = list(cut_edge_indices)
            return

        # Lower bound using isolating cuts on current contracted/active graph
        # Compute min isolating cut sum
        lb = 0
        super_sink = n + 1
        for i in range(k):
            ti = terminals[i]
            dinic = Dinic(n + 2)
            for eid in active_edges:
                u, v, w, _ = edges[eid]
                dinic.add_edge(u, v, w)
                dinic.add_edge(v, u, w)
            for j in range(k):
                if i != j:
                    dinic.add_edge(terminals[j], super_sink, INF)
            lb += dinic.max_flow(ti, super_sink)
        
        lb_cost = (lb + 1) // 2
        if current_cost + lb_cost >= best_c[0] or current_cost + lb_cost > B:
            return

        path_eids = get_path(adj, terminals)
        if not path_eids:
            return

        # Sort path edges by weight descending for pruning efficiency
        path_eids.sort(key=lambda eid: edges[eid][2])

        # Branching: on each edge, cut it or contract it
        # Branch 1: cut e1
        # Branch 2: contract e1, cut e2
        # ...
        contracted = []
        for eid in path_eids:
            u, v, w, _ = edges[eid]
            # Try cutting eid
            rem_active = [e for e in active_edges if e != eid and e not in contracted]
            bnb(current_cost + w, rem_active, cut_edge_indices + [eid])
            if best_c[0] <= B:
                return
            
            # To contract eid, ensure it doesn't merge two terminals
            # Find current components with contracted edges
            temp_dsu = DSU(n + 1)
            for ce in contracted + [eid]:
                temp_dsu.union(edges[ce][0], edges[ce][1])
            t_set = set()
            invalid = False
            for t in terminals:
                r = temp_dsu.find(t)
                if r in t_set:
                    invalid = True
                    break
                t_set.add(r)
            if invalid:
                break
            contracted.append(eid)

    all_edge_indices = list(range(m))
    bnb(0, all_edge_indices, [])

    if best_c[0] <= B and best_sol[0] is not None:
        print("YES")
        print(len(best_sol[0]))
        for eid in best_sol[0]:
            u, v, _, _ = edges[eid]
            print(f"{u} {v}")
    else:
        print("NO")

if __name__ == '__main__':
    solve()