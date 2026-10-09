import sys

def solve():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    k = int(next(it))
    
    conflict = [0] * (n + 1)
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        conflict[u] |= 1 << (v - 1)
        conflict[v] |= 1 << (u - 1)
    
    # Convert to 0-indexed masks
    masks = [conflict[i+1] for i in range(n)]
    
    half = n // 2
    left_size = half
    right_size = n - half
    
    # Precompute popcount for numbers up to max(2^left_size, 2^right_size)
    max_size = max(left_size, right_size)
    popcount = [0] * (1 << max_size)
    for i in range(1, 1 << max_size):
        popcount[i] = popcount[i & (i - 1)] + 1
    
    # Process left half (vertices 0 to half-1)
    left_masks = masks[:half]
    left_conflict = [0] * (1 << left_size)
    left_conflict[0] = 0
    valid_left = [[] for _ in range(left_size + 1)]
    valid_left[0].append(0)
    
    for mask in range(1, 1 << left_size):
        lb = mask & -mask
        i = (lb.bit_length() - 1)
        prev = mask ^ lb
        left_conflict[mask] = left_conflict[prev] | left_masks[i]
        if left_conflict[mask] & mask == 0:
            valid_left[popcount[mask]].append(mask)
    
    # Process right half (vertices half to n-1)
    right_masks = masks[half:]
    right_conflict = [0] * (1 << right_size)
    right_conflict[0] = 0
    valid_right = [[] for _ in range(right_size + 1)]
    valid_right[0].append(0)
    
    for mask in range(1, 1 << right_size):
        lb = mask & -mask
        i = (lb.bit_length() - 1)
        prev = mask ^ lb
        right_conflict[mask] = right_conflict[prev] | right_masks[i]
        if right_conflict[mask] & mask == 0:
            valid_right[popcount[mask]].append(mask)
    
    # For each valid right mask, compute which left vertices are forbidden
    # right_forbidden[mask] = set of left vertices that conflict with any vertex in mask
    right_forbidden = [0] * (1 << right_size)
    for mask in range(1, 1 << right_size):
        lb = mask & -mask
        i = (lb.bit_length() - 1)
        prev = mask ^ lb
        # right_masks[i] contains conflicts with all vertices
        # We need only the left half part
        forbidden_by_i = right_masks[i] & ((1 << half) - 1)
        right_forbidden[mask] = right_forbidden[prev] | forbidden_by_i
    
    # Try to find a solution
    for r_count in range(min(k, right_size) + 1):
        l_count = k - r_count
        if l_count < 0 or l_count > left_size:
            continue
        
        for r_mask in valid_right[r_count]:
            forbidden = right_forbidden[r_mask]
            for l_mask in valid_left[l_count]:
                if l_mask & forbidden == 0:
                    # Found solution
                    result = []
                    for i in range(left_size):
                        if l_mask & (1 << i):
                            result.append(i + 1)
                    for i in range(right_size):
                        if r_mask & (1 << i):
                            result.append(half + i + 1)
                    print("YES")
                    print(' '.join(map(str, result)))
                    return
    
    print("NO")

solve()