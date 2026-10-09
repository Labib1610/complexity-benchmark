from itertools import permutations

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    k = int(data[0])
    t = int(data[1])
    
    pathways = []
    idx = 2
    for _ in range(t):
        x = int(data[idx])
        y = int(data[idx+1])
        z = int(data[idx+2])
        pathways.append((x, y, z))
        idx += 3
    
    # Try all permutations of k pathways
    # Since k <= 22, and we need to choose k out of t, this could be huge
    # However, since we're looking for a matching where each layer element appears once,
    # we can model this as a bipartite matching or use backtracking
    
    # Let's try a backtracking approach
    # We want to pick k triplets such that all x, y, z are unique
    
    def backtrack(pos, used_x, used_y, used_z, current):
        if pos == k:
            return True
            
        for i in range(t):
            x, y, z = pathways[i]
            if x not in used_x and y not in used_y and z not in used_z:
                used_x.add(x)
                used_y.add(y)
                used_z.add(z)
                current.append(pathways[i])
                
                if backtrack(pos + 1, used_x, used_y, used_z, current):
                    return True
                    
                used_x.remove(x)
                used_y.remove(y)
                used_z.remove(z)
                current.pop()
                
        return False
    
    # Optimization: if t < k, impossible
    if t < k:
        print("NO")
        return
        
    used_x = set()
    used_y = set()
    used_z = set()
    current = []
    
    if backtrack(0, used_x, used_y, used_z, current):
        print("YES")
        for triplet in current:
            print(triplet[0], triplet[1], triplet[2])
    else:
        print("NO")

solve()