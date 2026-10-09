import sys
from itertools import combinations

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    
    # Read the reactive pairs
    reactive = set()
    idx = 3
    for _ in range(m):
        u = int(data[idx])
        v = int(data[idx+1])
        if u > v:
            u, v = v, u
        reactive.add((u, v))
        idx += 2
    
    # If no reactive pairs, we can take any k markers
    if m == 0:
        print("YES")
        print(' '.join(map(str, range(1, k+1))))
        return
    
    # For small n, we can check all combinations
    if n <= 20:
        markers = list(range(1, n+1))
        for combo in combinations(markers, k):
            valid = True
            for u, v in combinations(combo, 2):
                if u > v:
                    u, v = v, u
                if (u, v) in reactive:
                    valid = False
                    break
            if valid:
                print("YES")
                print(' '.join(map(str, combo)))
                return
        print("NO")
        return
    
    # For larger n, use bit manipulation approach
    # Build adjacency list
    adj = [set() for _ in range(n+1)]
    for u, v in reactive:
        adj[u].add(v)
        adj[v].add(u)
    
    # Generate all subsets of size k using meet-in-the-middle for efficiency
    # Split markers into two halves
    mid = n // 2
    left_markers = list(range(1, mid+1))
    right_markers = list(range(mid+1, n+1))
    
    # Precompute all valid subsets for left half
    left_subsets = []
    for i in range(1 << len(left_markers)):
        subset = []
        for j in range(len(left_markers)):
            if i & (1 << j):
                subset.append(left_markers[j])
        if len(subset) > k:
            continue
        # Check if this subset is valid internally
        valid_internal = True
        for u, v in combinations(subset, 2):
            if u > v:
                u, v = v, u
            if (u, v) in reactive:
                valid_internal = False
                break
        if valid_internal:
            left_subsets.append((subset, i))
    
    # Precompute all valid subsets for right half
    right_subsets = []
    for i in range(1 << len(right_markers)):
        subset = []
        for j in range(len(right_markers)):
            if i & (1 << j):
                subset.append(right_markers[j])
        if len(subset) > k:
            continue
        # Check if this subset is valid internally
        valid_internal = True
        for u, v in combinations(subset, 2):
            if u > v:
                u, v = v, u
            if (u, v) in reactive:
                valid_internal = False
                break
        if valid_internal:
            right_subsets.append((subset, i))
    
    # Now, for each left subset of size s, look for a right subset of size k-s
    from collections import defaultdict
    left_by_size = defaultdict(list)
    for subset, mask in left_subsets:
        left_by_size[len(subset)].append((subset, mask))
        
    right_by_size = defaultdict(list)
    for subset, mask in right_subsets:
        right_by_size[len(subset)].append((subset, mask))
    
    # Check all combinations
    for s in range(k+1):
        left_list = left_by_size[s]
        right_list = right_by_size[k - s]
        for left_subset, left_mask in left_list:
            for right_subset, right_mask in right_list:
                # Combine the subsets
                combined = left_subset + right_subset
                if len(combined) != k:
                    continue
                # Check for cross-reactivity between left and right
                valid_cross = True
                for u in left_subset:
                    for v in right_subset:
                        if u > v:
                            u, v = v, u
                        if (u, v) in reactive:
                            valid_cross = False
                            break
                    if not valid_cross:
                        break
                if valid_cross:
                    print("YES")
                    print(' '.join(map(str, combined)))
                    return
                    
    print("NO")

if __name__ == "__main__":
    main()