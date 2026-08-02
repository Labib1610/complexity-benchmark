import sys

def solve():
    # Read n and m
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Use an adjacency list and adjacency sets for quick lookups
    adj = [set() for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        adj[u].add(v)
        adj[v].add(u)
        idx += 2
        
    # We want the lexicographically smallest triple (a, b, c) with a < b < c.
    # We iterate through possible values of a, then b, then c.
    # To optimize: 
    # For a fixed a, b must be a neighbor of a.
    # For a fixed a and b, c must be a neighbor of both a and b.
    
    # Sorting adjacency lists allows us to find the smallest candidates first
    adj_list = [sorted(list(adj[i])) for i in range(n + 1)]
    
    for a in range(1, n + 1):
        neighbors_a = adj_list[a]
        # Only consider b > a
        for b in neighbors_a:
            if b <= a:
                continue
            
            # Now we need c > b such that c is in adj[a] and adj[b]
            # Since we want the smallest b and then smallest c, we check
            # neighbors of a that are also neighbors of b.
            # To be efficient, intersect neighbors_a and neighbors_b
            neighbors_b = adj[b]
            
            for c in neighbors_a:
                if c > b and c in neighbors_b:
                    print(f"{a} {b} {c}")
                    return

if __name__ == '__main__':
    solve()