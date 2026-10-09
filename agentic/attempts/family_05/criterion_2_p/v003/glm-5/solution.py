import sys

def solve():
    data = sys.stdin.buffer.read().split()
    if not data:
        return
    k = int(data[0])
    t = int(data[1])
    
    # xy_to_zs: maps (x,y) -> list of z
    # x_to_y: maps x -> y (since all combos with same x have same y)
    # y_to_x: maps y -> x
    
    xy_to_zs = {}
    x_to_y = {}
    y_to_x = {}
    
    idx = 2
    for _ in range(t):
        x = int(data[idx]); y = int(data[idx+1]); z = int(data[idx+2])
        idx += 3
        key = (x, y)
        if key not in xy_to_zs:
            xy_to_zs[key] = []
        xy_to_zs[key].append(z)
        x_to_y[x] = y
        y_to_x[y] = x
    
    # We need to select k crews, each x used once, each y used once, each z used once.
    # Since x and y are tied (same x => same y, same y => same x), the pairs (x,y) form groups.
    # Each group (x,y) has a set of z's. We need to assign z's to groups such that:
    # - each group gets exactly the number of z's equal to... wait.
    # Actually each x must be used exactly once, so each (x,y) pair that we use must be used exactly once.
    # But we need to use all k x's and all k y's. Since x and y are in bijection (same x => same y and vice versa),
    # the number of distinct (x,y) pairs equals the number of distinct x's equals the number of distinct y's.
    # Let's call this number m. We need m = k for a solution to exist (all x's and y's must be coverable).
    # If m < k, some x or y has no allowed combination, so impossible.
    
    # If m = k, then we need to select exactly one z from each (x,y) group, and all z's must be distinct.
    # This is a bipartite matching: groups on left, z's on right, edge if z is in group's list.
    # We need a perfect matching of size k.
    
    # Check m = k
    if len(x_to_y) != k:
        print("NO")
        return
    
    # Verify y_to_x is consistent (should be by problem guarantee, but let's be safe)
    # Actually the problem guarantees the operational rule, so x_to_y and y_to_x are bijections.
    
    # Build bipartite graph: left nodes are x (1..k), right nodes are z (1..k)
    # Edge x -> z if (x, x_to_y[x]) has z in its list
    
    adj = [[] for _ in range(k+1)]  # adj[x] = list of z's
    for (x, y), zs in xy_to_zs.items():
        adj[x].extend(zs)
    
    # Hopcroft-Karp for bipartite matching
    # Left: x in 1..k, Right: z in 1..k
    pair_x = [0] * (k + 1)  # pair_x[x] = z matched to x, 0 if none
    pair_z = [0] * (k + 1)  # pair_z[z] = x matched to z, 0 if none
    dist = [0] * (k + 1)
    INF = float('inf')
    
    from collections import deque
    
    def bfs():
        queue = deque()
        for x in range(1, k+1):
            if pair_x[x] == 0:
                dist[x] = 0
                queue.append(x)
            else:
                dist[x] = INF
        dist[0] = INF
        while queue:
            x = queue.popleft()
            if dist[x] < dist[0]:
                for z in adj[x]:
                    y = pair_z[z]
                    if y != 0 and dist[y] == INF:
                        dist[y] = dist[x] + 1
                        queue.append(y)
                    elif y == 0:
                        dist[0] = dist[x] + 1
        return dist[0] != INF
    
    def dfs(x):
        for z in adj[x]:
            y = pair_z[z]
            if y == 0 or (dist[y] == dist[x] + 1 and dfs(y)):
                pair_x[x] = z
                pair_z[z] = x
                return True
        dist[x] = INF
        return False
    
    matching = 0
    while bfs():
        for x in range(1, k+1):
            if pair_x[x] == 0:
                if dfs(x):
                    matching += 1
    
    if matching != k:
        print("NO")
        return
    
    print("YES")
    for x in range(1, k+1):
        z = pair_x[x]
        y = x_to_y[x]
        print(f"{x} {y} {z}")

solve()