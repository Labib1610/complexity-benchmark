from collections import defaultdict

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    k = int(data[0])
    t = int(data[1])
    
    protocols = []
    index = 2
    for _ in range(t):
        u = int(data[index])
        v = int(data[index+1])
        w = int(data[index+2])
        protocols.append((u, v, w))
        index += 3
    
    # Since each sensor cluster is tied to exactly one relay station,
    # and no two sensor clusters share the same relay station,
    # we can think of this as a matching problem.
    # For each sensor cluster u, it's paired with a unique relay station v.
    # So we can represent each protocol by (u, w) since v is determined by u.
    
    # Build a mapping from sensor cluster to its relay station
    sensor_to_relay = {}
    for u, v, w in protocols:
        if u not in sensor_to_relay:
            sensor_to_relay[u] = v
        else:
            # This is just a consistency check based on problem statement
            assert sensor_to_relay[u] == v
    
    # Group protocols by sensor cluster
    protocols_by_sensor = defaultdict(list)
    for u, v, w in protocols:
        protocols_by_sensor[u].append((u, v, w))
    
    # We need to select exactly one protocol for each sensor cluster
    # such that the control frequencies form a permutation of 1..k
    
    # This is equivalent to finding a perfect matching in a bipartite graph
    # where left side is sensor clusters, right side is control frequencies
    # and edges exist if there's a protocol for that sensor with that frequency
    
    # Build the bipartite graph
    # Left nodes: sensor clusters (which also determine relay stations)
    # Right nodes: control frequencies 1 to k
    # Edges: (sensor, freq) if there exists a protocol with that sensor and freq
    
    # But since we must use exactly k sensors and they map to exactly k relays,
    # and we're given that different sensors use different relays,
    # the set of sensors in any solution must be all sensors 1..k
    
    # Check if we have all sensors 1..k present
    available_sensors = set(protocols_by_sensor.keys())
    required_sensors = set(range(1, k+1))
    
    if available_sensors != required_sensors:
        print("NO")
        return
    
    # For each sensor, build list of possible control frequencies
    # Each sensor must be used exactly once, and each control frequency exactly once
    # This is a bipartite matching problem: sensors <-> control frequencies
    
    from collections import deque
    
    # Build adjacency list for sensors to control frequencies
    adj = defaultdict(list)
    for u in range(1, k+1):
        for u, v, w in protocols_by_sensor[u]:
            adj[u].append(w)
    
    # Solve maximum bipartite matching using Ford-Fulkerson/DFS
    def dfs(u, match_sensor_to_freq, match_freq_to_sensor, visited):
        for w in adj[u]:
            if visited[w]:
                continue
            visited[w] = True
            
            # If frequency w is unmatched or we can find augmenting path
            if match_freq_to_sensor[w] == -1 or dfs(match_freq_to_sensor[w], match_sensor_to_freq, match_freq_to_sensor, visited):
                match_sensor_to_freq[u] = w
                match_freq_to_sensor[w] = u
                return True
        return False
    
    # Initialize matching arrays
    match_sensor_to_freq = [-1] * (k + 1)  # 1-indexed
    match_freq_to_sensor = [-1] * (k + 1)  # 1-indexed
    
    matched = 0
    for u in range(1, k + 1):
        visited = [False] * (k + 1)
        if dfs(u, match_sensor_to_freq, match_freq_to_sensor, visited):
            matched += 1
    
    if matched != k:
        print("NO")
        return
    
    print("YES")
    # Reconstruct the solution
    result = []
    for u in range(1, k + 1):
        w = match_sensor_to_freq[u]
        v = sensor_to_relay[u]
        result.append(f"{u} {v} {w}")
    
    print("\n".join(result))

solve()