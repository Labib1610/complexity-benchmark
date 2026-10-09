from collections import defaultdict

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    k = int(data[0])
    t = int(data[1])
    
    index = 2
    # We'll store for each primary module, its secondary module and allowed tokens
    # Since each primary module is bound to exactly one secondary module,
    # we can represent this as a mapping from primary to (secondary, list of tokens)
    
    primary_to_secondary_tokens = defaultdict(lambda: [None, []])
    
    for _ in range(t):
        x = int(data[index])
        y = int(data[index+1])
        z = int(data[index+2])
        index += 3
        primary_to_secondary_tokens[x][0] = y
        primary_to_secondary_tokens[x][1].append(z)
    
    # If not all primary modules are present, impossible
    if len(primary_to_secondary_tokens) != k:
        print("NO")
        return
    
    # Create a bipartite graph for matching primary modules to access tokens
    # Each primary module has a list of allowed tokens
    # We need a perfect matching where each primary gets one token and all tokens are distinct
    
    # This is a maximum bipartite matching problem
    # Left side: primary modules 1..k
    # Right side: access tokens 1..k
    # Edge exists if token is in allowed list of that primary
    
    # Build adjacency list for graph
    # left node: primary module (1-based to 0-based: i-1)
    # right node: access token (1-based to 0-based: z-1)
    
    adj = [[] for _ in range(k)]
    primaries = sorted(primary_to_secondary_tokens.keys())
    
    primary_index_map = {}
    for idx, p in enumerate(primaries):
        primary_index_map[p] = idx
        
    for p in primaries:
        idx = primary_index_map[p]
        _, tokens = primary_to_secondary_tokens[p]
        for token in tokens:
            adj[idx].append(token - 1)  # Convert to 0-based
            
    # Maximum Bipartite Matching using Hungarian algorithm / DFS approach
    def dfs(u, match_right, match_left, visited):
        for v in adj[u]:
            if visited[v]:
                continue
            visited[v] = True
            
            # If v is unmatched or the mate of v can find another match
            if match_right[v] == -1 or dfs(match_right[v], match_right, match_left, visited):
                match_right[v] = u
                match_left[u] = v
                return True
        return False
    
    # Initialize matches
    match_left = [-1] * k   # match_left[u] = v if u is matched to v
    match_right = [-1] * k  # match_right[v] = u if v is matched to u
    
    result = 0
    for u in range(k):
        visited = [False] * k
        if dfs(u, match_right, match_left, visited):
            result += 1
            
    if result != k:
        print("NO")
        return
        
    print("YES")
    # Output the configurations
    for p in primaries:
        u = primary_index_map[p]
        v = match_left[u]  # 0-based token index
        token = v + 1      # Convert back to 1-based
        secondary = primary_to_secondary_tokens[p][0]
        print(p, secondary, token)

solve()