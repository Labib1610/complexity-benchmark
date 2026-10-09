def solve():
    import sys
    from collections import defaultdict
    
    n, m = map(int, sys.stdin.readline().split())
    
    if m == 0:
        print("YES")
        print(" ".join(["1"] * n))
        return
    
    # Build adjacency list
    adj = defaultdict(list)
    edges = []
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
        edges.append((u, v))
    
    # Try all 3^n assignments
    for mask in range(3**n):
        # Extract frequencies
        freq = [0] * (n + 1)
        temp_mask = mask
        valid = True
        for i in range(1, n + 1):
            freq[i] = (temp_mask % 3) + 1
            temp_mask //= 3
        
        # Check all constraints
        for u, v in edges:
            if abs(freq[u] - freq[v]) == 0:
                valid = False
                break
        
        if valid:
            print("YES")
            print(" ".join(map(str, freq[1:])))
            return
    
    print("NO")

solve()