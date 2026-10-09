from itertools import combinations

def main():
    n, m, k = map(int, input().split())
    
    # Read all edges (lock connections)
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u-1, v-1))  # Convert to 0-indexed
    
    # If k is 0, we don't need to select any process
    if k == 0:
        print("YES")
        return
    
    # If k is 1, we can always select any single process
    if k == 1:
        print("YES")
        print(1)
        return
    
    # Generate all possible combinations of k processes
    # Since n <= 46, we need to be smart about this
    # But given the constraints, a brute force on combinations should work
    # However, let's think of a better approach
    
    # Actually, let's try all combinations since k can be up to n, but n is up to 46
    # But the number of combinations can be huge. 
    # Let's use a more efficient approach by modeling this as a graph problem
    # We want to find an independent set of size k in the graph where edges represent conflicts
    
    # Build adjacency list for conflicts
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
    
    # Function to check if a set of nodes is independent
    def is_independent(nodes):
        node_set = set(nodes)
        for u in nodes:
            for v in adj[u]:
                if v in node_set:
                    return False
        return True
    
    # For small k, we can try all combinations
    # But for large n, this might be too slow
    # Let's try a meet-in-the-middle approach or other optimization
    
    # Since n <= 46, let's split into two halves
    mid = n // 2
    left_nodes = list(range(mid))
    right_nodes = list(range(mid, n))
    
    # Generate all independent sets for left half
    left_independent = {}
    for i in range(min(k+1, 2**mid)):
        # Generate subset using bitmask
        subset = []
        mask = i
        idx = 0
        temp_mask = mask
        while temp_mask:
            if temp_mask & 1:
                subset.append(left_nodes[idx])
            temp_mask >>= 1
            idx += 1
        
        if is_independent(subset):
            left_independent[i] = subset
    
    # Generate all independent sets for right half
    right_independent = {}
    for i in range(min(k+1, 2**(n-mid))):
        subset = []
        mask = i
        idx = 0
        temp_mask = mask
        while temp_mask:
            if temp_mask & 1:
                subset.append(right_nodes[idx])
            temp_mask >>= 1
            idx += 1
        
        if is_independent(subset):
            right_independent[i] = subset
    
    # Now check all pairs
    for l_mask, l_set in left_independent.items():
        for r_mask, r_set in right_independent.items():
            # Combine sets
            combined = l_set + r_set
            if len(combined) == k and is_independent(combined):
                print("YES")
                result = [str(x+1) for x in combined]
                print(" ".join(result))
                return
    
    # If that doesn't work, let's try a simpler approach for small n
    if n <= 25:
        # Try all combinations
        for combo in combinations(range(n), k):
            if is_independent(list(combo)):
                print("YES")
                result = [str(x+1) for x in combo]
                print(" ".join(result))
                return
    
    print("NO")

if __name__ == "__main__":
    main()