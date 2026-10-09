import sys
sys.setrecursionlimit(10000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    k = int(next(it))
    t = int(next(it))
    
    # We need to find k triples (m, c, f) such that:
    # - Each m in [1..k] appears exactly once
    # - Each c in [1..k] appears exactly once
    # - Each f in [1..k] appears exactly once
    
    # This is a 3D matching problem. We can reduce it to bipartite matching.
    # Match pairs (c, f) to modules m.
    # A pair (c, f) is valid for module m if the triple (m, c, f) exists.
    
    # Build adjacency: for each pair (c, f), list of modules m that can go there
    # Map (c, f) to an index 0..k*k-1
    pair_to_idx = {}
    idx_to_pair = []
    for c in range(1, k+1):
        for f in range(1, k+1):
            pair_to_idx[(c, f)] = len(idx_to_pair)
            idx_to_pair.append((c, f))
    
    adj = [[] for _ in range(k * k)]
    records = []  # list of (m, c, f)
    
    for _ in range(t):
        m = int(next(it))
        c = int(next(it))
        f = int(next(it))
        records.append((m, c, f))
        pair_idx = pair_to_idx[(c, f)]
        adj[pair_idx].append(m - 1)  # 0-indexed module
    
    # Bipartite matching: left side = pairs (c, f), right side = modules m
    # We need to match exactly k pairs to k modules
    
    n_pairs = k * k
    n_modules = k
    
    match_to = [-1] * n_modules  # match_to[m] = pair_idx matched to module m
    
    def dfs(pair_idx, visited):
        for m in adj[pair_idx]:
            if visited[m]:
                continue
            visited[m] = True
            if match_to[m] == -1 or dfs(match_to[m], visited):
                match_to[m] = pair_idx
                return True
        return False
    
    match_count = 0
    for pair_idx in range(n_pairs):
        visited = [False] * n_modules
        if dfs(pair_idx, visited):
            match_count += 1
    
    if match_count != k:
        print("NO")
        return
    
    # Now we have k matches: each module m is matched to a pair (c, f)
    # But we also need each row c and each column f to appear exactly once
    # The matching ensures each module appears once, but rows/columns might repeat
    
    # Check if rows and columns are all distinct
    rows_used = set()
    cols_used = set()
    result = []
    
    for m in range(n_modules):
        pair_idx = match_to[m]
        c, f = idx_to_pair[pair_idx]
        if c in rows_used or f in cols_used:
            print("NO")
            return
        rows_used.add(c)
        cols_used.add(f)
        result.append((m + 1, c, f))
    
    print("YES")
    for m, c, f in result:
        print(m, c, f)

if __name__ == "__main__":
    solve()