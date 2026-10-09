from collections import defaultdict
import sys

def solve():
    k, t = map(int, input().split())
    
    if t < k:
        print("NO")
        return
    
    pockets = []
    for _ in range(t):
        x, y, z = map(int, input().split())
        pockets.append((x, y, z))
    
    # Try all combinations of k pockets out of t
    # Since k <= 22 and t <= k^3, we can use backtracking with pruning
    
    def backtrack(index, selected, depths, latitudes, longitudes):
        # Pruning: if we already have enough to cover all coordinates, but not enough slots
        if len(selected) + (t - index) < k:
            return None
            
        if len(selected) == k:
            # Check if all coordinates are covered
            if len(depths) == k and len(latitudes) == k and len(longitudes) == k:
                return selected[:]
            else:
                return None
        
        # If remaining positions cannot cover missing coordinates, prune
        missing_depths = k - len(depths)
        missing_lats = k - len(latitudes)
        missing_longs = k - len(longitudes)
        
        if len(selected) + (t - index) < k:
            return None
            
        # Try including current pocket
        if index < t:
            x, y, z = pockets[index]
            new_depths = depths | {x}
            new_latitudes = latitudes | {y}
            new_longitudes = longitudes | {z}
            
            # Only proceed if this pocket adds new coverage or we have room
            if (len(new_depths) > len(depths) or 
                len(new_latitudes) > len(latitudes) or 
                len(new_longitudes) > len(longitudes) or
                (len(selected) + (t-index) >= k and 
                 len(new_depths) >= k and len(new_latitudes) >= k and len(new_longitudes) >= k)):
                
                selected.append(pockets[index])
                result = backtrack(index + 1, selected, new_depths, new_latitudes, new_longitudes)
                if result is not None:
                    return result
                selected.pop()
            
            # Try not including current pocket
            result = backtrack(index + 1, selected, depths, latitudes, longitudes)
            if result is not None:
                return result
                
        return None
    
    # Optimized approach: try greedy selection first
    # For small k, we can try a more direct approach
    
    from itertools import combinations
    
    # For larger inputs, let's use a smarter approach
    if k <= 10 or (k <= 15 and t <= 200):
        # Try combinations directly
        for combo in combinations(range(t), k):
            depths = set()
            latitudes = set()
            longitudes = set()
            
            for i in combo:
                x, y, z = pockets[i]
                depths.add(x)
                latitudes.add(y)
                longitudes.add(z)
            
            if len(depths) == k and len(latitudes) == k and len(longitudes) == k:
                print("YES")
                for i in combo:
                    print(pockets[i][0], pockets[i][1], pockets[i][2])
                return
    
    # For other cases, use backtracking with better pruning
    else:
        result = backtrack(0, [], set(), set(), set())
        if result is not None:
            print("YES")
            for pocket in result:
                print(pocket[0], pocket[1], pocket[2])
            return
    
    print("NO")

solve()