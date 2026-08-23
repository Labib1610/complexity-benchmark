import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    iterator = iter(input_data)
    n = int(next(iterator))
    m = int(next(iterator))
    
    adj = [set() for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(iterator))
        v = int(next(iterator))
        adj[u].add(v)
        adj[v].add(u)
    
    # Iterate to find the lexicographically smallest triad
    for a in range(1, n + 1):
        neighbors_a = adj[a]
        # We need to find b and c such that a < b < c and b, c are neighbors of a
        # and b, c are neighbors of each other.
        # Convert to list to iterate in order, filtering for elements > a
        # Sorting neighbors is not strictly necessary if we iterate b and check conditions
        # but iterating b in ascending order helps find the lexicographically smallest faster.
        
        # Create a sorted list of valid neighbors (greater than a)
        valid_neighbors = [v for v in neighbors_a if v > a]
        valid_neighbors.sort()
        
        for b in valid_neighbors:
            # Check if b is connected to a (it is by definition)
            # Now find c in neighbors of a such that c > b and c is neighbor of b
            neighbors_b = adj[b]
            
            # Iterate through valid_neighbors again to find c
            # Since valid_neighbors is sorted, we can start checking from elements > b
            for c in valid_neighbors:
                if c > b:
                    if c in neighbors_b:
                        print(a, b, c)
                        return

if __name__ == '__main__':
    solve()