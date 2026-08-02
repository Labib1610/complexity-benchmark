import sys

def solve():
    # Read n and m
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Use adjacency list represented as sets for O(1) lookup
    adj = [set() for _ in range(n + 1)]
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].add(v)
        adj[v].add(u)
        idx += 2
        
    # To find the lexicographically smallest triple (a, b, c) with a < b < c
    # iterate through all possible a, then b, then c.
    # Since we want the smallest triple, we iterate in increasing order.
    # To optimize, we only check if b is in adj[a] and c is in adj[a] AND adj[b].
    
    # Convert sets to sorted lists for deterministic iteration order
    adj_list = [sorted(list(s)) for s in adj]
    
    for a in range(1, n + 1):
        # We only care about neighbors b > a
        neighbors_a = [b for b in adj_list[a] if b > a]
        for i in range(len(neighbors_a)):
            b = neighbors_a[i]
            # We need a c such that b < c and c is connected to both a and b
            # Intersection of neighbors of a and neighbors of b
            # Since we need c > b, we search in neighbors_a[i+1:]
            # Or more efficiently, intersect the sorted neighbors
            
            # Use sets for O(1) lookup
            for j in range(i + 1, len(neighbors_a)):
                c = neighbors_a[j]
                if c in adj[b]:
                    print(f"{a} {b} {c}")
                    return

if __name__ == '__main__':
    solve()