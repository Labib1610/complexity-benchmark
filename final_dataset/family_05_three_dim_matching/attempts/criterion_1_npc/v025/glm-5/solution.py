import sys
sys.setrecursionlimit(10000)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    triples = []
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        triples.append((x, y, z))
    
    # Build adjacency list: for each (source x, reflection y), list of detectors z
    adj = {}
    for x, y, z in triples:
        adj.setdefault((x, y), []).append(z)
    
    # We need to find k triples such that:
    # - Each source x appears exactly once
    # - Each reflection y appears exactly once
    # - Each detector z appears exactly once
    
    # This is equivalent to finding a perfect matching in a bipartite graph
    # where left side = sources x, right side = reflections y,
    # and we need to match each (x, y) pair to a unique detector z
    
    # Actually, we need to select k triples (x, y, z) such that:
    # - All x's are distinct (each source used once)
    # - All y's are distinct (each reflection used once)
    # - All z's are distinct (each detector used once)
    
    # This is a 3D matching problem. We can solve it using bipartite matching
    # by fixing one dimension.
    
    # Let's use sources as the left side and (reflection, detector) pairs as right side
    # We need to find a matching where each source is matched to a unique (y, z) pair
    # and all y's and z's are distinct
    
    # Alternative: Use reflections as left side and (source, detector) as right side
    
    # Let's try: sources (1..k) on left, reflections (1..k) on right
    # For each edge (x, y), we have possible detectors z
    # We need to select k edges such that each x and y is used exactly once,
    # and all z's are distinct
    
    # This is a bipartite matching with additional constraint on z
    # We can use maximum flow or augmenting paths
    
    # Let's use Hopcroft-Karp for bipartite matching
    # Left: sources 1..k
    # Right: reflections 1..k
    # Edge exists if there's a valid triple (x, y, z) for some z
    
    # But we also need to ensure z's are distinct
    
    # Approach: For each matching of sources to reflections, check if we can
    # assign distinct detectors
    
    # Better: Use bipartite matching where left = sources, right = reflections
    # and for each matched pair (x, y), we track which z is used
    
    # We can use a flow network:
    # Source -> sources (capacity 1)
    # sources -> reflections (capacity 1, with specific z)
    # reflections -> detectors (capacity 1)
    # detectors -> sink (capacity 1)
    
    # But this is complex. Let's use a simpler approach:
    # Try all permutations of sources to reflections and check if detectors can be distinct
    
    # For k up to 22, this is too slow (22! permutations)
    
    # Better: Use bipartite matching with augmenting paths
    # We'll match sources to (reflection, detector) pairs
    
    # Let's reformulate:
    # Left side: sources 1..k
    # Right side: all valid (y, z) pairs from triples
    # We need to find a matching of size k where all y's are distinct and all z's are distinct
    
    # This is still complex. Let's use a different approach:
    # Use bipartite matching iteratively
    
    # Actually, let's use the standard 3D matching reduction:
    # Create a bipartite graph where left = sources, right = reflections
    # For each edge (x, y), we have a list of possible z's
    # We need to find a perfect matching and assign z's such that all z's are distinct
    
    # This can be solved by finding a maximum matching and then checking if we can
    # assign z's uniquely
    
    # Let's use a greedy approach with backtracking
    
    # Build adjacency: for each source x, list of (y, z) pairs
    adj_x = {}
    for x, y, z in triples:
        adj_x.setdefault(x, []).append((y, z))
    
    # Try to find a matching using DFS with augmenting paths
    # We'll match sources to (y, z) pairs, ensuring y's and z's are unique
    
    match_y = [0] * (k + 1)  # match_y[y] = x if reflection y is matched to source x
    match_z = [0] * (k + 1)  # match_z[z] = x if detector z is matched to source x
    match_x = [None] * (k + 1)  # match_x[x] = (y, z) if source x is matched
    
    def dfs(x, visited_y, visited_z):
        """Try to find an augmenting path starting from source x"""
        if x not in adj_x:
            return False
        for y, z in adj_x[x]:
            if visited_y[y] or visited_z[z]:
                continue
            visited_y[y] = True
            visited_z[z] = True
            if match_y[y] == 0 and match_z[z] == 0:
                # Both y and z are free
                match_y[y] = x
                match_z[z] = x
                match_x[x] = (y, z)
                return True
            # Try to reassign
            old_x_y = match_y[y]
            old_x_z = match_z[z]
            
            # Case 1: y is matched, z is free
            if match_y[y] != 0 and match_z[z] == 0:
                # Try to reassign the source that uses y
                match_y[y] = x
                match_z[z] = x
                match_x[x] = (y, z)
                if dfs(old_x_y, visited_y, visited_z):
                    return True
                # Backtrack
                match_y[y] = old_x_y
                match_z[z] = 0
                match_x[x] = None
            
            # Case 2: y is free, z is matched
            elif match_y[y] == 0 and match_z[z] != 0:
                match_y[y] = x
                match_z[z] = x
                match_x[x] = (y, z)
                if dfs(old_x_z, visited_y, visited_z):
                    return True
                match_y[y] = 0
                match_z[z] = old_x_z
                match_x[x] = None
            
            # Case 3: Both y and z are matched (possibly to same or different sources)
            else:
                # Both are matched
                if old_x_y == old_x_z:
                    # Same source uses both y and z, can't reassign
                    continue
                # Try to reassign both
                match_y[y] = x
                match_z[z] = x
                match_x[x] = (y, z)
                temp_y = match_y[y]
                temp_z = match_z[z]
                if dfs(old_x_y, visited_y, visited_z) and dfs(old_x_z, visited_y, visited_z):
                    return True
                # Backtrack
                match_y[y] = old_x_y
                match_z[z] = old_x_z
                match_x[x] = None
        
        return False
    
    # Try to match each source
    for x in range(1, k + 1):
        visited_y = [False] * (k + 1)
        visited_z = [False] * (k + 1)
        if not dfs(x, visited_y, visited_z):
            print("NO")
            return
    
    # Check if we have a valid matching
    result = []
    for x in range(1, k + 1):
        if match_x[x] is None:
            print("NO")
            return
        y, z = match_x[x]
        result.append((x, y, z))
    
    print("YES")
    for x, y, z in result:
        print(x, y, z)

solve()