import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    # Build adjacency structure: adj[x][y] = set of z values for authorized (x, y, z)
    adj = [[set() for _ in range(k + 1)] for _ in range(k + 1)]
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        adj[x][y].add(z)
    
    # Hungarian algorithm for maximum bipartite matching
    def hungarian(n, graph):
        """Returns (max_matching_size, match_U, match_V) where:
        - graph[u] = set of v that u can match to
        - match_U[u] = v matched to u (or 0 if unmatched)
        - match_V[v] = u matched to v (or 0 if unmatched)
        """
        match_U = [0] * (n + 1)
        match_V = [0] * (n + 1)
        
        def dfs(u, seen):
            for v in graph[u]:
                if not seen[v]:
                    seen[v] = True
                    if match_V[v] == 0 or dfs(match_V[v], seen):
                        match_U[u] = v
                        match_V[v] = u
                        return True
            return False
        
        result = 0
        for u in range(1, n + 1):
            seen = [False] * (n + 1)
            if dfs(u, seen):
                result += 1
        return result, match_U, match_V
    
    # Build bipartite graph for (specialist, machine) pairs to time slots
    # Left side: pairs (x, y) encoded as (x-1)*k + y, range 1 to k*k
    # Right side: time slots z, range 1 to k
    pair_graph = [set() for _ in range(k * k + 1)]
    pair_to_config = {}  # Maps (x, y, z) to the original triple
    
    for x in range(1, k + 1):
        for y in range(1, k + 1):
            pair_id = (x - 1) * k + y
            for z in adj[x][y]:
                pair_graph[pair_id].add(z)
                pair_to_config[(x, y, z)] = (x, y, z)
    
    # Find maximum matching from pairs to time slots
    max_match, match_pair, match_z = hungarian(k * k, pair_graph)
    
    if max_match < k:
        print("NO")
        return
    
    # Extract k matched pairs
    matched_pairs = []
    for pair_id in range(1, k * k + 1):
        if match_pair[pair_id] != 0:
            x = (pair_id - 1) // k + 1
            y = (pair_id - 1) % k + 1
            z = match_pair[pair_id]
            matched_pairs.append((x, y, z))
    
    # Now we need to select k pairs such that each specialist and machine appears exactly once
    # Build bipartite graph: specialists (1..k) to machines (1..k)
    # Edge exists if (s, m, z) is in matched_pairs for some z
    
    spec_to_machines = [set() for _ in range(k + 1)]
    config_by_pair = {}  # (x, y) -> (x, y, z)
    
    for x, y, z in matched_pairs:
        spec_to_machines[x].add(y)
        config_by_pair[(x, y)] = (x, y, z)
    
    # Find perfect matching between specialists and machines
    match_spec, match_spec_U, match_mach_V = hungarian(k, spec_to_machines)
    
    if match_spec < k:
        print("NO")
        return
    
    print("YES")
    for s in range(1, k + 1):
        m = match_spec_U[s]
        config = config_by_pair[(s, m)]
        print(f"{config[0]} {config[1]} {config[2]}")

if __name__ == "__main__":
    solve()