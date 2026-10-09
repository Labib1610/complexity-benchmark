import sys

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    points = set()
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        points.add((x, y, z))
    
    # We need to select k points such that all x, y, z are distinct
    # This is a 3D matching problem. We'll use bipartite matching on (x, y) -> z
    
    # Build adjacency: for each (x, y), list of valid z values
    adj = {}
    for x, y, z in points:
        key = (x, y)
        if key not in adj:
            adj[key] = []
        adj[key].append(z)
    
    # Bipartite matching: left side = (x, y) pairs, right side = z values
    # We need to match exactly k pairs
    
    match_z = {}  # z -> (x, y)
    
    def dfs(xy, visited):
        if xy in visited:
            return False
        visited.add(xy)
        if xy not in adj:
            return False
        for z in adj[xy]:
            if z not in match_z:
                match_z[z] = xy
                return True
            else:
                prev_xy = match_z[z]
                if dfs(prev_xy, visited):
                    match_z[z] = xy
                    return True
        return False
    
    matched_pairs = []
    for xy in adj:
        visited = set()
        if dfs(xy, visited):
            x, y = xy
            # Find the z that was matched
            for z in adj[xy]:
                if z in match_z and match_z[z] == xy:
                    matched_pairs.append((x, y, z))
                    break
    
    if len(matched_pairs) >= k:
        print("YES")
        for i in range(k):
            x, y, z = matched_pairs[i]
            print(x, y, z)
    else:
        print("NO")

if __name__ == "__main__":
    solve()