import sys
from collections import deque

def solve():
    data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(data[idx]); idx += 1
    m = int(data[idx]); idx += 1
    k = int(data[idx]); idx += 1
    
    adj = [[] for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(data[idx]); idx += 1
        v = int(data[idx]); idx += 1
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    if k == 1:
        print("YES")
        print(1)
        return
    
    # BFS to find the two camps (bipartite coloring)
    color = [0] * (n + 1)
    camp_a = []
    camp_b = []
    
    for start in range(1, n + 1):
        if color[start] == 0:
            color[start] = 1
            queue = deque([start])
            while queue:
                u = queue.popleft()
                if color[u] == 1:
                    camp_a.append(u)
                else:
                    camp_b.append(u)
                for v in adj[u]:
                    if color[v] == 0:
                        color[v] = 3 - color[u]
                        queue.append(v)
    
    # Check if either camp alone has k users
    if len(camp_a) >= k:
        print("YES")
        print(' '.join(map(str, camp_a[:k])))
        return
    if len(camp_b) >= k:
        print("YES")
        print(' '.join(map(str, camp_b[:k])))
        return
    
    # Neither camp has k users, need to combine from both camps
    # We need to find a set S_A from camp A and S_B from camp B
    # such that |S_A| + |S_B| = k and no edges between S_A and S_B
    
    # Strategy: pick the vertex with minimum degree in camp A (or B)
    # Its non-neighbors in the other camp form a large independent set
    
    # Find vertex with minimum degree overall
    min_deg = n + 1
    min_v = -1
    for v in range(1, n + 1):
        d = len(adj[v])
        if d < min_deg:
            min_deg = d
            min_v = v
    
    # If min_v is in camp A, its non-neighbors in camp B form an independent set
    # We can take min_v + (k-1) non-neighbors from camp B
    # But we need to ensure those k-1 non-neighbors are mutually non-adjacent
    # Since they're all in camp B, and camp B is an independent set, this works!
    
    neighbors = set(adj[min_v])
    
    if color[min_v] == 1:
        # min_v in camp A, non-neighbors in camp B
        candidates = [v for v in camp_b if v not in neighbors]
    else:
        # min_v in camp B, non-neighbors in camp A
        candidates = [v for v in camp_a if v not in neighbors]
    
    if len(candidates) >= k - 1:
        result = [min_v] + candidates[:k-1]
        print("YES")
        print(' '.join(map(str, result)))
        return
    
    # If we can't find k-1 non-neighbors, try the other approach
    # Pick min degree vertex from the other camp
    other_camp = camp_b if color[min_v] == 1 else camp_a
    same_camp = camp_a if color[min_v] == 1 else camp_b
    
    min_deg2 = n + 1
    min_v2 = -1
    for v in other_camp:
        d = len(adj[v])
        if d < min_deg2:
            min_deg2 = d
            min_v2 = v
    
    if min_v2 != -1:
        neighbors2 = set(adj[min_v2])
        candidates2 = [v for v in same_camp if v not in neighbors2]
        if len(candidates2) >= k - 1:
            result = [min_v2] + candidates2[:k-1]
            print("YES")
            print(' '.join(map(str, result)))
            return
    
    print("NO")

solve()