from itertools import combinations
import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    
    # Read conflicts
    conflicts = set()
    idx = 3
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        idx += 2
        conflicts.add((min(u,v), max(u,v)))
    
    # If k is 1, just pick any channel
    if k == 1:
        print("YES")
        print(1)
        return
    
    # If k > n, impossible
    if k > n:
        print("NO")
        return
    
    # Generate all combinations of k channels
    # For efficiency, we'll use a meet-in-the-middle approach for larger n
    if n <= 23:
        # Brute force for small n
        for combo in combinations(range(1, n+1), k):
            valid = True
            for u, v in combinations(combo, 2):
                if (u, v) in conflicts:
                    valid = False
                    break
            if valid:
                print("YES")
                print(' '.join(map(str, combo)))
                return
        print("NO")
        return
    
    # For larger n, use meet-in-the-middle
    # Split channels into two halves
    mid = n // 2
    left_channels = list(range(1, mid+1))
    right_channels = list(range(mid+1, n+1))
    
    # Precompute conflicts for left and right separately
    left_conflicts = set()
    right_conflicts = set()
    cross_conflicts = {}
    
    for u, v in conflicts:
        if u <= mid and v <= mid:
            left_conflicts.add((u, v))
        elif u > mid and v > mid:
            right_conflicts.add((u - mid, v - mid))  # reindex to 1-based in right
        else:
            # Cross conflict
            if u > v:
                u, v = v, u
            if u not in cross_conflicts:
                cross_conflicts[u] = set()
            cross_conflicts[u].add(v)
    
    # Generate all valid subsets for left and right
    left_valid = {}
    right_valid = {}
    
    # Left subsets
    for i in range(0, min(k+1, mid+1)):
        for combo in combinations(left_channels, i):
            # Check if combo is valid
            valid = True
            for u, v in combinations(combo, 2):
                if (min(u,v), max(u,v)) in left_conflicts:
                    valid = False
                    break
            if valid:
                left_valid[combo] = True
    
    # Right subsets
    for i in range(0, min(k+1, n-mid+1)):
        for combo in combinations(range(1, len(right_channels)+1), i):  # 1-indexed in right
            # Check if combo is valid
            valid = True
            for u, v in combinations(combo, 2):
                if (u, v) in right_conflicts:
                    valid = False
                    break
            if valid:
                # Convert back to actual channel numbers
                actual_combo = tuple(right_channels[x-1] for x in combo)
                right_valid[actual_combo] = True
    
    # Now check all combinations of left and right subsets
    for left_size in range(0, k+1):
        right_size = k - left_size
        if right_size < 0:
            continue
            
        # Get all valid left subsets of size left_size
        left_subsets = [combo for combo in combinations(left_channels, left_size) if combo in left_valid]
        # Get all valid right subsets of size right_size
        right_subsets = [combo for combo in combinations(right_channels, right_size) if combo in right_valid]
        
        for left_combo in left_subsets:
            for right_combo in right_subsets:
                # Check cross conflicts
                valid = True
                for u in left_combo:
                    if u in cross_conflicts:
                        for v in right_combo:
                            if v in cross_conflicts[u]:
                                valid = False
                                break
                        if not valid:
                            break
                if valid:
                    result = list(left_combo) + list(right_combo)
                    print("YES")
                    print(' '.join(map(str, result)))
                    return
    
    print("NO")

if __name__ == "__main__":
    main()