from collections import defaultdict, deque
import sys

def solve():
    n, m, k = map(int, input().split())
    
    species = []
    for i in range(k):
        s, t, d = map(int, input().split())
        species.append((s, t, d))
    
    edges = []
    edge_index = {}
    adj = defaultdict(list)
    for i in range(m):
        u, v, cap = map(int, input().split())
        edges.append((u, v, cap))
        edge_index[(u, v)] = i
        adj[u].append((v, i))
    
    # For each species, find all possible paths from source to target
    # We'll use a flow approach, but since we need integer flows and small graphs,
    # we can model this as an integer linear program or use a multi-commodity flow approach.
    
    # Let's model this as a feasibility problem with integer constraints.
    # Variables: f[i][j] = flow of species i on edge j
    # Constraints:
    # 1. Flow conservation for each species at each node
    # 2. Capacity constraints on edges (sum over all species <= cap)
    # 3. Demand constraints (total flow out of source = demand, into sink = demand)
    
    # We'll use a brute-force approach for small instances, but since constraints
    # might be large, we need a more systematic approach.
    
    # Let's build a system of equations and inequalities.
    # This is essentially a multi-commodity flow problem with integer flows.
    
    # For small k and m, we can try to enumerate flows, but that's not efficient.
    # Instead, we'll model this as an integer linear program and solve it.
    
    # Since we cannot use external libraries, we'll implement a custom solution.
    
    # Let's try a different approach: for each species, we find a set of paths,
    # then determine how much flow to send on each path such that:
    # 1. Total demand is satisfied
    # 2. Edge capacities are not exceeded
    
    # Find all simple paths for each species (assuming small graphs)
    def find_paths(src, dst, max_len=10):
        paths = []
        visited = [False] * (n + 1)
        
        def dfs(u, path, length):
            if length > max_len:
                return
            if u == dst:
                paths.append(path[:])
                return
            visited[u] = True
            for v, edge_id in adj[u]:
                if not visited[v]:
                    path.append(edge_id)
                    dfs(v, path, length + 1)
                    path.pop()
            visited[u] = False
            
        dfs(src, [], 0)
        return paths
    
    # For each species, find paths
    species_paths = []
    for s, t, d in species:
        paths = find_paths(s, t)
        species_paths.append(paths)
    
    # Now we need to assign flows to paths such that:
    # 1. For each species, sum of flows on its paths = demand
    # 2. For each edge, sum of flows (over all species and their paths using the edge) <= capacity
    
    # This is an integer programming problem. We'll try a backtracking approach.
    
    # Let's define variables: for each species and each of its paths, how much flow to send.
    # We'll iterate through species and try all possible flow assignments.
    
    def backtrack(species_idx, edge_flows):
        if species_idx == k:
            # Check if all edge capacities are satisfied
            for i in range(m):
                if edge_flows[i] > edges[i][2]:
                    return None
            return []
        
        s, t, d = species
        paths = species_paths[species_idx]
        
        # Try all ways to distribute d units among paths
        # This is equivalent to finding all compositions of d into len(paths) non-negative parts
        def generate_compositions(remaining, num_paths, current):
            if num_paths == 1:
                yield current + [remaining]
                return
            for i in range(remaining + 1):
                yield from generate_compositions(remaining - i, num_paths - 1, current + [i])
        
        for composition in generate_compositions(d, len(paths), []):
            # Calculate edge flows for this composition
            temp_edge_flows = edge_flows[:]
            valid = True
            
            for path_idx, flow in enumerate(composition):
                if flow == 0:
                    continue
                path = paths[path_idx]
                for edge_id in path:
                    temp_edge_flows[edge_id] += flow
                    if temp_edge_flows[edge_id] > edges[edge_id][2]:
                        valid = False
                        break
                if not valid:
                    break
            
            if valid:
                result = backtrack(species_idx + 1, temp_edge_flows)
                if result is not None:
                    return [composition] + result
        
        return None
    
    # Start backtracking
    edge_flows = [0] * m
    solution = backtrack(0, edge_flows)
    
    if solution is None:
        print("NO")
        return
    
    print("YES")
    # Reconstruct the output format
    for i in range(k):
        composition = solution[i]
        paths = species_paths[i]
        
        # For each edge, sum up flows from all paths that use it
        edge_usage = [0] * m
        for path_idx, flow in enumerate(composition):
            if flow == 0:
                continue
            path = paths[path_idx]
            for edge_id in path:
                edge_usage[edge_id] += flow
        
        print(' '.join(map(str, edge_usage)))

solve()