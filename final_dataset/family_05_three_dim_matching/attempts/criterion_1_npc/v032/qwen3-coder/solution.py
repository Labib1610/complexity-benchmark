from itertools import permutations

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    k = int(data[0])
    t = int(data[1])
    
    routes = []
    idx = 2
    for _ in range(t):
        x = int(data[idx])
        y = int(data[idx+1])
        z = int(data[idx+2])
        routes.append((x, y, z))
        idx += 3
    
    # Try all permutations of k routes
    for perm in permutations(range(t), k):
        selected_routes = [routes[i] for i in perm]
        
        # Check if sources, transformers, and destinations are all unique
        sources = [r[0] for r in selected_routes]
        transformers = [r[1] for r in selected_routes]
        destinations = [r[2] for r in selected_routes]
        
        if len(set(sources)) == k and len(set(transformers)) == k and len(set(destinations)) == k:
            print("YES")
            for r in selected_routes:
                print(r[0], r[1], r[2])
            return
    
    print("NO")

solve()