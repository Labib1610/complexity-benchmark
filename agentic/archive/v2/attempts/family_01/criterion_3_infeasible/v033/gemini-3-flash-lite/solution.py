import sys

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Store graph as adjacency sets for O(1) lookups
    adj = [set() for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        adj[u].add(v)
        adj[v].add(u)
        idx += 2
        
    # To find the lexicographically smallest triple (a, b, c) with a < b < c:
    # Iterate a from 1 to n-2
    # Iterate b from a+1 to n-1
    # Iterate c from b+1 to n
    # Check if a,b are connected, a,c connected, b,c connected.
    
    # Optimization: Sort neighbors of each node to speed up finding c
    adj_list = [sorted(list(s)) for s in adj]
    
    for a in range(1, n - 1):
        # We only care about neighbors of a to find b and c
        neighbors_a = adj_list[a]
        # Filter neighbors > a
        neighbors_a = [x for x in neighbors_a if x > a]
        
        for i in range(len(neighbors_a)):
            b = neighbors_a[i]
            # Now we need a c such that c > b, c is in adj[a], and c is in adj[b]
            # Since adj sets are needed for O(1) check, use the sets
            # To iterate efficiently, intersect adj[a] and adj[b]
            
            # Intersection of two sorted lists:
            neighbors_b = adj[b]
            
            # We want smallest c > b that is in both
            for c in neighbors_a[i+1:]:
                if c in neighbors_b:
                    print(f"{a} {b} {c}")
                    return

if __name__ == '__main__':
    solve()