from itertools import combinations
import sys

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    
    constraints = []
    index = 3
    for _ in range(m):
        u = int(data[index]) - 1  # Convert to 0-based indexing
        v = int(data[index+1]) - 1
        constraints.append((u, v))
        index += 2
    
    # If k is 1, just pick any single module
    if k == 1:
        print("YES")
        print(1)
        return
    
    # For small n, we can check all combinations
    # But n can be up to 46, so we need a smarter approach
    # We'll use meet-in-the-middle for larger cases
    
    if n <= 25:
        # Brute force: check all combinations of k modules
        for combo in combinations(range(n), k):
            valid = True
            for u, v in constraints:
                if u in combo and v in combo:
                    valid = False
                    break
            if valid:
                print("YES")
                print(' '.join(str(x + 1) for x in combo))
                return
        print("NO")
    else:
        # Meet-in-the-middle approach
        mid = n // 2
        left_nodes = list(range(mid))
        right_nodes = list(range(mid, n))
        
        # Generate all valid subsets of left part
        left_valid = {}
        for l_size in range(min(k+1, mid+1)):
            for subset in combinations(left_nodes, l_size):
                # Check if subset is valid internally
                valid_internal = True
                for u, v in constraints:
                    if u in subset and v in subset:
                        valid_internal = False
                        break
                if valid_internal:
                    mask = 0
                    for node in subset:
                        mask |= (1 << node)
                    left_valid[mask] = subset
        
        # Generate all valid subsets of right part
        right_valid = {}
        for r_size in range(min(k+1, len(right_nodes)+1)):
            for subset in combinations(right_nodes, r_size):
                # Check if subset is valid internally
                valid_internal = True
                for u, v in constraints:
                    if u in subset and v in subset:
                        valid_internal = False
                        break
                if valid_internal:
                    mask = 0
                    for node in subset:
                        mask |= (1 << (node - mid))
                    right_valid[mask] = subset
        
        # Now, check all pairs of left and right subsets
        for l_mask, l_subset in left_valid.items():
            l_size = len(l_subset)
            r_needed = k - l_size
            if r_needed < 0 or r_needed > len(right_nodes):
                continue
            
            # For each combination of r_needed nodes from right
            for r_subset in combinations(right_nodes, r_needed):
                # Check if r_subset is valid internally
                valid_internal = True
                for u, v in constraints:
                    if u in r_subset and v in r_subset:
                        valid_internal = False
                        break
                if not valid_internal:
                    continue
                
                # Check if no edge between l_subset and r_subset
                conflict = False
                for u, v in constraints:
                    if (u in l_subset and v in r_subset) or (u in r_subset and v in l_subset):
                        conflict = True
                        break
                if not conflict:
                    result = list(l_subset) + list(r_subset)
                    print("YES")
                    print(' '.join(str(x + 1) for x in result))
                    return
        
        print("NO")

if __name__ == "__main__":
    main()