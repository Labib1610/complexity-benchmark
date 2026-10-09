from itertools import combinations
import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    
    edges = []
    idx = 3
    for _ in range(m):
        u = int(data[idx]) - 1
        v = int(data[idx+1]) - 1
        edges.append((u, v))
        idx += 2
    
    # If no edges, any combination works
    if m == 0:
        print("YES")
        print(' '.join(map(str, range(1, k+1))))
        return
    
    # For small n, we can check all combinations
    # But n can be up to 46, so we need a better approach
    # Let's use meet-in-the-middle for larger n
    
    if n <= 25:
        # Brute force: check all combinations of k sensors
        for combo in combinations(range(n), k):
            # Check if this combination is clean
            valid = True
            for u, v in edges:
                if u in combo and v in combo:
                    valid = False
                    break
            if valid:
                print("YES")
                print(' '.join(map(str, [x+1 for x in combo])))
                return
        print("NO")
    else:
        # Use meet-in-the-middle approach
        mid = n // 2
        left_nodes = list(range(mid))
        right_nodes = list(range(mid, n))
        
        # Precompute all valid subsets for the left half
        left_valid = {}
        for i in range(min(k+1, 1 << mid)):
            subset = []
            count = 0
            for j in range(mid):
                if i & (1 << j):
                    subset.append(j)
                    count += 1
            if count <= k:
                # Check if this subset is valid (no edges within)
                valid = True
                for u, v in edges:
                    if u in subset and v in subset:
                        valid = False
                        break
                if valid:
                    left_valid[i] = set(subset)
        
        # Precompute all valid subsets for the right half
        right_valid = {}
        for i in range(min(k+1, 1 << (n - mid))):
            subset = []
            count = 0
            for j in range(n - mid):
                if i & (1 << j):
                    subset.append(j + mid)
                    count += 1
            if count <= k:
                # Check if this subset is valid (no edges within)
                valid = True
                for u, v in edges:
                    if u in subset and v in subset:
                        valid = False
                        break
                if valid:
                    right_valid[i] = set(subset)
        
        # Now check all combinations of left and right subsets
        for left_mask, left_set in left_valid.items():
            left_size = len(left_set)
            if left_size > k:
                continue
            needed = k - left_size
            
            for right_mask, right_set in right_valid.items():
                right_size = len(right_set)
                if right_size != needed:
                    continue
                
                # Check if there are no edges between left and right
                valid = True
                for u, v in edges:
                    if (u in left_set and v in right_set) or (u in right_set and v in left_set):
                        valid = False
                        break
                
                if valid:
                    result = list(left_set) + list(right_set)
                    print("YES")
                    print(' '.join(map(str, [x+1 for x in result])))
                    return
        
        print("NO")

if __name__ == "__main__":
    main()