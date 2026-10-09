from itertools import combinations

def solve():
    n, m, k = map(int, input().split())
    
    # Build adjacency list
    adj = [set() for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].add(v)
        adj[v].add(u)
    
    # Generate all combinations of k members
    for combo in combinations(range(1, n + 1), k):
        # Check if this combination forms a valid unassociated panel
        valid = True
        for i in range(k):
            for j in range(i + 1, k):
                if combo[j] in adj[combo[i]]:
                    valid = False
                    break
            if not valid:
                break
        
        if valid:
            print("YES")
            print(*combo)
            return
    
    print("NO")

solve()