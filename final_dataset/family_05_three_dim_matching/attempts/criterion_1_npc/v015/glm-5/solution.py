import sys
sys.setrecursionlimit(1000000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    # Build adjacency: for each (node, image) pair, list of valid shards
    adj = {}
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        key = (x, y)
        if key not in adj:
            adj[key] = []
        adj[key].append(z)
    
    # match_shard[z] = (x, y) that uses shard z
    match_shard = {}
    # match_image[y] = x that uses image y
    match_image = {}
    # match_node[x] = y that uses node x
    match_node = {}
    
    def dfs_shard(x, y, visited_shard):
        for z in adj.get((x, y), []):
            if z in visited_shard:
                continue
            visited_shard.add(z)
            if z not in match_shard:
                match_shard[z] = (x, y)
                return True
            else:
                ox, oy = match_shard[z]
                if dfs_shard(ox, oy, visited_shard):
                    match_shard[z] = (x, y)
                    return True
        return False
    
    def dfs_image(x, visited_image):
        for y in range(1, k + 1):
            if y in visited_image:
                continue
            # Check if (x, y) has valid shards
            if (x, y) not in adj:
                continue
            visited_image.add(y)
            if y not in match_image:
                # Try to match this (x, y) with a shard
                visited_shard = set()
                if dfs_shard(x, y, visited_shard):
                    match_image[y] = x
                    return True
            else:
                ox = match_image[y]
                if dfs_image(ox, visited_image):
                    visited_shard = set()
                    if dfs_shard(x, y, visited_shard):
                        match_image[y] = x
                        return True
        return False
    
    # Main matching loop
    for x in range(1, k + 1):
        visited_image = set()
        if not dfs_image(x, visited_image):
            print("NO")
            return
    
    print("YES")
    # Reconstruct solution
    for y in range(1, k + 1):
        x = match_image[y]
        # Find which shard is used for (x, y)
        for z in adj.get((x, y), []):
            if z in match_shard and match_shard[z] == (x, y):
                print(x, y, z)
                break

solve()