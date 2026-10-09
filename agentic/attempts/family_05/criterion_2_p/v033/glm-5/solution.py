import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    # Map (x, y) -> list of z values
    xy_to_z = {}
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        key = (x, y)
        if key not in xy_to_z:
            xy_to_z[key] = []
        xy_to_z[key].append(z)
    
    # Build bipartite graph between (x,y) pairs and z values
    # Left side: pairs (x,y), Right side: z values 1..k
    
    # Assign indices to pairs
    pairs = list(xy_to_z.keys())
    n_pairs = len(pairs)
    pair_to_idx = {pair: i for i, pair in enumerate(pairs)}
    
    # Build adjacency list
    adj = [[] for _ in range(n_pairs)]
    for pair, zlist in xy_to_z.items():
        idx = pair_to_idx[pair]
        for z in zlist:
            adj[idx].append(z)
    
    # Hopcroft-Karp for maximum matching
    INF = n_pairs + k + 10
    pair_match = [-1] * n_pairs  # which z is matched to this pair
    z_match = [-1] * (k + 1)     # which pair is matched to this z
    
    def bfs():
        dist = [INF] * n_pairs
        queue = []
        for u in range(n_pairs):
            if pair_match[u] == -1:
                dist[u] = 0
                queue.append(u)
        d = INF
        idx = 0
        while idx < len(queue):
            u = queue[idx]
            idx += 1
            if dist[u] < d:
                for z in adj[u]:
                    v = z_match[z]
                    if v == -1:
                        d = dist[u] + 1
                    elif dist[v] == INF:
                        dist[v] = dist[u] + 1
                        queue.append(v)
        return d != INF, dist, d
    
    def dfs(u, dist, d):
        for z in adj[u]:
            v = z_match[z]
            if v == -1 or (dist[v] == dist[u] + 1 and dist[v] < d and dfs(v, dist, d)):
                pair_match[u] = z
                z_match[z] = u
                return True
        dist[u] = INF
        return False
    
    matching = 0
    while True:
        found, dist, d = bfs()
        if not found:
            break
        for u in range(n_pairs):
            if pair_match[u] == -1 and dist[u] == 0:
                if dfs(u, dist, d):
                    matching += 1
    
    if matching != k:
        print("NO")
        return
    
    # Check if all x and y are covered exactly once
    x_used = [False] * (k + 1)
    y_used = [False] * (k + 1)
    result = []
    
    for u in range(n_pairs):
        z = pair_match[u]
        if z != -1:
            x, y = pairs[u]
            if x_used[x] or y_used[y]:
                print("NO")
                return
            x_used[x] = True
            y_used[y] = True
            result.append((x, y, z))
    
    if len(result) != k:
        print("NO")
        return
    
    print("YES")
    for x, y, z in result:
        print(x, y, z)

if __name__ == "__main__":
    solve()