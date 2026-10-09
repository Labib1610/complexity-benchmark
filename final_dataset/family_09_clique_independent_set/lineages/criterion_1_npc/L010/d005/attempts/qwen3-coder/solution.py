from itertools import combinations

def solve():
    n, m, k = map(int, input().split())
    edges = []
    degree = [0] * (n + 1)
    
    for _ in range(m):
        u, v = map(int, input().split())
        edges.append((u, v))
        degree[u] += 1
        degree[v] += 1
    
    # Try all combinations of k upgraded modules
    for upgraded in combinations(range(1, n + 1), k):
        upgraded_set = set(upgraded)
        standard = [i for i in range(1, n + 1) if i not in upgraded_set]
        
        # Count edges between standard modules
        standard_edges = 0
        for u, v in edges:
            if u in standard and v in standard:
                standard_edges += 1
        
        # Calculate sum of degrees of standard modules
        degree_sum = sum(degree[i] for i in standard)
        
        # Check stability condition
        if standard_edges == degree_sum - m:
            print("YES")
            print(*upgraded)
            return
    
    print("NO")

solve()