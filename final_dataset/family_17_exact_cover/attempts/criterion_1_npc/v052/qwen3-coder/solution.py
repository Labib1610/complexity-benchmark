from collections import defaultdict
import sys

def solve():
    q, t = map(int, input().split())
    
    if t == 0:
        if q == 0:
            print("YES")
        else:
            print("NO")
        return
    
    blueprints = []
    for _ in range(t):
        a, b, c = map(int, input().split())
        blueprints.append((a, b, c))
    
    # Try all combinations of q blueprints
    # Since q <= 200 and t <= 20000, we need a more efficient approach
    
    # This is essentially a matching problem - we want to find q triplets
    # that cover all 3q elements exactly once
    
    # Use backtracking with pruning
    def backtrack(selected, used_relics, index):
        if len(selected) == q:
            return selected[:]
        
        if index >= t:
            return None
            
        # Pruning: if even selecting all remaining blueprints won't give us enough
        if len(selected) + (t - index) < q:
            return None
            
        # Try including current blueprint
        a, b, c = blueprints[index]
        if a not in used_relics and b not in used_relics and c not in used_relics:
            selected.append(index)
            used_relics.add(a)
            used_relics.add(b)
            used_relics.add(c)
            
            result = backtrack(selected, used_relics, index + 1)
            if result is not None:
                return result
                
            selected.pop()
            used_relics.remove(a)
            used_relics.remove(b)
            used_relics.remove(c)
        
        # Try not including current blueprint
        return backtrack(selected, used_relics, index + 1)
    
    # Optimization: preprocess to remove obviously bad choices
    # But let's just try a direct approach first
    
    result = backtrack([], set(), 0)
    
    if result is None:
        print("NO")
    else:
        print("YES")
        for idx in result:
            a, b, c = blueprints[idx]
            print(a, b, c)

solve()