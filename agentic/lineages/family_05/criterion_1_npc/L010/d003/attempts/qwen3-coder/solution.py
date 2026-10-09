from itertools import permutations

def solve():
    k, t = map(int, input().split())
    
    if t < k:
        print("NO")
        return
    
    protocols = []
    for _ in range(t):
        x, y, z = map(int, input().split())
        protocols.append((x, y, z))
    
    # Try all possible combinations of k protocols
    from itertools import combinations
    
    for combo in combinations(protocols, k):
        # Check if all x, y, z values are unique
        x_vals = [p[0] for p in combo]
        y_vals = [p[1] for p in combo]
        z_vals = [p[2] for p in combo]
        
        if len(set(x_vals)) == k and len(set(y_vals)) == k and len(set(z_vals)) == k:
            print("YES")
            for protocol in combo:
                print(protocol[0], protocol[1], protocol[2])
            return
    
    print("NO")

solve()