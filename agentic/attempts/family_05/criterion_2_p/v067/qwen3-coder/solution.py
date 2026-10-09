from collections import defaultdict

def solve():
    k, t = map(int, input().split())
    
    if t < k:
        print("NO")
        return
    
    configs = []
    drone_to_station = {}
    station_to_drone = {}
    
    for _ in range(t):
        d, c, f = map(int, input().split())
        configs.append((d, c, f))
        
        # Verify the constraint: each drone connects to exactly one station
        if d in drone_to_station:
            if drone_to_station[d] != c:
                # This shouldn't happen according to problem statement
                print("NO")
                return
        else:
            drone_to_station[d] = c
            
        if c in station_to_drone:
            if station_to_drone[c] != d:
                # This shouldn't happen according to problem statement
                print("NO")
                return
        else:
            station_to_drone[c] = d
    
    # Build a graph where each configuration is an edge
    # We want a perfect matching that covers all drones/stations/frequencies
    # Since each drone is associated with exactly one station, we can think of this as:
    # For each drone d (and its station s), we need to pick exactly one frequency
    
    # Group configurations by (drone, station) pair
    ds_to_freqs = defaultdict(list)
    for d, c, f in configs:
        ds_to_freqs[(d, c)].append(f)
    
    # For each drone, we have exactly one station. So we need to pick one frequency
    # for each drone such that all frequencies are distinct.
    # This is equivalent to finding a matching in a bipartite graph:
    # Left side: drones (1 to k)
    # Right side: frequencies (1 to k)
    # Edge exists if there's a configuration with that drone and frequency
    
    # Build adjacency list for drone -> list of possible frequencies
    drone_freqs = defaultdict(list)
    for (d, c), freqs in ds_to_freqs.items():
        for f in freqs:
            drone_freqs[d].append(f)
    
    # Now we need to match each drone to a distinct frequency
    # This is a bipartite matching problem
    # Use a greedy approach with backtracking or Hungarian algorithm
    # But since k <= 1200, we can use a simple DFS-based approach
    
    match_freq_to_drone = [-1] * (k + 1)  # match_freq_to_drone[f] = d means frequency f is matched to drone d
    match_drone_to_freq = [-1] * (k + 1)  # match_drone_to_freq[d] = f means drone d is matched to frequency f
    
    def dfs(d, visited):
        for f in drone_freqs[d]:
            if visited[f]:
                continue
            visited[f] = True
            
            # If frequency f is not matched or we can find an augmenting path
            if match_freq_to_drone[f] == -1 or dfs(match_freq_to_drone[f], visited):
                match_freq_to_drone[f] = d
                match_drone_to_freq[d] = f
                return True
        return False
    
    # Try to match each drone
    matched = 0
    for d in range(1, k + 1):
        visited = [False] * (k + 1)
        if dfs(d, visited):
            matched += 1
    
    if matched < k:
        print("NO")
        return
    
    print("YES")
    # Output the configurations
    for d in range(1, k + 1):
        f = match_drone_to_freq[d]
        c = drone_to_station[d]
        print(d, c, f)

solve()