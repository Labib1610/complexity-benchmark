import sys

def solve():
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
        adj[u].add(v)
        adj[v].add(u)
    
    # Sort adjacency lists for deterministic iteration
    # We need to iterate neighbors in sorted order to find lexicographically smallest triple
    adj_lists = [sorted(s) for s in adj]
    
    best_a = n + 1
    best_b = n + 1
    best_c = n + 1
    
    for a in range(1, n + 1):
        # Optimization: if current a is already larger than best_a, we can stop
        if a > best_a:
            break
            
        neighbors_a = adj_lists[a]
        # We need b > a and c > b
        # Iterate b in neighbors_a where b > a
        # To find smallest triple, iterate b in sorted order
        
        # Filter neighbors > a
        # Since neighbors_a is sorted, we can iterate
        for b in neighbors_a:
            if b <= a:
                continue
            if b > best_b:
                break
            
            neighbors_b = adj_lists[b]
            # Iterate c in neighbors_b where c > b
            for c in neighbors_b:
                if c <= b:
                    continue
                # Check if a-c is an edge
                if c in adj[a]:
                    # Found a triple
                    if a < best_a or (a == best_a and b < best_b) or (a == best_a and b == best_b and c < best_c):
                        best_a = a
                        best_b = b
                        best_c = c
                    # Since we iterate in sorted order, this is the smallest c for this (a, b)
                    # We can break inner loop
                    break
        
        # If we found a triple with current a, we don't need to check larger a values
        # But we need to make sure we have the smallest b and c for this a
        # The above logic already finds smallest b and c for each a
        # Since we want lexicographically smallest, once we find any triple with current a,
        # we can update best and continue to next a (but we already break early if a > best_a)
    
    print(best_a, best_b, best_c)

if __name__ == "__main__":
    solve()