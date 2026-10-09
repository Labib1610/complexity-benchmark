import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    configs = []
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        configs.append((x, y, z))
    
    # We need to select exactly k configurations such that:
    # sum of 2^x_i = sum of 2^y_i = sum of 2^z_i = B_k = sum_{j=1}^{k} 2^j
    # This means each of x, y, z values must be a permutation of {1, 2, ..., k}
    
    # Build adjacency list for bipartite matching between x-values and y-values
    # For each x-value, find all y-values that share at least one configuration
    
    # Group configurations by (x, y)
    xy_to_z = {}
    for x, y, z in configs:
        key = (x, y)
        if key not in xy_to_z:
            xy_to_z[key] = set()
        xy_to_z[key].add(z)
    
    # Build bipartite graph between x-values (left) and y-values (right)
    adj = [[] for _ in range(k + 1)]
    for x, y in xy_to_z:
        adj[x].append(y)
    
    # Find maximum matching using Hungarian algorithm
    match_y = [0] * (k + 1)
    
    def dfs(x, visited):
        for y in adj[x]:
            if visited[y]:
                continue
            visited[y] = True
            if match_y[y] == 0 or dfs(match_y[y], visited):
                match_y[y] = x
                return True
        return False
    
    for x in range(1, k + 1):
        visited = [False] * (k + 1)
        if not dfs(x, visited):
            print("NO")
            return
    
    # We have a perfect matching between x and y
    # Now check if we can assign z values to form a valid permutation
    
    # Build the matching pairs
    xy_pairs = []
    for y in range(1, k + 1):
        x = match_y[y]
        xy_pairs.append((x, y))
    
    # For each (x, y) pair, we need to pick a z such that z forms a permutation
    # This is another bipartite matching problem
    
    # Build adjacency for z assignment
    adj_z = [[] for _ in range(k + 1)]
    z_values_for_pair = [set() for _ in range(k + 1)]
    
    for i, (x, y) in enumerate(xy_pairs):
        z_set = xy_to_z.get((x, y), set())
        z_values_for_pair[i + 1] = z_set
        for z in z_set:
            adj_z[i + 1].append(z)
    
    # Find matching for z values
    match_z = [0] * (k + 1)
    
    def dfs_z(pair_idx, visited):
        for z in adj_z[pair_idx]:
            if visited[z]:
                continue
            visited[z] = True
            if match_z[z] == 0 or dfs_z(match_z[z], visited):
                match_z[z] = pair_idx
                return True
        return False
    
    for pair_idx in range(1, k + 1):
        visited = [False] * (k + 1)
        if not dfs_z(pair_idx, visited):
            print("NO")
            return
    
    # Build the result
    result = []
    for y in range(1, k + 1):
        x = match_y[y]
        pair_idx = y  # pair_idx corresponds to position in xy_pairs (1-indexed by y)
        z = 0
        for zz in range(1, k + 1):
            if match_z[zz] == pair_idx:
                z = zz
                break
        result.append((x, y, z))
    
    print("YES")
    for x, y, z in result:
        print(x, y, z)

solve()