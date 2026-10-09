from itertools import combinations

def solve():
    k, t = map(int, input().split())
    
    if k == 0:
        print("YES")
        return
    
    if t < k:
        print("NO")
        return
    
    candidates = []
    for _ in range(t):
        x, y, z = map(int, input().split())
        candidates.append((x, y, z))
    
    # Try all combinations of k candidates
    for combo in combinations(candidates, k):
        # Check if this combination satisfies all constraints
        freqs = set()
        keys = set()
        pols = set()
        
        valid = True
        for x, y, z in combo:
            if x in freqs or y in keys or z in pols:
                valid = False
                break
            freqs.add(x)
            keys.add(y)
            pols.add(z)
        
        if valid:
            print("YES")
            for x, y, z in combo:
                print(x, y, z)
            return
    
    print("NO")

solve()