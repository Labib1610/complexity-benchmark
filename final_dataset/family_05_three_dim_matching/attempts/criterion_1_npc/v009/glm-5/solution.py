import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    k = int(data[0])
    t = int(data[1])
    idx = 2
    allowed = []
    for _ in range(t):
        x = int(data[idx]); y = int(data[idx+1]); z = int(data[idx+2])
        idx += 3
        allowed.append((x, y, z))
    
    # For each (x, y), collect list of z's
    xy_to_z = {}
    for (x, y, z) in allowed:
        key = (x, y)
        if key not in xy_to_z:
            xy_to_z[key] = []
        xy_to_z[key].append(z)
    
    # We need to select k pairs (x, y) such that x's are a permutation and y's are a permutation,
    # and then assign z's as a permutation where each selected (x,y) has z available.
    
    # Enumerate all perfect matchings between X and Y using allowed (x,y) pairs.
    # Then check if z assignment is possible.
    
    # Build adjacency for X-Y bipartite graph
    adj = [[] for _ in range(k+1)]
    xy_pairs = []
    for (x, y, z) in allowed:
        adj[x].append(y)
    for x in range(1, k+1):
        adj[x] = sorted(set(adj[x]))
    
    # Find all perfect matchings in X-Y bipartite graph
    # Using recursive backtracking
    
    matchings = []
    match_y = [0] * (k+1)  # which x is matched to y
    match_x = [0] * (k+1)  # which y is matched to x
    used_y = [False] * (k+1)
    
    def find_matchings(x):
        if x > k:
            # Found a perfect matching
            matching = [(i, match_x[i]) for i in range(1, k+1)]
            matchings.append(matching)
            return
        for y in adj[x]:
            if not used_y[y]:
                used_y[y] = True
                match_x[x] = y
                match_y[y] = x
                find_matchings(x + 1)
                used_y[y] = False
                match_x[x] = 0
                match_y[y] = 0
                if len(matchings) > 0:
                    return  # We only need one valid solution
        return
    
    find_matchings(1)
    
    if not matchings:
        print("NO")
        return
    
    # For each matching, try to assign z's
    # We have k pairs (x, y), each with a set of available z's
    # Need to find a perfect matching in the bipartite graph between pairs and Z
    
    for matching in matchings:
        # Build bipartite graph: pair index -> z's
        pair_z = []
        for (x, y) in matching:
            zs = xy_to_z.get((x, y), [])
            pair_z.append(zs)
        
        # Try to find perfect matching using Hungarian algorithm / augmenting paths
        # pair index 0..k-1, z 1..k
        match_pair = [-1] * k  # which z is matched to pair i
        match_z = [0] * (k+1)  # which pair is matched to z
        
        def try_kuhn(pair, visited):
            for z in pair_z[pair]:
                if not visited[z]:
                    visited[z] = True
                    if match_z[z] == -1 or match_z[z] == 0:
                        match_z[z] = pair
                        match_pair[pair] = z
                        return True
                    else:
                        if try_kuhn(match_z[z], visited):
                            match_pair[pair] = z
                            return True
            return False
        
        # Initialize match_z to -1 (unmatched)
        for i in range(k+1):
            match_z[i] = -1
        match_z[0] = -1  # placeholder
        
        success = True
        for pair in range(k):
            visited = [False] * (k+1)
            if not try_kuhn(pair, visited):
                success = False
                break
        
        if success:
            print("YES")
            for pair in range(k):
                x, y = matching[pair]
                z = match_pair[pair]
                print(f"{x} {y} {z}")
            return
    
    print("NO")

solve()