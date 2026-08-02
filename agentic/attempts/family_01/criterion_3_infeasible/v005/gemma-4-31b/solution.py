import sys

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Adjacency list using sets for O(1) lookup
    adj = [set() for _ in range(n + 1)]
    # Store edges in a sorted list to iterate efficiently
    edges = []
    
    ptr = 2
    for _ in range(m):
        u = int(input_data[ptr])
        v = int(input_data[ptr+1])
        ptr += 2
        # Ensure u < v for consistent processing
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    # Sort edges to facilitate finding the lexicographically smallest triple
    # Since we want smallest a, then b, then c, iterating through edges (a, b)
    # where a < b and then checking common neighbors c > b is efficient.
    edges.sort()
    
    # To optimize, we only check nodes c that are neighbors of both a and b.
    # We want the smallest a, then smallest b, then smallest c.
    # The sorted edges list ensures we check pairs (a, b) in lexicographical order.
    
    # However, just iterating through edges might not be enough if we don't
    # check the neighbors of the smaller degree vertex.
    # Let's refine: iterate through all possible 'a' from 1 to n.
    # For each 'a', iterate through its neighbors 'b' where b > a.
    # For each 'b', find common neighbors 'c' where c > b.
    
    # To speed up common neighbor search, we can use bitsets if N was larger,
    # but for N=2000, intersecting sets or iterating over the smaller adjacency list works.
    
    # Pre-calculate adjacency lists as sorted lists for faster iteration
    sorted_adj = [sorted(list(adj[i])) for i in range(n + 1)]
    
    for a in range(1, n + 1):
        # Only check b > a
        neighbors_a = sorted_adj[a]
        for b in neighbors_a:
            if b <= a:
                continue
            
            # Find common neighbors c of a and b such that c > b
            # We iterate through the neighbors of b and check if they are also neighbors of a
            neighbors_b = sorted_adj[b]
            for c in neighbors_b:
                if c <= b:
                    continue
                if c in adj[a]:
                    print(f"{a} {b} {c}")
                    return

if __name__ == "__main__":
    solve()