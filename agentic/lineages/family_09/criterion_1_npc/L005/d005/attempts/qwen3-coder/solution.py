from itertools import combinations

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    
    # Read updates
    edges = []
    adj = [set() for _ in range(n+1)]
    for i in range(m):
        u = int(data[3 + 2*i])
        v = int(data[4 + 2*i])
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # We want to find a subset S of size k such that the induced subgraph has no edges
    # That is, for all i,j in S, there is no edge between i and j
    
    # Try all combinations of k nodes
    from itertools import combinations
    
    # Since n <= 46 and we need combinations, let's optimize:
    # If m is small, we can check all combinations
    # But since n can be up to 46, combinations(46, k) can be huge
    # However, since we only need one solution, we can try a smarter approach
    
    # Let's build complement graph: nodes i,j are connected if there is NO edge between them in original
    # Then we need to find a clique of size k in the complement graph
    # But that's also hard. Let's just try combinations for small enough cases
    
    # For larger cases, let's think differently:
    # If we pick k nodes such that none of them are adjacent in G, then x^T A x = k
    # Because only diagonal terms contribute (A[i][i] = 1), and off-diagonal terms are 0 since no edges within the set
    
    # So we need an independent set of size k in the original graph
    
    # Try all combinations when feasible
    if k == 1:
        print("YES")
        print(1)
        return
        
    # For small n, we can enumerate
    # Actually, let's do a smarter backtracking or use the fact that we might have to try all
    
    # Let's try a greedy approach first: find a maximal independent set
    # But we need exactly k nodes
    
    # Brute force for reasonable limits
    # Given time constraint and n up to 46, but k could be small
    # Let's try combinations if k is small
    
    def is_independent(nodes):
        node_set = set(nodes)
        for u in nodes:
            for v in adj[u]:
                if v in node_set:
                    return False
        return True
    
    # Special case: if no edges, any k nodes work
    if m == 0:
        print("YES")
        print(' '.join(map(str, range(1, k+1))))
        return
    
    # Try combinations for small k
    if k <= 20:  # Heuristic threshold
        from itertools import combinations
        for combo in combinations(range(1, n+1), k):
            if is_independent(combo):
                print("YES")
                print(' '.join(map(str, combo)))
                return
        print("NO")
        return
    else:
        # For large k, maybe there's no solution or we need a different approach
        # Let's still try some heuristics
        # Greedy: pick nodes with minimum degree not adjacent to already picked
        used = [False] * (n+1)
        selected = []
        
        # Sort nodes by degree
        degrees = [(len(adj[i]), i) for i in range(1, n+1)]
        degrees.sort()
        
        for _, node in degrees:
            if len(selected) == k:
                break
            # Check if node is not adjacent to any in selected
            conflict = False
            for u in selected:
                if u in adj[node]:
                    conflict = True
                    break
            if not conflict:
                selected.append(node)
                
        if len(selected) >= k:
            print("YES")
            print(' '.join(map(str, selected[:k])))
            return
            
        # Try reverse order
        selected = []
        degrees.sort(reverse=True)
        for _, node in degrees:
            if len(selected) == k:
                break
            conflict = False
            for u in selected:
                if u in adj[node]:
                    conflict = True
                    break
            if not conflict:
                selected.append(node)
                
        if len(selected) >= k:
            print("YES")
            print(' '.join(map(str, selected[:k])))
            return
            
        # Last resort: try random sampling
        import random
        random.seed(42)
        for _ in range(10000):
            sample = random.sample(range(1, n+1), k)
            if is_independent(sample):
                print("YES")
                print(' '.join(map(str, sample)))
                return
                
        print("NO")
        return

solve()