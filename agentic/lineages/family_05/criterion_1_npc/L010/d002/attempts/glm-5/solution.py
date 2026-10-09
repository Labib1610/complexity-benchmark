import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    configs = []
    # Map (x, y) -> list of z values
    xy_to_z = {}
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        configs.append((x, y, z))
        key = (x, y)
        if key not in xy_to_z:
            xy_to_z[key] = []
        xy_to_z[key].append(z)
    
    # Build bipartite graph between X and Y
    # For each edge (x, y), store list of available z values
    adj = [[] for _ in range(k + 1)]
    edge_data = {}  # (x, y) -> list of z values
    for x in range(1, k + 1):
        for y in range(1, k + 1):
            key = (x, y)
            if key in xy_to_z:
                adj[x].append(y)
                edge_data[key] = xy_to_z[key]
    
    # Find perfect matching using bitmask DP
    # dp[mask] = x value matched to this mask (mask represents which y's are used)
    # dp[mask] = 0 means unreachable
    dp = [0] * (1 << k)
    dp[0] = -1  # Start marker
    
    for mask in range(1 << k):
        if dp[mask] == 0:
            continue
        # Determine which x we're trying to match
        # Count bits in mask to get current x
        x = bin(mask).count('1') + 1
        if x > k:
            continue
        for y in adj[x]:
            bit = 1 << (y - 1)
            if mask & bit:
                continue
            new_mask = mask | bit
            if dp[new_mask] == 0:
                dp[new_mask] = y
    
    final_mask = (1 << k) - 1
    if dp[final_mask] == 0:
        print("NO")
        return
    
    # Reconstruct matching
    matching = {}
    mask = final_mask
    for x in range(k, 0, -1):
        y = dp[mask]
        matching[x] = y
        mask ^= (1 << (y - 1))
    
    # Now we have matching (x, y) pairs, need to assign z values
    # Build bipartite graph: X nodes on left, Z nodes on right
    # Edge exists if (x, matching[x], z) is a valid configuration
    adj_z = [[] for _ in range(k + 1)]
    for x in range(1, k + 1):
        y = matching[x]
        key = (x, y)
        if key in edge_data:
            for z in edge_data[key]:
                adj_z[x].append(z)
    
    # Find matching using Hungarian algorithm / augmenting paths
    match_z = [0] * (k + 1)  # match_z[z] = x matched to z
    
    def dfs_z(x, visited):
        for z in adj_z[x]:
            if visited[z]:
                continue
            visited[z] = True
            if match_z[z] == 0 or dfs_z(match_z[z], visited):
                match_z[z] = x
                return True
        return False
    
    for x in range(1, k + 1):
        visited = [False] * (k + 1)
        if not dfs_z(x, visited):
            print("NO")
            return
    
    # Found valid deployment
    print("YES")
    for z in range(1, k + 1):
        x = match_z[z]
        y = matching[x]
        print(x, y, z)

if __name__ == "__main__":
    solve()