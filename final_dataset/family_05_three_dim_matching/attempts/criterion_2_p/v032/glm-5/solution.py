import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    k = int(data[0])
    t = int(data[1])
    
    # ground station x -> list of satellites z
    # due to constraints, each ground station has a unique encryption key
    station_sats = [[] for _ in range(k + 1)]
    
    idx = 2
    for _ in range(t):
        x = int(data[idx]); y = int(data[idx+1]); z = int(data[idx+2])
        idx += 3
        station_sats[x].append(z)
    
    # We need to select exactly one satellite for each ground station
    # such that all selected satellites are distinct (perfect matching)
    # This is a bipartite matching problem: ground stations -> satellites
    
    # Check if all ground stations have at least one link
    for x in range(1, k + 1):
        if not station_sats[x]:
            print("NO")
            return
    
    # Hopcroft-Karp algorithm for bipartite matching
    # Left side: ground stations 1..k
    # Right side: satellites 1..k
    
    # Build adjacency list
    adj = station_sats  # adj[x] = list of satellites for station x
    
    pair_u = [0] * (k + 1)  # pair_u[x] = satellite matched to station x, 0 if unmatched
    pair_v = [0] * (k + 1)  # pair_v[z] = station matched to satellite z, 0 if unmatched
    dist = [0] * (k + 1)
    
    from collections import deque
    
    INF = float('inf')
    
    def bfs():
        queue = deque()
        for u in range(1, k + 1):
            if pair_u[u] == 0:
                dist[u] = 0
                queue.append(u)
            else:
                dist[u] = INF
        dist[0] = INF
        while queue:
            u = queue.popleft()
            if dist[u] < dist[0]:
                for v in adj[u]:
                    if pair_v[v] == 0:
                        if dist[0] == INF:
                            dist[0] = dist[u] + 1
                    else:
                        if dist[pair_v[v]] == INF:
                            dist[pair_v[v]] = dist[u] + 1
                            queue.append(pair_v[v])
        return dist[0] != INF
    
    def dfs(u):
        for v in adj[u]:
            if pair_v[v] == 0 or (dist[pair_v[v]] == dist[u] + 1 and dfs(pair_v[v])):
                pair_u[u] = v
                pair_v[v] = u
                return True
        dist[u] = INF
        return False
    
    matching = 0
    while bfs():
        for u in range(1, k + 1):
            if pair_u[u] == 0:
                if dfs(u):
                    matching += 1
    
    if matching == k:
        print("YES")
        for x in range(1, k + 1):
            z = pair_u[x]
            # We need to output x y z
            # Due to constraints, each ground station x has a unique encryption key y
            # But we need to find what y is from the input
            # Actually, we can just re-read the input to find y for each x
            # But that's inefficient. Let's store it.
            pass
        # We need to store the encryption key for each ground station
        # Let's re-read
        # Actually, let's just store it during the first read
        # But we already read the data... let's re-parse
        # Actually, the encryption key y is the same for all links of ground station x
        # So we can just find any link for station x and get y
        # But we already consumed the data... let's re-read from the stored data
        # Actually, we stored station_sats but not the keys
        # Let's re-parse the data to get the key for each station
        station_key = [0] * (k + 1)
        idx2 = 2
        for _ in range(t):
            x = int(data[idx2]); y = int(data[idx2+1]); z = int(data[idx2+2])
            idx2 += 3
            station_key[x] = y
        
        for x in range(1, k + 1):
            z = pair_u[x]
            y = station_key[x]
            print(f"{x} {y} {z}")
    else:
        print("NO")

solve()