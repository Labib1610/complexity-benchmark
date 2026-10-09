import sys
sys.setrecursionlimit(10000)

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    adj = [set() for _ in range(n)]
    for _ in range(m):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        adj[u].add(v)
        adj[v].add(u)
    
    # Try to find an independent set of size k
    # Strategy: try all subsets of size k (n <= 46, but we use pruning)
    
    best = None
    
    # For small k, use recursive search with pruning
    # For larger k, we can use complement approach
    
    # Use branch and bound with vertex ordering
    vertices = list(range(n))
    
    # Sort by degree (heuristic)
    vertices.sort(key=lambda x: len(adj[x]))
    
    # Upper bound: size of remaining vertices + current selection
    # Lower bound: we need exactly k
    
    def search(selected, candidates, start):
        nonlocal best
        if best is not None:
            return
        if len(selected) == k:
            best = selected[:]
            return
        if len(selected) + len(candidates) < k:
            return
        
        # Pruning: if we can't reach k, stop
        remaining_needed = k - len(selected)
        if len(candidates) < remaining_needed:
            return
        
        # Try adding each candidate
        for i, v in enumerate(candidates):
            if len(selected) + 1 + (len(candidates) - i - 1) < k:
                break  # Can't reach k even with all remaining
            
            # Check if v conflicts with selected
            conflict = False
            for u in selected:
                if v in adj[u]:
                    conflict = True
                    break
            if conflict:
                continue
            
            # Add v and filter remaining candidates
            new_candidates = []
            for j in range(i + 1, len(candidates)):
                u = candidates[j]
                if u not in adj[v]:
                    new_candidates.append(u)
            
            selected.append(v)
            search(selected, new_candidates, 0)
            selected.pop()
            
            if best is not None:
                return
    
    search([], vertices, 0)
    
    if best is not None:
        print("YES")
        print(' '.join(str(x + 1) for x in best))
        return
    
    # If k is large, try complement approach: find clique of size n-k in complement graph
    # Then the remaining vertices form an independent set of size k
    
    if k > n // 2:
        # Find clique of size n - k in complement graph
        target_clique = n - k
        if target_clique == 0:
            print("YES")
            print(' '.join(str(i + 1) for i in range(n)))
            return
        
        # Build complement adjacency
        comp_adj = [set() for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j and j not in adj[i]:
                    comp_adj[i].add(j)
        
        clique = []
        found_clique = [None]
        
        def bron_kerbosch(R, P, X):
            if found_clique[0] is not None:
                return
            if len(R) == target_clique:
                found_clique[0] = R[:]
                return
            if len(R) + len(P) < target_clique:
                return
            
            # Choose pivot from P union X with max degree in P
            pivot = None
            max_deg = -1
            for v in P | X:
                deg = len(P & comp_adj[v])
                if deg > max_deg:
                    max_deg = deg
                    pivot = v
            
            for v in list(P - comp_adj[pivot] if pivot else P):
                if found_clique[0] is not None:
                    return
                bron_kerbosch(R + [v], P & comp_adj[v], X & comp_adj[v])
                P.remove(v)
                X.add(v)
        
        P = set(range(n))
        bron_kerbosch([], P, set())
        
        if found_clique[0] is not None:
            clique_set = set(found_clique[0])
            result = [i for i in range(n) if i not in clique_set]
            print("YES")
            print(' '.join(str(x + 1) for x in result))
            return
    
    print("NO")

solve()