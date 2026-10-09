from collections import defaultdict

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    k = int(data[0])
    t = int(data[1])
    
    struts = []
    index = 2
    for _ in range(t):
        x = int(data[index])
        y = int(data[index+1])
        z = int(data[index+2])
        struts.append((x, y, z))
        index += 3
    
    # If k is 0, special case
    if k == 0:
        print("YES")
        return
    
    # If we don't have enough struts, impossible
    if t < k:
        print("NO")
        return
        
    # Build a graph for matching: we want a 3D matching where each x, y, z coordinate appears once
    # This is equivalent to finding a perfect matching in a 3-dimensional bipartite graph
    # We can model this as a maximum bipartite matching problem
    
    # However, since k <= 22, and we need exactly k struts with distinct x,y,z coords,
    # we can think of this as selecting k struts such that their x-coords are distinct,
    # y-coords are distinct, and z-coords are distinct.
    # This is like a 3D matching which can be reduced to finding a maximum matching in tripartite graph
    
    # But there's a simpler way: model it as a matching from X to Y to Z
    # Actually, let's think of it differently:
    # We want to select k points from the struts such that all x, y, z coords are distinct
    # This is equivalent to finding a system of distinct representatives for three partitions
    
    # Let's reduce it to a matching problem:
    # Create a tripartite graph with:
    # - Left nodes: x coordinates (1 to k)
    # - Middle nodes: y coordinates (1 to k)  
    # - Right nodes: z coordinates (1 to k)
    # For each strut (x,y,z), add edges x->y and y->z
    # We want to find k struts such that we get a perfect matching across all three parts
    
    # Even simpler approach: Try all combinations using backtracking with pruning
    # But with k up to 22, that's too large
    
    # Better approach: This is essentially a 3D matching problem which can be solved with
    # maximum flow or backtracking with pruning
    
    # Let's use a backtracking approach with bitmasks for efficiency
    
    # Map each coordinate to available struts
    x_struts = defaultdict(list)
    y_struts = defaultdict(list)
    z_struts = defaultdict(list)
    
    for i in range(t):
        x, y, z = struts[i]
        x_struts[x].append(i)
        y_struts[y].append(i)
        z_struts[z].append(i)
        
    # We'll use backtracking with pruning
    selected = []
    used_x = [False] * (k + 1)
    used_y = [False] * (k + 1)
    used_z = [False] * (k + 1)
    
    def backtrack(index):
        if len(selected) == k:
            return True
            
        if index >= t:
            return False
            
        # Pruning: if even selecting all remaining struts won't give us k, return False
        if len(selected) + (t - index) < k:
            return False
            
        # Try including current strut
        x, y, z = struts[index]
        if not used_x[x] and not used_y[y] and not used_z[z]:
            selected.append(index)
            used_x[x] = True
            used_y[y] = True
            used_z[z] = True
            
            if backtrack(index + 1):
                return True
                
            selected.pop()
            used_x[x] = False
            used_y[y] = False
            used_z[z] = False
            
        # Try not including current strut
        if backtrack(index + 1):
            return True
            
        return False
        
    # Optimization: sort struts to try "better" ones first
    # But for correctness, simple indexing works
    
    if backtrack(0):
        print("YES")
        for idx in selected:
            x, y, z = struts[idx]
            print(x, y, z)
    else:
        print("NO")

solve()