from collections import defaultdict
import sys

def solve():
    q, t = map(int, input().split())
    clusters = []
    for _ in range(t):
        a, b, c = map(int, input().split())
        clusters.append((a, b, c))
    
    if t == 0:
        if q == 0:
            print("YES")
        else:
            print("NO")
        return
    
    # Build graph: each cluster is a node, edges connect clusters sharing crystals
    # This is actually a matching problem - we want to select q clusters that don't share any crystals
    
    # Try all combinations using backtracking
    def backtrack(index, selected, used_crystals):
        if len(selected) == q:
            return selected[:]
        
        if index >= t:
            return None
            
        # Try not taking current cluster
        result = backtrack(index + 1, selected, used_crystals)
        if result is not None:
            return result
            
        # Try taking current cluster if possible
        a, b, c = clusters[index]
        if a not in used_crystals and b not in used_crystals and c not in used_crystals:
            used_crystals.add(a)
            used_crystals.add(b)
            used_crystals.add(c)
            selected.append(index)
            
            result = backtrack(index + 1, selected, used_crystals)
            
            selected.pop()
            used_crystals.remove(a)
            used_crystals.remove(b)
            used_crystals.remove(c)
            
            if result is not None:
                return result
        
        return None
    
    # Optimization: if q*3 > 3*q (total crystals), impossible
    total_crystals = 3 * q
    if q * 3 > total_crystals:
        print("NO")
        return
    
    result = backtrack(0, [], set())
    
    if result is not None:
        print("YES")
        for idx in result:
            a, b, c = clusters[idx]
            print(a, b, c)
    else:
        print("NO")

solve()