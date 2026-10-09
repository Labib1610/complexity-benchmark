from collections import defaultdict, deque

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    k = int(data[0])
    t = int(data[1])
    
    index = 2
    configs = []
    drone_to_station = {}
    
    for _ in range(t):
        d = int(data[index])
        c = int(data[index+1])
        f = int(data[index+2])
        configs.append((d, c, f))
        drone_to_station[d] = c
        index += 3
    
    # Group configurations by drone
    drone_configs = defaultdict(list)
    for d, c, f in configs:
        drone_configs[d].append((d, c, f))
    
    # Build bipartite graph: drones on one side, frequencies on the other
    # Edge exists if there's a config with that drone and frequency
    # We need a perfect matching in this bipartite graph
    
    # Since each drone is associated with exactly one station,
    # we can think of this as matching drones to frequencies
    # where an edge exists if there's a config (drone, station_of_drone, freq)
    
    # Build adjacency list for drones -> frequencies
    adj = defaultdict(list)
    for d, c, f in configs:
        adj[d].append(f)
    
    # Maximum bipartite matching using Ford-Fulkerson with DFS
    def bpm(u, match_f, seen):
        for v in adj[u]:
            if seen[v]:
                continue
            seen[v] = True
            if match_f[v] == -1 or bpm(match_f[v], match_f, seen):
                match_f[v] = u
                return True
        return False
    
    # match_f[f] = d means frequency f is matched to drone d
    match_f = [-1] * (k + 1)
    
    result = 0
    for d in range(1, k + 1):
        seen = [False] * (k + 1)
        if bpm(d, match_f, seen):
            result += 1
    
    if result < k:
        print("NO")
        return
    
    # Reconstruct the matching
    # match_d[d] = f means drone d is matched to frequency f
    match_d = [-1] * (k + 1)
    for f in range(1, k + 1):
        if match_f[f] != -1:
            match_d[match_f[f]] = f
    
    # Now for each drone, find the config that uses its matched frequency
    selected = []
    for d in range(1, k + 1):
        f = match_d[d]
        c = drone_to_station[d]
        selected.append((d, c, f))
    
    # Verify that all frequencies are used exactly once
    used_freq = [0] * (k + 1)
    for d, c, f in selected:
        used_freq[f] += 1
    
    for f in range(1, k + 1):
        if used_freq[f] != 1:
            print("NO")
            return
    
    print("YES")
    for d, c, f in selected:
        print(d, c, f)

solve()