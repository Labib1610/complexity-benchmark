import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    it = iter(input_data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [set() for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].add(v)
        adj[v].add(u)
    
    # Convert to sorted lists for deterministic iteration
    adj_list = [sorted(s) for s in adj]
    
    best_a, best_b, best_c = n + 1, n + 1, n + 1
    
    for a in range(1, n - 1):
        # Optimization: if a is already larger than best_a, we can't improve
        if a > best_a:
            break
            
        neighbors_a = adj_list[a]
        # We need b > a and c > b, so filter neighbors
        # Candidates for b and c must be in neighbors of a
        # Create a list of valid neighbors (greater than a)
        valid_neighbors = [v for v in neighbors_a if v > a]
        
        len_vn = len(valid_neighbors)
        for i in range(len_vn):
            b = valid_neighbors[i]
            if b > best_b and a == best_a:
                continue
            
            neighbors_b = adj_list[b]
            # We need c > b, so iterate over neighbors of b that are > b
            # and check if they are also in neighbors of a
            
            # Since valid_neighbors is sorted, we can iterate from i+1
            for j in range(i + 1, len_vn):
                c = valid_neighbors[j]
                if c > best_c and a == best_a and b == best_b:
                    continue
                
                # Check if b and c are connected
                # Binary search in neighbors_b since it's sorted
                # neighbors_b is sorted list of adj[b]
                # We check if c exists in neighbors_b
                
                # Manual binary search
                nb = neighbors_b
                lo, hi = 0, len(nb) - 1
                found = False
                while lo <= hi:
                    mid = (lo + hi) // 2
                    if nb[mid] == c:
                        found = True
                        break
                    elif nb[mid] < c:
                        lo = mid + 1
                    else:
                        hi = mid - 1
                
                if found:
                    best_a, best_b, best_c = a, b, c
                    # Since valid_neighbors is sorted, the first found c is the smallest
                    # So we can break inner loop
                    break
    
    print(best_a, best_b, best_c)

if __name__ == "__main__":
    solve()