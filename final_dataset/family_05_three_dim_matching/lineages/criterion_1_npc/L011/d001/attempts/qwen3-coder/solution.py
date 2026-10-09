import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    k = int(data[0])
    t = int(data[1])
    
    vectors = []
    index = 2
    for _ in range(t):
        x = int(data[index])
        y = int(data[index+1])
        z = int(data[index+2])
        vectors.append((x, y, z))
        index += 3
    
    # We need to find a subset of k vectors such that each x, y, z in 1..k appears exactly once
    # This is essentially finding a perfect matching in a 3-dimensional bipartite graph
    # We can model this as a matching problem and use backtracking with pruning
    
    # Build a mapping from x to list of (y,z) pairs
    x_map = defaultdict(list)
    y_map = defaultdict(list)
    z_map = defaultdict(list)
    
    for i, (x, y, z) in enumerate(vectors):
        x_map[x].append((y, z, i))
        y_map[y].append((x, z, i))
        z_map[z].append((x, y, i))
    
    # We'll use backtracking: try to assign each x from 1 to k
    used_y = [False] * (k + 1)
    used_z = [False] * (k + 1)
    selected = []
    selected_indices = []
    
    def backtrack(x_index):
        if x_index == k + 1:
            return True
        
        for y, z, idx in x_map.get(x_index, []):
            if not used_y[y] and not used_z[z]:
                used_y[y] = True
                used_z[z] = True
                selected.append((x_index, y, z))
                selected_indices.append(idx)
                
                if backtrack(x_index + 1):
                    return True
                
                used_y[y] = False
                used_z[z] = False
                selected.pop()
                selected_indices.pop()
        
        return False
    
    if backtrack(1):
        print("YES")
        for vec in selected:
            print(vec[0], vec[1], vec[2])
    else:
        print("NO")

if __name__ == "__main__":
    main()