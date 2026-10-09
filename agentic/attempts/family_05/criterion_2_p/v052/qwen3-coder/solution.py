from collections import defaultdict

def solve():
    k, t = map(int, input().split())
    
    configs = []
    captain_cruiser = {}  # captain -> cruiser
    cruiser_captain = {}  # cruiser -> captain
    captain_sectors = defaultdict(lambda: defaultdict(list))  # captain -> sector -> [configs]
    sector_configs = defaultdict(list)  # sector -> [configs]
    
    for _ in range(t):
        c, v, s = map(int, input().split())
        configs.append((c, v, s))
        captain_cruiser[c] = v
        cruiser_captain[v] = c
        captain_sectors[c][s].append((c, v, s))
        sector_configs[s].append((c, v, s))
    
    # Build bipartite graph for matching
    # Left side: captains (or cruisers, since they're 1:1)
    # Right side: sectors
    # Edge exists if there's at least one config with that captain-cruiser pair and that sector
    
    # For each captain-cruiser pair, collect possible sectors
    pair_sectors = defaultdict(list)  # (captain,cruiser) -> [sectors]
    for c, v, s in configs:
        if (c, v) not in pair_sectors:
            pair_sectors[(c, v)] = []
        if s not in pair_sectors[(c, v)]:
            pair_sectors[(c, v)].append(s)
    
    # Create mapping from captain to its cruiser
    pairs = list(pair_sectors.keys())  # list of (captain, cruiser) pairs
    
    # Build graph for maximum bipartite matching
    # Left nodes: 0 to len(pairs)-1 (representing captain-cruiser pairs)
    # Right nodes: 1 to k (sectors)
    graph = defaultdict(list)
    pair_to_idx = {pair: i for i, pair in enumerate(pairs)}
    
    for pair, sectors in pair_sectors.items():
        idx = pair_to_idx[pair]
        for s in sectors:
            graph[idx].append(s)
    
    # Maximum bipartite matching implementation
    def dfs(u, match_right, match_left, visited):
        for v in graph[u]:
            if visited[v]:
                continue
            visited[v] = True
            
            if match_right[v] == -1 or dfs(match_right[v], match_right, match_left, visited):
                match_right[v] = u
                match_left[u] = v
                return True
        return False
    
    # Initialize matching arrays
    match_right = [-1] * (k + 1)  # sector -> pair_idx
    match_left = [-1] * len(pairs)  # pair_idx -> sector
    
    matching = 0
    for u in range(len(pairs)):
        visited = [False] * (k + 1)
        if dfs(u, match_right, match_left, visited):
            matching += 1
    
    if matching < k:
        print("NO")
        return
    
    print("YES")
    
    # Reconstruct solution
    # For each matched pair-sector, find a valid config
    result = []
    used_configs = set()
    
    for pair_idx, sector in enumerate(match_left):
        if sector == -1:
            continue
        pair = pairs[pair_idx]
        c, v = pair
        
        # Find any valid config with this captain, cruiser, sector
        found = False
        for config in configs:
            cc, vv, ss = config
            if cc == c and vv == v and ss == sector:
                result.append(config)
                found = True
                break
    
    for c, v, s in result:
        print(c, v, s)

solve()