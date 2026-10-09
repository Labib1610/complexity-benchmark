import sys
sys.setrecursionlimit(1 << 25)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].append(v)
        adj[v].append(u)
    
    # BFS to find the diameter of the tree
    def bfs_furthest(start):
        dist = [-1] * (n + 1)
        q = [start]
        dist[start] = 0
        head = 0
        furthest_node = start
        while head < len(q):
            u = q[head]
            head += 1
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
                    if dist[v] > dist[furthest_node]:
                        furthest_node = v
        return furthest_node, dist

    # Find one endpoint of diameter
    ep1, _ = bfs_furthest(1)
    # Find the other endpoint and distances from ep1
    ep2, dist1 = bfs_furthest(ep1)
    # Get distances from ep2
    _, dist2 = bfs_furthest(ep2)
    
    # Assign positions: minimize sum of edge lengths
    # Bandwidth heuristic: place modules with largest dist1+dist2 in the middle
    band = []
    for u in range(1, n + 1):
        band.append((dist1[u] + dist2[u], u))
    
    # Sort by bandwidth
    band.sort(key=lambda x: x[0])
    
    # Assign positions: low bandwidth to ends, high bandwidth to middle
    pos = [0] * (n + 1)
    left = 1
    right = n
    toggle = True
    for _, u in band:
        if toggle:
            pos[u] = left
            left += 1
        else:
            pos[u] = right
            right -= 1
        toggle = not toggle
    
    # Calculate total length
    total_len = 0
    for u in range(1, n + 1):
        for v in adj[u]:
            if u < v:
                total_len += abs(pos[u] - pos[v])
    
    if total_len <= B:
        print("YES")
        print(' '.join(map(str, pos[1:])))
    else:
        print("NO")

solve()