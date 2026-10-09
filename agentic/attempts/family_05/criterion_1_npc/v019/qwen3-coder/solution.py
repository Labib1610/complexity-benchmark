import sys
from itertools import combinations

def solve():
    k, t = map(int, input().split())
    
    if t < k:
        print("NO")
        return
    
    blocks = []
    for _ in range(t):
        x, y, z = map(int, input().split())
        blocks.append((x, y, z))
    
    # Try all combinations of k blocks
    for combo in combinations(blocks, k):
        shapes = set()
        colors = set()
        materials = set()
        
        valid = True
        for x, y, z in combo:
            if x in shapes or y in colors or z in materials:
                valid = False
                break
            shapes.add(x)
            colors.add(y)
            materials.add(z)
        
        if valid and len(shapes) == k and len(colors) == k and len(materials) == k:
            print("YES")
            for block in combo:
                print(block[0], block[1], block[2])
            return
    
    print("NO")

solve()