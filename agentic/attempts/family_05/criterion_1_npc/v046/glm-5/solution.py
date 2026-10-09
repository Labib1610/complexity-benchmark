import sys
sys.setrecursionlimit(10000)

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    # Build adjacency list: for each (analyst, week) pair, list available GPUs
    adj = {}
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        key = (x, z)
        if key not in adj:
            adj[key] = []
        adj[key].append(y)
    
    # match_g[analyst] = week assigned to this analyst
    match_g = [-1] * (k + 1)
    # match_w[week] = analyst assigned to this week
    match_w = [-1] * (k + 1)
    
    def dfs(u, seen):
        for w in range(1, k + 1):
            key = (u, w)
            if key not in adj:
                continue
            if seen[w]:
                continue
            seen[w] = True
            if match_w[w] == -1 or dfs(match_w[w], seen):
                match_w[w] = u
                match_g[u] = w
                return True
        return False
    
    # Find maximum matching
    for u in range(1, k + 1):
        seen = [False] * (k + 1)
        dfs(u, seen)
    
    # Check if we have a perfect matching
    matched_pairs = []
    for w in range(1, k + 1):
        if match_w[w] == -1:
            print("NO")
            return
        matched_pairs.append((match_w[w], w))
    
    # For each matched (analyst, week) pair, find the GPU
    result = []
    for x, z in matched_pairs:
        key = (x, z)
        y = adj[key][0]  # Pick any available GPU for this pair
        result.append((x, y, z))
    
    print("YES")
    for x, y, z in result:
        print(x, y, z)

solve()