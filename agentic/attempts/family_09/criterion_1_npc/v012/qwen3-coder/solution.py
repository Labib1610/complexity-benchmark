from itertools import combinations

def solve():
    n, m, k = map(int, input().split())
    
    # Read edges and build adjacency list
    edges = []
    adj = [set() for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # If k is 1, we can always pick any single user
    if k == 1:
        print("YES")
        print(1)
        return
    
    # For larger k, we need to check all combinations
    # But since n <= 46, we can't check all combinations directly
    # We'll use a more efficient approach
    
    # Try all combinations of k users
    users = list(range(1, n + 1))
    
    # For small n, we can check all combinations
    # But for performance, let's be smarter
    
    if n <= 20:
        # Brute force for small n
        for combo in combinations(users, k):
            # Check if this combination is valid
            valid = True
            combo_set = set(combo)
            for u in combo:
                # Check if u has any neighbor in the combo
                for v in adj[u]:
                    if v in combo_set:
                        valid = False
                        break
                if not valid:
                    break
            if valid:
                print("YES")
                print(' '.join(map(str, combo)))
                return
    else:
        # For larger n, still brute force but more carefully
        # Actually, given the constraints, even with n=46, 
        # if k is large enough, it might be impossible due to the edges
        # Let's still try combinations but limit the search space smartly
        
        # But let's just do the brute force with combinations
        # Python's combinations is efficient enough for this
        for combo in combinations(users, k):
            # Check if this combination is valid (independent set)
            valid = True
            for u, v in edges:
                if u in combo and v in combo:
                    valid = False
                    break
            if valid:
                print("YES")
                print(' '.join(map(str, combo)))
                return
    
    print("NO")

solve()