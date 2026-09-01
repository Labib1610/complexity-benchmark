import sys

def solve() -> None:
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [set() for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        if u > v:
            u, v = v, u
        adj[u].add(v)
    
    best_a = -1
    best_b = -1
    best_c = -1
    
    for a in range(1, n + 1):
        # Optimization: if current a is already larger than best found, we can stop
        # because we need lexicographically smallest.
        if best_a != -1 and a > best_a:
            break
            
        neighbors = adj[a]
        # Convert to sorted list to iterate in order, ensuring we find smallest b first
        sorted_neighbors = sorted(neighbors)
        
        # Iterate over pairs (b, c) from neighbors where b < c
        # We iterate b from smallest to largest
        for i in range(len(sorted_neighbors)):
            b = sorted_neighbors[i]
            
            # Optimization: if best_a is found and current a is same, 
            # but b is larger than best_b, we can break inner loop
            if best_a != -1 and a == best_a and b > best_b:
                break
            
            # For c, we only need to check values > b that are in neighbors
            # and also in adj[b].
            # Since sorted_neighbors is sorted, we can iterate j > i
            # but checking adj[b] is faster if adj[b] is small.
            # However, iterating sorted_neighbors from i+1 ensures we check in order.
            
            # Let's try checking adj[b] intersection with neighbors
            # To maintain order for c, we iterate sorted_neighbors from i+1
            # and check membership in adj[b].
            
            # Optimization: if best_b is found and b == best_b, 
            # we only need to find c < best_c.
            
            for j in range(i + 1, len(sorted_neighbors)):
                c = sorted_neighbors[j]
                
                if best_a != -1 and a == best_a and b == best_b and c >= best_c:
                    break
                
                if c in adj[b]:
                    # Found a triangle
                    best_a = a
                    best_b = b
                    best_c = c
                    # Since we iterate in order, this is the best for current a and b.
                    # We can break the innermost loop for c.
                    break
            
            # If we found a triangle for this (a, b), we can break the loop for b
            # because we want the smallest b.
            if best_a == a and best_b == b:
                break
    
    print(best_a, best_b, best_c)

if __name__ == "__main__":
    solve()