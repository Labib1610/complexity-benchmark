import sys
sys.setrecursionlimit(1000000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    adj = [[] for _ in range(n)]
    edges = []
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # Check if graph is a path
    deg = [len(adj[i]) for i in range(n)]
    if max(deg) > 2:
        # Not a path, but maybe still possible with small B?
        # We'll try backtracking anyway.
        pass
    
    # Try to find a Hamiltonian path order that minimizes sum
    # Use backtracking with pruning
    best_perm = None
    best_cost = float('inf')
    
    # Precompute adjacency matrix for O(1) distance checks
    adj_mat = [[False]*n for _ in range(n)]
    for u,v in edges:
        adj_mat[u][v] = adj_mat[v][u] = True
    
    # Try starting from each node
    for start in range(n):
        perm = [start]
        used = [False]*n
        used[start] = True
        # DFS
        def dfs(pos, cost):
            nonlocal best_perm, best_cost
            if cost > B:
                return
            if pos == n:
                if cost < best_cost:
                    best_cost = cost
                    best_perm = perm[:]
                return
            # Try next nodes
            # Heuristic: try neighbors first
            candidates = []
            for v in range(n):
                if not used[v]:
                    # distance from last placed
                    d = abs(pos - (pos))  # will compute after placement
                    # Actually distance is |pos - last_index|, but we place in order
                    # So if we place v at position pos, distance to last placed is 1
                    # But we need to consider all edges from v to already placed nodes
                    # We'll compute cost increment
                    inc = 0
                    for u in perm:
                        if adj_mat[u][v]:
                            inc += abs(perm.index(u) - pos)
                    candidates.append((inc, v))
            candidates.sort()
            for inc, v in candidates:
                if cost + inc > B:
                    continue
                used[v] = True
                perm.append(v)
                dfs(pos+1, cost+inc)
                perm.pop()
                used[v] = False
        dfs(1, 0)
        if best_perm is not None and best_cost <= B:
            break
    
    if best_perm is not None and best_cost <= B:
        print("YES")
        # Convert to 1-based slot numbers: position i gets slot i+1
        res = [0]*n
        for slot, mod in enumerate(best_perm):
            res[mod] = slot+1
        print(' '.join(map(str, res)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()