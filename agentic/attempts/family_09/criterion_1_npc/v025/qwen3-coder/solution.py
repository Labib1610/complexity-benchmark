from itertools import combinations

def solve():
    n, m, k = map(int, input().split())
    
    # Create adjacency list representation of the graph
    # where vertices are trajectories and edges represent collision risks
    graph = [[] for _ in range(n + 1)]
    edges = []
    
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
        edges.append((u, v))
    
    # If k is 1, we can always choose any single trajectory
    if k == 1:
        print("YES")
        print(1)
        return
    
    # If k is larger than n, it's impossible
    if k > n:
        print("NO")
        return
    
    # For the given constraints, we can use a brute-force approach
    # since n ≤ 46 and the structure is limited
    
    # Try all combinations of k trajectories
    for combo in combinations(range(1, n + 1), k):
        # Check if this combination is collision-free
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