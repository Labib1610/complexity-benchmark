import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [set() for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        adj[u].add(v)
        adj[v].add(u)
        idx += 2
        
    # To find the lexicographically smallest triple (a, b, c),
    # we iterate a from 1 to n, b from a+1 to n, and c from b+1 to n.
    # To optimize, we only check b in adj[a] and c in (adj[a] intersect adj[b]).
    
    # Sort adjacency lists for predictable order, though not strictly required for correctness.
    sorted_adj = [sorted(list(adj[i])) for i in range(n + 1)]
    
    for a in range(1, n + 1):
        neighbors_a = sorted_adj[a]
        # Only keep neighbors > a to ensure a < b
        filtered_a = [b for b in neighbors_a if b > a]
        
        for i in range(len(filtered_a)):
            b = filtered_a[i]
            # Find common neighbors of a and b that are > b
            # We can intersect the sets or iterate through neighbors of b
            # that are also in neighbors_a.
            # Using set intersection is efficient for sparse graphs.
            
            # Optimization: check intersection of adj[a] and adj[b]
            # Only need to check if there is any c > b in the intersection.
            # To get the lexicographically smallest, we need the smallest c.
            
            common = sorted(list(adj[a].intersection(adj[b])))
            for c in common:
                if c > b:
                    print(f"{a} {b} {c}")
                    return

if __name__ == '__main__':
    solve()