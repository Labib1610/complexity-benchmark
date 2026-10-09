import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    # Read all allowed triples
    triples = []
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        triples.append((x, y, z))
    
    # Build bipartite graph between X and Y
    # For each (x, y), store list of z values
    xy_to_z = {}
    for x, y, z in triples:
        key = (x, y)
        if key not in xy_to_z:
            xy_to_z[key] = []
        xy_to_z[key].append(z)
    
    # Build adjacency list for X -> Y
    adj = [[] for _ in range(k + 1)]
    for (x, y) in xy_to_z:
        adj[x].append(y)
    
    # Find maximum matching from X to Y
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
        dfs(x, visited)
    
    # Check if we have perfect matching
    matched_count = sum(1 for y in range(1, k + 1) if match_y[y] != 0)
    if matched_count != k:
        print("NO")
        return
    
    # Build reverse mapping
    match_x = [0] * (k + 1)
    for y in range(1, k + 1):
        if match_y[y] != 0:
            match_x[match_y[y]] = y
    
    # Now we need to assign z values
    # For each x, we have matched y = match_x[x]
    # We need to choose z such that (x, y, z) is valid and all z's are distinct
    
    # Build graph: for each x, list of available z values
    x_to_z_options = [[] for _ in range(k + 1)]
    for x in range(1, k + 1):
        y = match_x[x]
        if (x, y) in xy_to_z:
            x_to_z_options[x] = xy_to_z[(x, y)][:]  # copy
    
    # Check if any x has no z options
    for x in range(1, k + 1):
        if not x_to_z_options[x]:
            print("NO")
            return
    
    # Bipartite matching from X to Z
    match_z = [0] * (k + 1)
    
    def dfs_z(x, visited):
        for z in x_to_z_options[x]:
            if visited[z]:
                continue
            visited[z] = True
            if match_z[z] == 0 or dfs_z(match_z[z], visited):
                match_z[z] = x
                return True
        return False
    
    for x in range(1, k + 1):
        visited = [False] * (k + 1)
        if not dfs_z(x, visited):
            print("NO")
            return
    
    # Build result
    result = []
    for z in range(1, k + 1):
        x = match_z[z]
        y = match_x[x]
        result.append((x, y, z))
    
    print("YES")
    for x, y, z in result:
        print(x, y, z)

solve()