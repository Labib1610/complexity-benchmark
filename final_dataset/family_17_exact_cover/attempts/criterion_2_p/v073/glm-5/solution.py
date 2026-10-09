import sys
from collections import deque

def solve():
    input_data = sys.stdin.buffer.read().split()
    if not input_data:
        return
    q = int(input_data[0])
    t = int(input_data[1])
    
    # Build adjacency list for bipartite matching
    # Drones: 1..q, Zones: q+1..2q
    # We'll use 1-indexed for drones, and zone_id = b - q for internal matching
    
    head = [-1] * (q + 1)
    to = [0] * t
    nxt = [0] * t
    
    idx = 2
    for i in range(t):
        a = int(input_data[idx]); b = int(input_data[idx+1]); idx += 2
        to[i] = b - q  # zone internal id: 1..q
        nxt[i] = head[a]
        head[a] = i
    
    match_drone = [0] * (q + 1)  # match_drone[zone] = drone
    match_zone = [0] * (q + 1)   # match_zone[drone] = zone
    
    def try_kuhn(v, visited):
        e = head[v]
        while e != -1:
            u = to[e]
            if not visited[u]:
                visited[u] = True
                if match_drone[u] == 0 or try_kuhn(match_drone[u], visited):
                    match_drone[u] = v
                    match_zone[v] = u
                    return True
            e = nxt[e]
        return False
    
    for v in range(1, q + 1):
        visited = [False] * (q + 1)
        if not try_kuhn(v, visited):
            sys.stdout.write("NO\n")
            return
    
    sys.stdout.write("YES\n")
    out = []
    for v in range(1, q + 1):
        out.append(f"{v} {match_zone[v] + q}")
    sys.stdout.write("\n".join(out) + "\n")

solve()