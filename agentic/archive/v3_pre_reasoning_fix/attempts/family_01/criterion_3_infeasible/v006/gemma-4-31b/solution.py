import sys

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Adjacency list for the graph
    adj = [[] for _ in range(n + 1)]
    ptr = 2
    for _ in range(m):
        u = int(input_data[ptr])
        v = int(input_data[ptr + 1])
        adj[u].append(v)
        adj[v].append(u)
        ptr += 2
    
    # Sort neighbors to ensure we find the lexicographically smallest triple
    for i in range(1, n + 1):
        adj[i].sort()
        
    # To quickly check if an edge exists, we use sets for high-degree nodes
    # or a bitset-like approach. However, since n=2000, we can use a bitset 
    # (Python's large integers) to represent the adjacency matrix.
    # This allows O(N/64) intersection checks.
    
    adj_bitset = [0] * (n + 1)
    for u in range(1, n + 1):
        for v in adj[u]:
            adj_bitset[u] |= (1 << v)
            
    # To find the lexicographically smallest triple (a, b, c):
    # We iterate a from 1 to n, then b from a+1 to n, then check if 
    # there exists a c > b such that (a, c) and (b, c) are edges.
    # The smallest such c will be the smallest bit set in (adj_bitset[a] & adj_bitset[b])
    # that is greater than b.
    
    for a in range(1, n + 1):
        # To optimize, we only iterate over actual neighbors of a that are > a
        neighbors_a = [v for v in adj[a] if v > a]
        for b in neighbors_a:
            # We need c > b such that c is a neighbor of both a and b
            common = adj_bitset[a] & adj_bitset[b]
            
            # Mask out all bits <= b
            # (1 << (b + 1)) - 1 creates a bitmask of 1s from index 0 to b
            # XORing or ANDing with the complement removes them.
            mask = ~((1 << (b + 1)) - 1)
            candidates = common & mask
            
            if candidates:
                # Find the lowest set bit (the smallest c)
                # Using bit_length and shifting or trailing zero count
                # In Python 3.10+, candidates.bit_count() or similar, 
                # but (candidates & -candidates).bit_length() - 1 is a common trick.
                
                # More reliably:
                c = (candidates & -candidates).bit_length() - 1
                print(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()