from itertools import combinations

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    
    edges = []
    idx = 3
    for _ in range(m):
        u = int(data[idx]) - 1  # Convert to 0-indexed
        v = int(data[idx+1]) - 1
        edges.append((u, v))
        idx += 2
    
    # Special case: if k == n, we power all pins, so every edge must have at least one unpowered pin, which is impossible
    if k == n:
        if m == 0:
            print("YES")
            print(" ".join(str(i) for i in range(1, n+1)))
            return
        else:
            print("NO")
            return
            
    # For small n, try all combinations
    if n <= 20:
        for combo in combinations(range(n), k):
            valid = True
            for u, v in edges:
                if u in combo and v in combo:
                    valid = False
                    break
            if valid:
                print("YES")
                print(" ".join(str(x + 1) for x in combo))
                return
        print("NO")
        return
    
    # For larger n, use a more efficient approach with bitsets
    # We'll use a meet-in-the-middle approach since n <= 46
    
    mid = n // 2
    left_pins = list(range(mid))
    right_pins = list(range(mid, n))
    
    # Generate all valid subsets of left side
    left_valid = {}
    for lsize in range(min(k+1, len(left_pins)+1)):
        for left_combo in combinations(left_pins, lsize):
            # Check if this subset violates any constraints
            valid_subset = True
            for u, v in edges:
                if u in left_combo and v in left_combo:
                    valid_subset = False
                    break
            if valid_subset:
                mask = 0
                for x in left_combo:
                    mask |= (1 << x)
                left_valid[mask] = len(left_combo)
    
    # Generate all valid subsets of right side
    right_valid = {}
    for rsize in range(min(k+1, len(right_pins)+1)):
        for right_combo in combinations(right_pins, rsize):
            valid_subset = True
            for u, v in edges:
                if u in right_combo and v in right_combo:
                    valid_subset = False
                    break
            if valid_subset:
                mask = 0
                for x in right_combo:
                    mask |= (1 << (x - mid))
                right_valid[mask] = len(right_combo)
    
    # Now check all combinations of left and right parts
    for lmask, lcount in left_valid.items():
        if lcount > k:
            continue
        needed = k - lcount
        if needed < 0:
            continue
        # We need to find a right subset of size 'needed' that doesn't conflict with left
        for rmask, rcount in right_valid.items():
            if rcount != needed:
                continue
            # Check if combination is valid
            combined_valid = True
            for u, v in edges:
                u_in_left = u < mid
                v_in_left = v < mid
                u_bit = u if u_in_left else (u - mid)
                v_bit = v if v_in_left else (v - mid)
                
                u_selected = (lmask & (1 << u)) != 0 if u_in_left else (rmask & (1 << (u - mid))) != 0
                v_selected = (lmask & (1 << v)) != 0 if v_in_left else (rmask & (1 << (v - mid))) != 0
                
                if u_selected and v_selected:
                    combined_valid = False
                    break
            
            if combined_valid:
                result = []
                temp_mask = lmask
                while temp_mask:
                    bit = temp_mask & (-temp_mask)
                    pos = (bit.bit_length() - 1)
                    result.append(pos + 1)
                    temp_mask ^= bit
                
                temp_mask = rmask
                while temp_mask:
                    bit = temp_mask & (-temp_mask)
                    pos = (bit.bit_length() - 1)
                    result.append(pos + mid + 1)
                    temp_mask ^= bit
                
                print("YES")
                print(" ".join(map(str, sorted(result))))
                return
    
    print("NO")

solve()