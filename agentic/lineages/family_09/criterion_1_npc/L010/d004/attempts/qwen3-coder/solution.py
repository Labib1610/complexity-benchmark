from itertools import combinations

def solve():
    n, m, k = map(int, input().split())
    
    # Build adjacency list and degree count
    adj = [[] for _ in range(n + 1)]
    degree = [0] * (n + 1)
    
    edges = []
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)
        adj[v].append(u)
        degree[u] += 1
        degree[v] += 1
        edges.append((u, v))
    
    # Try all combinations of k modules
    for upgraded in combinations(range(1, n + 1), k):
        upgraded_set = set(upgraded)
        
        # Calculate sum of degrees of upgraded modules
        sum_degrees = sum(degree[i] for i in upgraded)
        
        # Count asymmetric edges
        asymmetric_count = 0
        for u, v in edges:
            if (u in upgraded_set) != (v in upgraded_set):  # XOR
                asymmetric_count += 1
        
        if asymmetric_count == sum_degrees:
            print("YES")
            print(*upgraded)
            return
    
    print("NO")

solve()