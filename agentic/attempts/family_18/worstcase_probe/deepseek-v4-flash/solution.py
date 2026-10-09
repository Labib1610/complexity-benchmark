import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    B = int(next(it))
    adj = [[] for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].append(v)
        adj[v].append(u)
    
    # If B is huge, any permutation works
    # But we need to find one.
    
    # Try a simple heuristic first: order by degree descending
    order = sorted(range(n), key=lambda x: -len(adj[x]))
    pos = [0]*n
    for i, node in enumerate(order):
        pos[node] = i+1
    total = 0
    for u in range(n):
        for v in adj[u]:
            if u < v:
                total += abs(pos[u]-pos[v])
    if total <= B:
        print("YES")
        print(' '.join(str(pos[i]) for i in range(n)))
        return
    
    # If n is small, try backtracking
    if n <= 15:
        # backtracking with pruning
        best = [None]
        best_cost = [10**18]
        used = [False]*n
        perm = []
        cur_cost = 0
        
        # Precompute adjacency as bitmask for speed
        adj_mask = [0]*n
        for u in range(n):
            mask = 0
            for v in adj[u]:
                mask |= (1<<v)
            adj_mask[u] = mask
        
        def backtrack():
            if len(perm) == n:
                if cur_cost <= B:
                    best[0] = perm[:]
                    best_cost[0] = cur_cost
                return
            # lower bound: current cost + minimum possible for remaining edges
            # For each edge not yet fully placed, at least 1 if both endpoints not placed, else 0 if one placed? Actually if one placed and other not, the distance will be at least 1 (since positions differ by at least 1). So lower bound = cur_cost + number of edges with at least one endpoint unplaced.
            # But that's weak. We'll just prune if cur_cost > B.
            if cur_cost > B:
                return
            # Try nodes in order of degree descending for better pruning
            candidates = [i for i in range(n) if not used[i]]
            candidates.sort(key=lambda x: -len(adj[x]))
            for v in candidates:
                # compute added cost
                added = 0
                k = len(perm)+1  # position 1-indexed
                for u in perm:
                    if u in adj[v]:  # check adjacency
                        added += k - (perm.index(u)+1)
                # Actually perm.index is O(n), but n small
                used[v] = True
                perm.append(v)
                cur_cost += added
                backtrack()
                cur_cost -= added
                perm.pop()
                used[v] = False
                if best[0] is not None:
                    return
        
        backtrack()
        if best[0] is not None:
            pos = [0]*n
            for i, node in enumerate(best[0]):
                pos[node] = i+1
            print("YES")
            print(' '.join(str(pos[i]) for i in range(n)))
            return
    
    # If n > 15, try a greedy with local search (swap)
    # Simple: start with degree order, then try swapping pairs to reduce cost
    pos = [0]*n
    order = sorted(range(n), key=lambda x: -len(adj[x]))
    for i, node in enumerate(order):
        pos[node] = i+1
    
    def total_cost(pos):
        s = 0
        for u in range(n):
            for v in adj[u]:
                if u < v:
                    s += abs(pos[u]-pos[v])
        return s
    
    cur = total_cost(pos)
    improved = True
    while improved:
        improved = False
        for i in range(n):
            for j in range(i+1, n):
                # swap positions of i and j
                pos[i], pos[j] = pos[j], pos[i]
                new_cost = total_cost(pos)
                if new_cost < cur:
                    cur = new_cost
                    improved = True
                else:
                    pos[i], pos[j] = pos[j], pos[i]
        if cur <= B:
            print("YES")
            print(' '.join(str(pos[i]) for i in range(n)))
            return
    
    # If still not, try random restarts? But time limit.
    # We'll just output NO if not found.
    print("NO")

if __name__ == "__main__":
    solve()