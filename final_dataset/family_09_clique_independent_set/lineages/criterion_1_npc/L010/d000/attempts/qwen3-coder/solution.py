import sys
from itertools import combinations

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    k = int(data[2])
    
    # Read edges
    edges = []
    index = 3
    for _ in range(m):
        u = int(data[index]) - 1  # Convert to 0-based
        v = int(data[index+1]) - 1
        edges.append((u, v))
        index += 2
    
    # If k is 1, we can always pick any single node
    if k == 1:
        print("YES")
        print(1)
        return
    
    # Build adjacency list using bitmasks for efficiency
    adj = [0] * n
    for u, v in edges:
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
    
    # If k > n, impossible
    if k > n:
        print("NO")
        return
        
    # For small n, try all combinations
    if n <= 25:
        # Try all combinations of k nodes
        for combo in combinations(range(n), k):
            valid = True
            for i in range(k):
                for j in range(i+1, k):
                    u = combo[i]
                    v = combo[j]
                    if adj[u] & (1 << v):
                        valid = False
                        break
                if not valid:
                    break
            if valid:
                print("YES")
                print(' '.join(str(x + 1) for x in combo))
                return
        print("NO")
        return
    
    # For larger n, use meet-in-the-middle approach
    # Split nodes into two halves
    mid = n // 2
    left_nodes = list(range(mid))
    right_nodes = list(range(mid, n))
    
    # Generate all valid subsets for left half
    left_valid = {}
    for mask in range(1 << mid):
        subset = []
        for i in range(mid):
            if mask & (1 << i):
                subset.append(i)
        
        # Check if subset is valid
        valid = True
        for i in range(len(subset)):
            for j in range(i+1, len(subset)):
                u = subset[i]
                v = subset[j]
                if adj[u] & (1 << v):
                    valid = False
                    break
            if not valid:
                break
        
        if valid:
            size = bin(mask).count('1')
            if size not in left_valid:
                left_valid[size] = []
            left_valid[size].append(mask)
    
    # Generate all valid subsets for right half
    right_valid = {}
    for mask in range(1 << (n - mid)):
        subset = []
        for i in range(n - mid):
            if mask & (1 << i):
                subset.append(mid + i)
        
        # Check if subset is valid
        valid = True
        for i in range(len(subset)):
            for j in range(i+1, len(subset)):
                u = subset[i]
                v = subset[j]
                if adj[u] & (1 << v):
                    valid = False
                    break
            if not valid:
                break
        
        if valid:
            size = bin(mask).count('1')
            if size not in right_valid:
                right_valid[size] = []
            right_valid[size].append((mask, subset))
    
    # Now check all pairs
    for left_size in range(k+1):
        right_size = k - left_size
        if left_size in left_valid and right_size in right_valid:
            for left_mask in left_valid[left_size]:
                for right_mask, right_subset in right_valid[right_size]:
                    # Check if there's no edge between left and right
                    valid = True
                    for i in range(mid):
                        if left_mask & (1 << i):
                            for node in right_subset:
                                if adj[i] & (1 << node):
                                    valid = False
                                    break
                        if not valid:
                            break
                    
                    if valid:
                        # Reconstruct the solution
                        left_subset = []
                        for i in range(mid):
                            if left_mask & (1 << i):
                                left_subset.append(i)
                        
                        result = left_subset + right_subset
                        print("YES")
                        print(' '.join(str(x + 1) for x in result))
                        return
    
    print("NO")

if __name__ == "__main__":
    main()