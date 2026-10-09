import sys
sys.setrecursionlimit(1000000)

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    # Sort vertices by degree for better pruning
    order = sorted(range(n), key=lambda x: len(adj[x]))
    
    # For fast neighbor checks
    adj_set = [set(adj[i]) for i in range(n)]
    
    chosen = []
    best = None
    
    def dfs(idx, current_set, available):
        nonlocal best
        if best is not None:
            return
        if len(current_set) == k:
            best = current_set[:]
            return
        if idx == n:
            return
        # Prune: if even taking all remaining vertices won't reach k
        if len(current_set) + (n - idx) < k:
            return
        
        v = order[idx]
        # Option 1: skip v
        dfs(idx + 1, current_set, available)
        if best is not None:
            return
        
        # Option 2: take v if possible
        if v in available:
            new_available = available - adj_set[v] - {v}
            current_set.append(v)
            dfs(idx + 1, current_set, new_available)
            current_set.pop()
    
    # Initial available set: all vertices
    all_vertices = set(range(n))
    dfs(0, [], all_vertices)
    
    if best is None:
        print("NO")
    else:
        print("YES")
        print(" ".join(str(x + 1) for x in best))

if __name__ == "__main__":
    solve()