import sys
import random
import time

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
    term_set = set(terminals)
    
    edges = []
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        w = int(next(it))
        edges.append((u, v, w))
        
    start_time = time.time()
    
    # Dinic's Algorithm implementation
    def min_st_cut(adj, cap, s, t, num_nodes):
        # adj is list of (to, rev_idx, orig_edge_idx)
        # cap is current residual capacity
        # returns cut_weight, cut_edges (set of orig_edge_idx)
        
        while True:
            level = [-1] * num_nodes
            level[s] = 0
            queue = [s]
            head = 0
            while head < len(queue):
                u = queue[head]
                head += 1
                for to, rev_idx, edge_id in adj[u]:
                    if cap[u][rev_idx ^ 1 if False else None] # wait, cap structure
                    pass
            break
        pass

    # Better Dinic with flat arrays
    # Edge list: to, cap, flow, rev, orig_id
    class Dinic:
        def __init__(self, n):
            self.n = n
            self.graph = [[] for _ in range(n)]
            
        def add_edge(self, u, v, c, orig_id):
            e1 = [v, c, 0, len(self.graph[v]), orig_id]
            e2 = [u, c, 0, len(self.graph[u]), orig_id] # undirected in original, so capacity c both ways
            self.graph[u].append(e1)
            self.graph[v].append(e2)
            
        def max_flow(self, s, t):
            flow = 0
            while True:
                level = [-1] * self.n
                level[s] = 0
                q = [s]
                head = 0
                while head < len(q):
                    u = q[head]
                    head += 1
                    for e in self.graph[u]:
                        v, c, f, rev, _ = e
                        if c - f > 0 and level[v] < 0:
                            level[v] = level[u] + 1
                            q.append(v)
                if level[t] < 0:
                    break
                
                ptr = [0] * self.n
                def dfs(u, pushed):
                    if pushed == 0 or u == t:
                        return pushed
                    for i in range(ptr[u], len(self.graph[u])):
                        ptr[u] = i
                        e = self.graph[u][i]
                        v, c, f, rev, _ = e
                        if level[v] != level[u] + 1 or c - f <= 0:
                            continue
                        tr = dfs(v, min(pushed, c - f))
                        if tr == 0:
                            continue
                        e[2] += tr
                        self.graph[v][rev][2] -= tr
                        return tr
                    return 0
                
                while True:
                    pushed = dfs(s, float('inf'))
                    if pushed == 0:
                        break
                    flow += pushed
            
            # Find reachable from s in residual graph
            visited = [False] * self.n
            visited[s] = True
            q = [s]
            head = 0
            while head < len(q):
                u = q[head]
                head += 1
                for e in self.graph[u]:
                    v, c, f, rev, _ = e
                    if c - f > 0 and not visited[v]:
                        visited[v] = True
                        q.append(v)
            return flow, visited

    def evaluate_cut(cut_edge_indices):
        # Clean up cut: remove redundant edges
        # DSU to check connectivity of terminals
        parent = list(range(n + 1))
        def find(i):
            path = []
            while parent[i] != i:
                path.append(i)
                i = parent[i]
            for node in path:
                parent[node] = i
            return i
        
        def union(i, j):
            root_i = find(i)
            root_j = find(j)
            if root_i != root_j:
                parent[root_i] = root_j
                return True
            return False

        # First build DSU without cut edges
        cut_set = set(cut_edge_indices)
        for i, (u, v, w) in enumerate(edges):
            if i not in cut_set:
                union(u, v)
                
        # Greedily add back cut edges if they don't merge two terminal components
        # Sort cut edges by weight descending to keep heavier edges if possible
        sorted_cut = sorted(list(cut_set), key=lambda idx: edges[idx][2], reverse=True)
        final_cut = []
        
        for idx in sorted_cut:
            u, v, w = edges[idx]
            ru = find(u)
            rv = find(v)
            if ru == rv:
                # Already connected, don't need to cut
                continue
            
            # Check if union(ru, rv) would connect any two terminals
            # Collect which terminals are in ru and rv
            # To do this efficiently, find root of each terminal
            term_roots = {t: find(t) for t in terminals}
            roots_in_u = [t for t, r in term_roots.items() if r == ru]
            roots_in_v = [t for t, r in term_roots.items() if r == rv]
            
            if len(roots_in_u) > 0 and len(roots_in_v) > 0:
                # Cannot merge, must keep in cut
                final_cut.append(idx)
            else:
                # Can safely add this edge back
                union(u, v)
                
        total_cost = sum(edges[idx][2] for idx in final_cut)
        return total_cost, final_cut

    # Sequential min-cut heuristic
    def run_sequential(perm):
        # We sequentially separate perm[i] from remaining terminals
        current_edges = list(range(m))
        removed_edges = set()
        
        for i in range(len(perm) - 1):
            source = perm[i]
            sink_terms = perm[i+1:]
            
            # Build graph with current active edges
            # Super sink node = 0 (1-indexed nodes 1..n, so 0 is free)
            super_sink = 0
            dinic = Dinic(n + 1)
            for idx in current_edges:
                if idx in removed_edges:
                    continue
                u, v, w = edges[idx]
                dinic.add_edge(u, v, w, idx)
                
            inf_cap = 10**15
            for st in sink_terms:
                dinic.add_edge(st, super_sink, inf_cap, -1)
                
            flow, visited = dinic.max_flow(source, super_sink)
            
            # Cut edges are those with visited[u] != visited[v]
            for idx in current_edges:
                if idx in removed_edges:
                    continue
                u, v, w = edges[idx]
                if visited[u] != visited[v]:
                    removed_edges.add(idx)
                    
        return evaluate_cut(removed_edges)

    # Isolating cuts heuristic
    def run_isolating():
        # For each terminal, isolate from all others
        cuts = []
        for i, t in enumerate(terminals):
            super_sink = 0
            dinic = Dinic(n + 1)
            for idx, (u, v, w) in enumerate(edges):
                dinic.add_edge(u, v, w, idx)
            for other_t in terminals:
                if other_t != t:
                    dinic.add_edge(other_t, super_sink, 10**15, -1)
            flow, visited = dinic.max_flow(t, super_sink)
            cut = set()
            for idx, (u, v, w) in enumerate(edges):
                if visited[u] != visited[v]:
                    cut.add(idx)
            cuts.append((flow, cut))
            
        # Union of best k-1 cuts
        cuts.sort(key=lambda x: x[0])
        combined_cut = set()
        for i in range(len(terminals) - 1):
            combined_cut.update(cuts[i][1])
            
        return evaluate_cut(combined_cut)

    best_cost = float('inf')
    best_cut = []

    # Try isolating cuts first
    cost, cut = run_isolating()
    if cost < best_cost:
        best_cost = cost
        best_cut = cut

    # Try sequential cuts with various permutations
    base_perm = list(terminals)
    perms = [base_perm]
    
    # Add reverse
    perms.append(base_perm[::-1])
    
    # Try random permutations
    random.seed(42)
    for _ in range(50):
        p = list(terminals)
        random.shuffle(p)
        perms.append(p)

    for p in perms:
        if best_cost <= B:
            break
        if time.time() - start_time > 4.2:
            break
        cost, cut = run_sequential(p)
        if cost < best_cost:
            best_cost = cost
            best_cut = cut

    if best_cost <= B:
        print("YES")
        print(len(best_cut))
        for idx in best_cut:
            u, v, _ = edges[idx]
            print(f"{u} {v}")
    else:
        print("NO")

if __name__ == '__main__':
    solve()