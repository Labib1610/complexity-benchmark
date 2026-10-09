from collections import defaultdict

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    k = int(data[0])
    t = int(data[1])
    
    triples = []
    idx = 2
    for _ in range(t):
        x = int(data[idx])
        y = int(data[idx+1])
        z = int(data[idx+2])
        triples.append((x, y, z))
        idx += 3
    
    # Build a graph for matching
    # We can model this as a 3D matching problem
    # Use backtracking with pruning
    
    # Try to find a perfect matching
    # Each element in X, Y, Z should be used exactly once
    
    used_x = [False] * (k + 1)
    used_y = [False] * (k + 1)
    used_z = [False] * (k + 1)
    selected = []
    
    def backtrack(i):
        if len(selected) == k:
            return True
            
        if i == t:
            return False
            
        # Try including this triple
        x, y, z = triples[i]
        if not used_x[x] and not used_y[y] and not used_z[z]:
            used_x[x] = True
            used_y[y] = True
            used_z[z] = True
            selected.append(triples[i])
            
            if backtrack(i + 1):
                return True
                
            used_x[x] = False
            used_y[y] = False
            used_z[z] = False
            selected.pop()
        
        # Try not including this triple
        if backtrack(i + 1):
            return True
            
        return False
    
    if backtrack(0):
        print("YES")
        for triple in selected:
            print(triple[0], triple[1], triple[2])
    else:
        print("NO")

solve()