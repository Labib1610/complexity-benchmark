import sys
sys.setrecursionlimit(1000000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    pathways = []
    for _ in range(t):
        m = int(next(it))
        c = int(next(it))
        f = int(next(it))
        pathways.append((m, c, f))
    
    # Build adjacency list: for each (m, c) pair, list of f values
    # We'll use a dictionary keyed by (m, c)
    from collections import defaultdict
    mc_to_f = defaultdict(list)
    for idx, (m, c, f) in enumerate(pathways):
        mc_to_f[(m, c)].append(f)
    
    # We need to select exactly one pathway for each m and each c
    # This is a bipartite matching problem between m (left) and c (right)
    # with the additional constraint that all f values must be distinct
    
    # First, find all valid (m, c) pairs (those that have at least one pathway)
    valid_mc = [(m, c) for (m, c) in mc_to_f.keys()]
    
    # Build bipartite graph for matching
    adj = defaultdict(list)
    for m, c in valid_mc:
        adj[m].append(c)
    
    # Try to find a perfect matching
    match_c = [0] * (k + 1)  # match_c[c] = m that c is matched to
    match_m = [0] * (k + 1)  # match_m[m] = c that m is matched to
    
    def dfs(m, visited):
        for c in adj[m]:
            if visited[c]:
                continue
            visited[c] = True
            if match_c[c] == 0 or dfs(match_c[c], visited):
                match_c[c] = m
                match_m[m] = c
                return True
        return False
    
    # Find matching
    for m in range(1, k + 1):
        visited = [False] * (k + 1)
        dfs(m, visited)
    
    # Check if perfect matching exists
    matched_pairs = []
    for c in range(1, k + 1):
        if match_c[c] != 0:
            matched_pairs.append((match_c[c], c))
    
    if len(matched_pairs) != k:
        print("NO")
        return
    
    # Now we have k matched (m, c) pairs
    # We need to assign f values such that all f values are distinct (1 to k)
    # For each matched pair (m, c), we have a list of available f values
    
    # Build the assignment problem: match pairs to f values
    # Each pair (m, c) can use any f in mc_to_f[(m, c)]
    
    # Create list of pairs in order
    pairs = [(match_c[c], c) for c in range(1, k + 1) if match_c[c] != 0]
    
    # Build bipartite graph for f assignment
    # Left side: pair indices (0 to k-1)
    # Right side: f values (1 to k)
    
    adj_f = [[] for _ in range(k)]
    for i, (m, c) in enumerate(pairs):
        for f in mc_to_f[(m, c)]:
            adj_f[i].append(f)
    
    match_f = [0] * (k + 1)  # match_f[f] = pair index
    match_pair = [0] * k     # match_pair[i] = f value
    
    def dfs_f(pair_idx, visited):
        for f in adj_f[pair_idx]:
            if visited[f]:
                continue
            visited[f] = True
            if match_f[f] == 0 or dfs_f(match_f[f], visited):
                match_f[f] = pair_idx
                match_pair[pair_idx] = f
                return True
        return False
    
    for i in range(k):
        visited = [False] * (k + 1)
        dfs_f(i, visited)
    
    # Check if all pairs got assigned
    for i in range(k):
        if match_pair[i] == 0:
            print("NO")
            return
    
    # Output result
    print("YES")
    for i, (m, c) in enumerate(pairs):
        f = match_pair[i]
        print(f"{m} {c} {f}")

solve()