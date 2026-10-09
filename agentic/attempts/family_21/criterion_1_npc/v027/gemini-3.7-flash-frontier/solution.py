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
    
    anchors = [int(next(it)) for _ in range(k)]
    
    original_edges = []
    adj_matrix = {}
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        if u == v:
            continue
        if u > v:
            u, v = v, u
        original_edges.append((u, v, w))
        adj_matrix[(u, v)] = adj_matrix.get((u, v), 0) + w

    if k <= 1:
        print("YES")
        print(0)
        return

    # Dinic's Algorithm for min s-t cut
    class Dinic:
        def __init__(self, num_nodes):
            self.n = num_nodes
            self.graph = [[] for _ in range(num_nodes)]
            self.edges = []
            
        def add_edge(self, u, v, cap):
            self.graph[u].append(len(self.edges))
            self.edges.append([v, cap, 0])
            self.graph[v].append(len(self.edges))
            self.edges.append([u, cap, 0])  # undirected graph

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
            if pushed == 0 or u == t:
                return pushed
            for idx in range(self.ptr[u], len(self.graph[u])):
                self.ptr[u] = idx
                edge_idx = self.graph[u][idx]
                v, cap, flow = self.edges[edge_idx]
                if self.level[u] + 1 != self.level[v] or cap - flow <= 0:
                    continue
                tr = self.dfs(v, t, min(pushed, cap - flow))
                if tr == 0:
                    continue
                self.edges[edge_idx][2] += tr
                self.edges[edge_idx ^ 1][2] -= tr
                return tr
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

        def get_cut(self, s):
            visited = [False] * self.n
            q = deque([s])
            visited[s] = True
            while q:
                u = q.popleft()
                for edge_idx in self.graph[u]:
                    v, cap, flow = self.edges[edge_idx]
                    if cap - flow > 0 and not visited[v]:
                        visited[v] = True
                        q.append(v)
            return visited

    # Find the isolating cuts for each terminal
    def get_isolating_cut(t_idx, terminal_assignment, current_graph):
        source = anchors[t_idx]
        sink = n + 1
        dinic = Dinic(n + 2)
        
        for (u, v), cap in current_graph.items():
            dinic.add_edge(u, v, cap)
            
        for i, a in enumerate(anchors):
            if i != t_idx:
                dinic.add_edge(a, sink, float('inf'))
                
        for v, t in terminal_assignment.items():
            if t == t_idx:
                dinic.add_edge(source, v, float('inf'))
            elif t is not None:
                dinic.add_edge(v, sink, float('inf'))
                
        flow = dinic.max_flow(source, sink)
        cut = dinic.get_cut(source)
        return flow, cut

    best_cost = float('inf')
    best_assignment = None

    # Initial upper bound using isolating cuts approximation
    cuts_info = []
    total_iso_flow = 0
    for i in range(k):
        f, cut = get_isolating_cut(i, {}, adj_matrix)
        cuts_info.append((f, cut, i))
        total_iso_flow += f

    cuts_info.sort(key=lambda x: x[0])
    
    # Assign components based on isolating cuts
    approx_assignment = {}
    for node in range(1, n + 1):
        assigned = False
        for f, cut, term_idx in cuts_info[:-1]:
            if cut[node]:
                approx_assignment[node] = term_idx
                assigned = True
                break
        if not assigned:
            approx_assignment[node] = cuts_info[-1][2]

    def eval_cost(assignment):
        cost = 0
        for (u, v), cap in adj_matrix.items():
            if assignment.get(u, u) != assignment.get(v, v):
                cost += cap
        return cost

    best_cost = eval_cost(approx_assignment)
    best_assignment = approx_assignment

    # Branch and bound to find exact minimum multiway cut
    assignment = {a: i for i, a in enumerate(anchors)}
    unassigned = [v for v in range(1, n + 1) if v not in assignment]
    
    # Sort unassigned by degree / connectivity to terminals
    def get_priority(v):
        return sum(adj_matrix.get((min(v, a), max(v, a)), 0) for a in anchors)
    unassigned.sort(key=get_priority, reverse=True)

    def lower_bound(curr_assignment):
        flows = []
        for i in range(k):
            f, _ = get_isolating_cut(i, curr_assignment, adj_matrix)
            flows.append(f)
        return max(max(flows), (sum(flows) + 1) // 2)

    def search(idx, curr_assignment):
        nonlocal best_cost, best_assignment
        if idx == len(unassigned):
            cost = eval_cost(curr_assignment)
            if cost < best_cost:
                best_cost = cost
                best_assignment = dict(curr_assignment)
            return

        lb = lower_bound(curr_assignment)
        if lb >= best_cost:
            return

        v = unassigned[idx]
        
        # Order branches by affinity to each terminal
        affinities = []
        for t_idx in range(k):
            aff = 0
            for u, t in curr_assignment.items():
                if t == t_idx:
                    aff += adj_matrix.get((min(u, v), max(u, v)), 0)
            affinities.append((aff, t_idx))
        affinities.sort(key=lambda x: x[0], reverse=True)

        for _, t_idx in affinities:
            curr_assignment[v] = t_idx
            search(idx + 1, curr_assignment)
            del curr_assignment[v]

    if best_cost > B:
        search(0, assignment)

    if best_cost <= B:
        print("YES")
        cut_edges = []
        for (u, v, w) in original_edges:
            if best_assignment[u] != best_assignment[v]:
                cut_edges.append((u, v))
        print(len(cut_edges))
        for u, v in cut_edges:
            print(f"{u} {v}")
    else:
        print("NO")

if __name__ == '__main__':
    solve()