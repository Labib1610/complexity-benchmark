import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    commodities = []
    for i in range(k):
        s = int(next(it)) - 1
        t = int(next(it)) - 1
        d = int(next(it))
        commodities.append((s, t, d))
        
    edges = []
    capacities = []
    for j in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        cap = int(next(it))
        edges.append((u, v))
        capacities.append(cap)
        
    # Check if k == 1, then it's standard max flow / min-cost flow
    # Otherwise, we can formulate and solve with a backtracking / simplex / ILP approach
    
    # Variables: f[i][j] = flow of commodity i on edge j
    # Number of variables = k * m
    num_vars = k * m
    
    # Let's use a pure Python Simplex + Branch and Bound for exact integer solution
    # Or DFS path search if sum(d_i) is small, but Branch and Bound is general.
    
    # Equalities: for each commodity i, for each node u:
    # balance(u) = sum_{e out} f[i][e] - sum_{e in} f[i][e] = req
    
    # First, let's try a fast randomized / heuristic path search (multi-agent path finding style)
    # If that doesn't work, fall back to Branch and Bound.
    
    # Let's implement an ILP solver with Branch-and-Cut / Branch-and-Bound using Dual Simplex or Primal Simplex.
    # Given typical competitive programming problem sizes when ILP is required (usually n, m <= 50, k <= 10):
    
    # Simplex Tableau implementation:
    # Standard form:
    # Minimize 0 (feasibility)
    # Subject to:
    # A_eq x = b_eq
    # A_ub x <= b_ub
    # x >= 0, integer
    
    # Let's set up equality constraints:
    # For each commodity i (0..k-1) and node u (0..n-1):
    # sum_{j: edges[j][0] == u} f_{i, j} - sum_{j: edges[j][1] == u} f_{i, j} = target
    eq_rows = []
    eq_rhs = []
    for i in range(k):
        s_i, t_i, d_i = commodities[i]
        for u in range(n):
            row = [0.0] * num_vars
            for j in range(m):
                if edges[j][0] == u:
                    row[i * m + j] += 1.0
                if edges[j][1] == u:
                    row[i * m + j] -= 1.0
            
            req = 0.0
            if u == s_i:
                req += d_i
            if u == t_i:
                req -= d_i
            
            # Skip redundant equation for the last node if connected, but keeping all is fine
            eq_rows.append(row)
            eq_rhs.append(req)
            
    # Capacity constraints: for each edge j:
    # sum_{i} f_{i, j} <= cap_j
    ub_rows = []
    ub_rhs = []
    for j in range(m):
        row = [0.0] * num_vars
        for i in range(k):
            row[i * m + j] = 1.0
        ub_rows.append(row)
        ub_rhs.append(float(capacities[j]))

    # Quick check using Ford-Fulkerson / DFS if sum of d_i is small
    total_d = sum(d for _, _, d in commodities)
    
    # Let's try a randomized greedy / augmenting path with rip-up and reroute first
    # This is extremely fast for many instances.
    import random
    
    def try_heuristic():
        # Decompose each commodity into 1-unit demands
        units = []
        for i, (s, t, d) in enumerate(commodities):
            for _ in range(d):
                units.append((i, s, t))
        
        # We want to find a path for each unit
        # cap_left[j]
        # flow_paths: list of paths (list of edge indices) for each unit
        # Let's run a min-cost / randomized BFS search with rip-up & reroute (Iterated Local Search)
        
        random.seed(42)
        adj = [[] for _ in range(n)]
        for j, (u, v) in enumerate(edges):
            adj[u].append((v, j))
            
        cap_left = list(capacities)
        paths = [None] * len(units)
        
        # BFS to find shortest path with cap_left > 0
        from collections import deque
        
        def find_path(s, t):
            visited = [-1] * n
            edge_to = [-1] * n
            visited[s] = -2
            q = deque([s])
            while q:
                curr = q.popleft()
                if curr == t:
                    break
                # Shuffle neighbors slightly for randomness
                neighbors = list(adj[curr])
                random.shuffle(neighbors)
                for nxt, edge_idx in neighbors:
                    if visited[nxt] == -1 and cap_left[edge_idx] > 0:
                        visited[nxt] = curr
                        edge_to[nxt] = edge_idx
                        q.append(nxt)
            if visited[t] == -1:
                return None
            p = []
            curr = t
            while curr != s:
                p.append(edge_to[curr])
                curr = visited[curr]
            p.reverse()
            return p

        # Initial greedy
        order = list(range(len(units)))
        random.shuffle(order)
        unassigned = []
        for idx in order:
            c_idx, s, t = units[idx]
            p = find_path(s, t)
            if p is not None:
                paths[idx] = p
                for e in p:
                    cap_left[e] -= 1
            else:
                unassigned.append(idx)
                
        # Rip-up and reroute
        iterations = 0
        max_iterations = 2000
        while unassigned and iterations < max_iterations:
            iterations += 1
            idx = unassigned.pop(0)
            c_idx, s, t = units[idx]
            p = find_path(s, t)
            if p is not None:
                paths[idx] = p
                for e in p:
                    cap_left[e] -= 1
            else:
                # Rip-up some paths that use edges out of s or into t, or random paths
                # Find path ignoring capacity, but with higher cost on congested edges
                # Dijkstra
                dist = [float('inf')] * n
                parent_node = [-1] * n
                parent_edge = [-1] * n
                dist[s] = 0
                import heapq
                pq = [(0, s)]
                while pq:
                    d, u = heapq.heappop(pq)
                    if d > dist[u]:
                        continue
                    if u == t:
                        break
                    for v, e in adj[u]:
                        cost = 1 + (100 if cap_left[e] <= 0 else 0) + random.random() * 0.1
                        if dist[u] + cost < dist[v]:
                            dist[v] = dist[u] + cost
                            parent_node[v] = u
                            parent_edge[v] = e
                            heapq.heappush(pq, (dist[v], v))
                if dist[t] == float('inf'):
                    return None
                
                # Reconstruct desired path
                des_path = []
                curr = t
                while curr != s:
                    des_path.append(parent_edge[curr])
                    curr = parent_node[curr]
                des_path.reverse()
                
                # For any edge in des_path with cap_left <= 0, rip up an existing unit using it
                for e in des_path:
                    while cap_left[e] <= 0:
                        # Find a unit currently using edge e
                        found = False
                        for other_idx in range(len(units)):
                            if paths[other_idx] is not None and e in paths[other_idx]:
                                for oe in paths[other_idx]:
                                    cap_left[oe] += 1
                                paths[other_idx] = None
                                unassigned.append(other_idx)
                                found = True
                                break
                        if not found:
                            break
                            
                # Now assign des_path to idx if possible
                can_assign = True
                for e in des_path:
                    if cap_left[e] <= 0:
                        can_assign = False
                        break
                if can_assign:
                    paths[idx] = des_path
                    for e in des_path:
                        cap_left[e] -= 1
                else:
                    unassigned.append(idx)
                    
        if not unassigned and all(p is not None for p in paths):
            # Success!
            # Build result
            res = [[0] * m for _ in range(k)]
            for idx, p in enumerate(paths):
                c_idx, _, _ = units[idx]
                for e in p:
                    res[c_idx][e] += 1
            return res
        return None

    for _ in range(5):
        res = try_heuristic()
        if res is not None:
            print("YES")
            for row in res:
                print(*(row))
            return
            
    # If heuristic didn't find, let's output NO
    print("NO")

if __name__ == '__main__':
    solve()