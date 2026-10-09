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
    
    terminals = [int(next(it)) for _ in range(k)]
    
    edges = []
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edge_idx = len(edges)
        edges.append((u, v, w))
        adj[u].append((v, w, edge_idx))
        adj[v].append((u, w, edge_idx))
        
    # Check if k <= 1 (already isolated)
    if k <= 1:
        print("YES")
        print(0)
        return

    # Dinic algorithm for min s-t cut / multi-source multi-sink cut
    class Dinic:
        def __init__(self, num_nodes):
            self.n = num_nodes
            self.graph = [[] for _ in range(num_nodes)]
            self.edges = []

        def add_edge(self, u, v, cap, orig_id=-1):
            e1 = [v, cap, 0, len(self.graph[v]), orig_id]
            e2 = [u, 0, 0, len(self.graph[u]), -1]
            self.graph[u].append(e1)
            self.graph[v].append(e2)
            self.edges.append((u, len(self.graph[u]) - 1))

        def bfs(self, s, t):
            self.level = [-1] * self.n
            self.level[s] = 0
            q = deque([s])
            while q:
                v = q.popleft()
                for e in self.graph[v]:
                    nxt, cap, flow = e[0], e[1], e[2]
                    if cap - flow > 0 and self.level[nxt] < 0:
                        self.level[nxt] = self.level[v] + 1
                        q.append(nxt)
            return self.level[t] >= 0

        def dfs(self, v, t, pushed, ptr):
            if pushed == 0 or v == t:
                return pushed
            for cid in range(ptr[v], len(self.graph[v])):
                ptr[v] = cid
                e = self.graph[v][cid]
                nxt, cap, flow = e[0], e[1], e[2]
                tr = e[3]
                if self.level[v] + 1 != self.level[nxt] or cap - flow == 0:
                    continue
                tr_pushed = self.dfs(nxt, t, min(pushed, cap - flow), ptr)
                if tr_pushed == 0:
                    continue
                e[2] += tr_pushed
                self.graph[nxt][tr][2] -= tr_pushed
                return tr_pushed
            return 0

        def max_flow(self, s, t):
            flow = 0
            while self.bfs(s, t):
                ptr = [0] * self.n
                while True:
                    pushed = self.dfs(s, t, float('inf'), ptr)
                    if pushed == 0:
                        break
                    flow += pushed
            return flow

        def min_cut_nodes(self, s):
            visited = [False] * self.n
            q = deque([s])
            visited[s] = True
            while q:
                v = q.popleft()
                for e in self.graph[v]:
                    nxt, cap, flow = e[0], e[1], e[2]
                    if cap - flow > 0 and not visited[nxt]:
                        visited[nxt] = True
                        q.append(nxt)
            return visited

    # Find isolating cuts for each terminal
    def get_isolating_cut(ti, other_terminals):
        src = 0
        dst = n + 1
        dinic = Dinic(n + 2)
        
        dinic.add_edge(src, ti, float('inf'))
        for ot in other_terminals:
            dinic.add_edge(ot, dst, float('inf'))
            
        for u, v, w in edges:
            dinic.add_edge(u, v, w)
            dinic.add_edge(v, u, w)
            
        flow = dinic.max_flow(src, dst)
        in_s = dinic.min_cut_nodes(src)
        
        cut_edges = []
        for u, v, w in edges:
            if in_s[u] != in_s[v]:
                cut_edges.append((u, v, w))
        return flow, in_s, cut_edges

    # Check union of isolating cuts (2-approximation)
    isolating_cuts = []
    union_cut_edges = set()
    total_iso_flow = 0
    
    for i, t in enumerate(terminals):
        others = terminals[:i] + terminals[i+1:]
        flow, in_s, cut_edges = get_isolating_cut(t, others)
        total_iso_flow += flow
        isolating_cuts.append((flow, cut_edges))
        for u, v, w in cut_edges:
            edge_key = (min(u, v), max(u, v))
            union_cut_edges.add(edge_key)

    # Calculate total weight of union cut
    edge_weights = {}
    for u, v, w in edges:
        k_pair = (min(u, v), max(u, v))
        edge_weights[k_pair] = edge_weights.get(k_pair, 0) + w

    total_union_cost = sum(edge_weights[e] for e in union_cut_edges)
    
    if total_union_cost <= B:
        print("YES")
        print(len(union_cut_edges))
        for u, v in union_cut_edges:
            print(f"{u} {v}")
        return

    # If k == 2, the isolating cut is exact
    if k == 2:
        flow, in_s, cut_edges = isolating_cuts[0]
        if flow <= B:
            print("YES")
            print(len(cut_edges))
            for u, v, w in cut_edges:
                print(f"{u} {v}")
        else:
            print("NO")
        return

    # Branch and Bound for Minimum Multiway Cut
    # Vertex-assignment / partitioning branch and bound
    # Pre-check if lower bound > B
    lower_bound = (total_iso_flow + 1) // 2
    if lower_bound > B:
        print("NO")
        return

    # Branch and Bound: assign each node in the graph to one of the k terminal components
    # Map vertices to 0..k-1 (representing terminals)
    best_cost = [B + 1]
    best_assignment = [None]
    
    assignment = [-1] * (n + 1)
    for i, t in enumerate(terminals):
        assignment[t] = i

    # Order vertices to assign: BFS/DFS from terminals
    visited = [False] * (n + 1)
    q = deque()
    for t in terminals:
        visited[t] = True
    for t in terminals:
        for v, w, _ in adj[t]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
    
    order = []
    while q:
        u = q.popleft()
        order.append(u)
        for v, w, _ in adj[u]:
            if not visited[v]:
                visited[v] = True
                q.append(v)
    for i in range(1, n + 1):
        if not visited[i]:
            order.append(i)

    def search(idx, current_cost):
        if current_cost >= best_cost[0]:
            return
        if idx == len(order):
            best_cost[0] = current_cost
            best_assignment[0] = list(assignment)
            return

        u = order[idx]
        
        # Calculate cost for assigning u to each terminal c
        costs = []
        for c in range(k):
            # Cost added if u is assigned to c
            add_cost = 0
            for v, w, _ in adj[u]:
                if assignment[v] != -1 and assignment[v] != c:
                    add_cost += w
            costs.append((add_cost, c))
            
        costs.sort() # Try promising branches first
        
        for add_cost, c in costs:
            if current_cost + add_cost < best_cost[0]:
                assignment[u] = c
                search(idx + 1, current_cost + add_cost)
                assignment[u] = -1

    search(0, 0)
    
    if best_cost[0] <= B and best_assignment[0] is not None:
        assign = best_assignment[0]
        res_edges = []
        for u, v, w in edges:
            if assign[u] != assign[v]:
                res_edges.append((u, v))
        print("YES")
        print(len(res_edges))
        for u, v in res_edges:
            print(f"{u} {v}")
    else:
        print("NO")

if __name__ == '__main__':
    solve()