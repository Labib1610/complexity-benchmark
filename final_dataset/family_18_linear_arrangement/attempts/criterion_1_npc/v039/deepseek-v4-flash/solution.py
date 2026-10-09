import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    edges = []
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        edges.append((u, v))
        adj[u].append(v)
        adj[v].append(u)
    
    # If no edges, any permutation works with cost 0
    if m == 0:
        print("YES")
        print(" ".join(str(i+1) for i in range(n)))
        return
    
    # Sort vertices by degree descending for better pruning
    order = sorted(range(n), key=lambda x: -len(adj[x]))
    pos = [-1] * n
    used = [False] * n
    best_perm = None
    best_cost = float('inf')
    
    # Precompute edge list for cost calculation
    edge_list = edges
    
    # Lower bound: sum of min possible distance for each edge given current partial assignment
    # We'll use a simple bound: for each unassigned edge, min possible distance is 1 if both endpoints unassigned, else something else.
    # But we can do better: for each edge, if one endpoint assigned and other not, min distance is 1 (if slot available) or 0? Actually min distance is at least 1 if both endpoints distinct slots.
    # We'll just use a simple bound: sum of 1 for each remaining edge not yet satisfied? That's weak.
    # Instead, we'll use branch and bound with current cost and prune if > B.
    
    # We'll do DFS assigning in order of 'order'
    def dfs(idx, cost):
        nonlocal best_cost, best_perm
        if cost > B:
            return
        if idx == n:
            if cost < best_cost:
                best_cost = cost
                best_perm = pos[:]
            return
        v = order[idx]
        # Try each unused slot
        for s in range(n):
            if not used[s]:
                # compute added cost
                added = 0
                for nb in adj[v]:
                    if pos[nb] != -1:
                        added += abs(pos[nb] - s)
                # prune
                if cost + added > B:
                    continue
                # Also compute a lower bound for remaining edges: 
                # For each unassigned vertex, at least some cost? We'll skip for simplicity.
                used[s] = True
                pos[v] = s
                # If we already have a solution with cost <= B, we can stop early? We want any <= B, so we can stop at first found.
                # But we want minimal? Actually we just need <= B, so we can stop when found.
                # But to be safe, we can continue to find better? Not needed.
                # We'll just return if we find a solution.
                if idx == n-1:
                    if cost + added <= B:
                        best_cost = cost + added
                        best_perm = pos[:]
                        used[s] = False
                        pos[v] = -1
                        return True
                else:
                    if dfs(idx+1, cost + added):
                        used[s] = False
                        pos[v] = -1
                        return True
                used[s] = False
                pos[v] = -1
        return False
    
    # Start DFS
    found = dfs(0, 0)
    if found or best_perm is not None:
        print("YES")
        # best_perm is position of each vertex index; we need output slot for server 1..n
        # best_perm[i] = slot (0-based) for vertex i
        res = [0]*n
        for i in range(n):
            res[i] = best_perm[i] + 1
        print(" ".join(map(str, res)))
    else:
        print("NO")

if __name__ == "__main__":
    solve()