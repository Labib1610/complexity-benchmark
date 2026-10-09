import sys
from itertools import permutations

def solve():
    input_data = sys.stdin.read().strip().split()
    if not input_data:
        return
    it = iter(input_data)
    k = int(next(it))
    t = int(next(it))
    
    blocks = []
    for _ in range(t):
        x = int(next(it))
        y = int(next(it))
        z = int(next(it))
        blocks.append((x, y, z))
    
    # If k is 1, just check if block (1,1,1) exists
    if k == 1:
        if (1,1,1) in blocks:
            print("YES")
            print("1 1 1")
        else:
            print("NO")
        return
    
    # For small k, we can try backtracking with pruning
    # We'll map each shape to possible colors and materials
    shape_to_blocks = [[] for _ in range(k+1)]
    for x,y,z in blocks:
        shape_to_blocks[x].append((y,z))
    
    # Check if any shape is missing
    for i in range(1,k+1):
        if not shape_to_blocks[i]:
            print("NO")
            return
    
    # Try to assign each shape a unique color and material
    used_color = [False]*(k+1)
    used_material = [False]*(k+1)
    chosen = [None]*(k+1)
    
    # Sort shapes by number of options (smallest first) for better pruning
    order = list(range(1,k+1))
    order.sort(key=lambda s: len(shape_to_blocks[s]))
    
    def dfs(idx):
        if idx == k:
            return True
        shape = order[idx]
        for y,z in shape_to_blocks[shape]:
            if not used_color[y] and not used_material[z]:
                used_color[y] = True
                used_material[z] = True
                chosen[shape] = (shape,y,z)
                if dfs(idx+1):
                    return True
                used_color[y] = False
                used_material[z] = False
        return False
    
    if dfs(0):
        print("YES")
        for s in range(1,k+1):
            print(*chosen[s])
    else:
        print("NO")

if __name__ == "__main__":
    solve()