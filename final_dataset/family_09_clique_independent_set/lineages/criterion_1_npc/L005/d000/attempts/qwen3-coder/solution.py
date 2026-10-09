import sys
from itertools import combinations

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    
    conflicts = []
    idx = 3
    for _ in range(m):
        u = int(data[idx]) - 1  # Convert to 0-based indexing
        v = int(data[idx+1]) - 1
        conflicts.append((u, v))
        idx += 2
    
    # If k is 1, we can always pick any employee if n >=1
    if k == 1:
        print("YES")
        print("1")
        return
    
    # Build adjacency list to represent conflicts
    adj = [set() for _ in range(n)]
    for u, v in conflicts:
        adj[u].add(v)
        adj[v].add(u)
    
    # For small n (n <= 46), we can try all combinations up to a certain point
    # But since n can be up to 46, trying all C(n,k) combinations is too slow for large k
    # We'll use a meet-in-the-middle approach for larger n
    
    # However, given constraints, let's proceed with a smart brute-force:
    # Since n <= 46, and we're looking for k elements, if k <= 23,
    # we can iterate through combinations efficiently.
    # For k > 23, we can instead look for the complement (n-k) elements to exclude.
    
    def is_independent(nodes):
        for i in range(len(nodes)):
            for j in range(i+1, len(nodes)):
                if nodes[j] in adj[nodes[i]]:
                    return False
        return True
    
    # Special case when k is small enough to enumerate combinations directly
    if k <= min(23, n):
        # Try all combinations of k elements
        for comb in combinations(range(n), k):
            if is_independent(comb):
                print("YES")
                print(' '.join(str(x+1) for x in comb))
                return
        print("NO")
        return
    else:
        # When k is large, it's more efficient to find a set of (n-k) nodes to remove
        # i.e., find a subset of size (n-k) that is independent, then the rest form a valid committee
        complement_size = n - k
        if complement_size <= 23:
            for comb in combinations(range(n), complement_size):
                if is_independent(comb):
                    # The remaining nodes form a valid committee
                    remaining = set(range(n)) - set(comb)
                    print("YES")
                    print(' '.join(str(x+1) for x in sorted(remaining)))
                    return
            print("NO")
            return
        else:
            # This case should not happen because n<=46 and k>=1
            # So complement_size = n - k <= 45
            # But just in case, we handle it
            # We can still enumerate combinations of size k, even if large
            # But it's computationally intensive
            # Let's try a different approach: backtracking with pruning
            
            # Build the complement graph: edges exist where there was NO conflict
            # Then finding a clique of size k in original graph = finding an independent set of size k
            # Which is same as finding a clique of size k in the complement graph
            
            # Complement adjacency list
            comp_adj = [set(range(n)) for _ in range(n)]
            for i in range(n):
                comp_adj[i].discard(i)
            for u, v in conflicts:
                comp_adj[u].discard(v)
                comp_adj[v].discard(u)
            
            # Now we need to find a clique of size k in comp_adj
            # Use Bron-Kerbosch algorithm or similar, but for fixed size
            
            # For efficiency, let's stick to combination enumeration with early pruning
            # Even for k up to 46, but since k + (n-k) = n, at least one is <=23
            
            # Since we already handled k<=23 above, now we have k>23 => n-k<23
            # So the else branch above should have been executed
            # But let's ensure correctness
            
            # Re-examine: if k >23, then n-k <23, so we can enumerate combinations of size n-k
            # Already handled above. So this else is just fallback
            print("NO") # Should not reach here for valid inputs

if __name__ == "__main__":
    main()