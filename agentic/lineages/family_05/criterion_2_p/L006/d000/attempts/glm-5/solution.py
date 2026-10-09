import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    k = int(input_data[idx]); idx += 1
    t = int(input_data[idx]); idx += 1
    
    # For each pilot x, collect the set of allowed routes z
    pilot_routes = [set() for _ in range(k + 1)]
    
    for _ in range(t):
        x = int(input_data[idx]); idx += 1
        y = int(input_data[idx]); idx += 1
        z = int(input_data[idx]); idx += 1
        pilot_routes[x].add(z)
    
    # Build bipartite graph: pilots 1..k on left, routes 1..k on right
    # Edge from pilot x to route z if (x, *, z) is allowed
    
    # Hopcroft-Karp for maximum bipartite matching
    # Left: pilots 1..k, Right: routes 1..k
    
    adj = [[] for _ in range(k + 1)]
    for x in range(1, k + 1):
        for z in pilot_routes[x]:
            adj[x].append(z)
    
    # match_left[x] = route assigned to pilot x, or 0
    # match_right[z] = pilot assigned to route z, or 0
    match_left = [0] * (k + 1)
    match_right = [0] * (k + 1)
    dist = [0] * (k + 1)
    
    from collections import deque
    
    INF = float('inf')
    
    def bfs():
        queue = deque()
        for x in range(1, k + 1):
            if match_left[x] == 0:
                dist[x] = 0
                queue.append(x)
            else:
                dist[x] = INF
        
        dist[0] = INF
        
        while queue:
            x = queue.popleft()
            if dist[x] < dist[0]:
                for z in adj[x]:
                    px = match_right[z]
                    if dist[px] == INF:
                        dist[px] = dist[x] + 1
                        queue.append(px)
        
        return dist[0] != INF
    
    def dfs(x):
        if x == 0:
            return True
        for z in adj[x]:
            px = match_right[z]
            if dist[px] == dist[x] + 1:
                if dfs(px):
                    match_left[x] = z
                    match_right[z] = x
                    return True
        dist[x] = INF
        return False
    
    matching_size = 0
    while bfs():
        for x in range(1, k + 1):
            if match_left[x] == 0:
                if dfs(x):
                    matching_size += 1
    
    if matching_size < k:
        print("NO")
        return
    
    print("YES")
    for x in range(1, k + 1):
        z = match_left[x]
        # pilot x, aircraft y = x (since pilot x is certified on aircraft x)
        print(f"{x} {x} {z}")

solve()