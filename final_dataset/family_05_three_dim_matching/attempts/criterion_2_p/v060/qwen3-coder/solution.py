from collections import defaultdict

def solve():
    k, t = map(int, input().split())
    
    # Since each satellite is permanently in one orbital slot,
    # and no two satellites share a slot, we can think of this
    # as a bipartite matching problem between satellites (or slots)
    # and frequencies.
    
    # Create adjacency list for satellite -> list of possible frequencies
    adj = defaultdict(list)
    
    # Also store all viable setups for later use
    setups = []
    
    for _ in range(t):
        x, y, z = map(int, input().split())
        adj[x].append(z)
        setups.append((x, y, z))
    
    # We need to match each satellite to a unique frequency
    # This is a maximum bipartite matching problem
    
    # Build graph for bipartite matching
    # Left side: satellites (1 to k)
    # Right side: frequencies (1 to k)
    
    match_satellite = [0] * (k + 1)  # which frequency is matched to satellite i
    match_frequency = [0] * (k + 1)  # which satellite is matched to frequency j
    
    def dfs(u, visited):
        for v in adj[u]:
            if visited[v]:
                continue
            visited[v] = True
            
            # If frequency v is unmatched or we can find augmenting path
            if match_frequency[v] == 0 or dfs(match_frequency[v], visited):
                match_frequency[v] = u
                match_satellite[u] = v
                return True
        return False
    
    # Try to match all satellites
    matching = 0
    for u in range(1, k + 1):
        visited = [False] * (k + 1)
        if dfs(u, visited):
            matching += 1
    
    if matching < k:
        print("NO")
        return
    
    print("YES")
    # Reconstruct the solution
    # For each satellite, we know its slot (from the input invariant)
    # and its assigned frequency (from match_satellite)
    
    # Create mapping from satellite to slot
    sat_to_slot = {}
    for x, y, z in setups:
        sat_to_slot[x] = y
    
    for satellite in range(1, k + 1):
        frequency = match_satellite[satellite]
        slot = sat_to_slot[satellite]
        print(satellite, slot, frequency)

solve()