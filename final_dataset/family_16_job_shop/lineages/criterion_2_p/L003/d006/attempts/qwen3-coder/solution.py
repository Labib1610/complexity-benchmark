import sys
import threading

def main():
    import sys
    sys.setrecursionlimit(1 << 25)
    
    j = int(sys.stdin.readline())
    tiles = []
    for _ in range(j):
        p1, p2 = map(int, sys.stdin.readline().split())
        tiles.append((p1, p2))
    
    # Binary search on the answer
    def can_achieve_max_cost(max_cost):
        # We want to check if there exists an arrangement such that 
        # the maximum path cost is <= max_cost
        
        # For each tile (p1, p2), if we place it at position i,
        # and the adversary goes down at column i, the path cost is:
        # prefix_sum_top[0..i-1] + p1 + p2 + suffix_sum_bottom[i+1..j-1]
        # We want this to be <= max_cost
        
        # But actually, let's think differently.
        # Let’s sort the tiles based on (p1 - p2) in descending order.
        # This is a classic strategy for this type of problem.
        
        # However, let's approach this more systematically.
        # The key insight is to binary search on the answer.
        # Given a max_cost, can we arrange the tiles so that all possible paths have cost <= max_cost?
        
        # There are j possible paths (going down at column 1, 2, ..., j).
        # Path i (1-indexed): goes right from (1,1) to (1,i), then down to (2,i), then right to (2,j)
        # Cost = sum(top[0..i-1]) + sum(bottom[i..j-1])
        #      = PrefixTop[i-1] + (TotalBottom - PrefixBottom[i-1])
        #      = PrefixTop[i-1] + TotalBottom - PrefixBottom[i-1]
        
        # So for each path i (1-based), we need:
        # PrefixTop[i-1] + TotalBottom - PrefixBottom[i-1] <= max_cost
        # Which is equivalent to:
        # PrefixTop[i-1] - PrefixBottom[i-1] <= max_cost - TotalBottom
        
        total_bottom = sum(tile[1] for tile in tiles)
        target = max_cost - total_bottom
        
        # Now, we want to arrange tiles to minimize max(PrefixTop[i-1] - PrefixBottom[i-1]) over all i
        # This is exactly the problem of minimizing the prefix max of (p1 - p2)
        # The optimal way is to sort tiles by (p1 - p2) in ascending order
        
        # But wait, that's not quite right. We want to minimize the maximum of those prefix differences.
        # Actually, let's reframe.
        
        # If we sort tiles by (p1 - p2) in ascending order, then the maximum of 
        # (PrefixTop[k] - PrefixBottom[k]) for k=0..j-1 is minimized.
        
        # But our paths are indexed by where we go down. Path i (1-based) has cost:
        # PrefixTop[i-1] + (TotalBottom - PrefixBottom[i-1])
        # So we want to minimize max_{i=1..j} (PrefixTop[i-1] - PrefixBottom[i-1])
        
        # Sorting tiles by (p1 - p2) ascending does minimize this maximum prefix difference.
        
        sorted_tiles = sorted(tiles, key=lambda x: x[0] - x[1])
        
        prefix_top = 0
        prefix_bottom = 0
        max_diff = float('-inf')
        
        for p1, p2 in sorted_tiles:
            prefix_top += p1
            prefix_bottom += p2
            diff = prefix_top - prefix_bottom
            if diff > max_diff:
                max_diff = diff
                
        # The maximum path cost for this arrangement is max_diff + total_bottom
        return max_diff + total_bottom <= max_cost
    
    # Binary search bounds
    low = min(tile[0] + tile[1] for tile in tiles)  # At least one path
    high = sum(tile[0] + tile[1] for tile in tiles)  # All paths if arranged worst
    
    while low < high:
        mid = (low + high) // 2
        if can_achieve_max_cost(mid):
            high = mid
        else:
            low = mid + 1
            
    print(low)

threading.Thread(target=main).start()