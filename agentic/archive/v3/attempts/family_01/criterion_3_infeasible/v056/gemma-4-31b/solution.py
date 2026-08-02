import sys

def solve():
    # Using fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Adjacency list for the graph
    adj = [[] for _ in range(n + 1)]
    # Adjacency matrix using bitsets (represented as integers in Python)
    # for O(1) or O(n/64) intersection check.
    # bit_adj[i] will have the j-th bit set if there is an edge between i and j.
    bit_adj = [0] * (n + 1)
    
    ptr = 2
    for _ in range(m):
        u = int(input_data[ptr])
        v = int(input_data[ptr + 1])
        ptr += 2
        if u > v:
            u, v = v, u
        adj[u].append(v)
        bit_adj[u] |= (1 << v)
        bit_adj[v] |= (1 << u)

    # To find the lexicographically smallest (a, b, c) with a < b < c:
    # We iterate a from 1 to n, then b from a + 1 to n.
    # We then check for c > b such that c is connected to both a and b.
    # The smallest such c will be the first bit set in (bit_adj[a] & bit_adj[b]) 
    # that is greater than b.
    
    # To optimize, we only iterate b through neighbors of a that are > a.
    for a in range(1, n + 1):
        # Pre-calculate neighbors of a that are > a
        neighbors_of_a = [v for v in adj[a] if v > a]
        # Sort neighbors of a to ensure we check b in increasing order
        neighbors_of_a.sort()
        
        for b in neighbors_of_a:
            # Find common neighbors of a and b that are > b
            common = bit_adj[a] & bit_adj[b]
            if common:
                # We need the smallest bit set in 'common' that is > b.
                # Mask out all bits <= b
                mask = ~((1 << (b + 1)) - 1)
                candidates = common & mask
                if candidates:
                    # Find the lowest set bit (LSB)
                    # c = (candidates & -candidates).bit_length() - 1
                    # In Python 3.10+, candidates.bit_count() or other methods exist,
                    # but (candidates & -candidates).bit_length() - 1 is a standard way.
                    c = (candidates & -candidates).bit_length() - 1
                    print(f"{a} {b} {c}")
                    return

if __name__ == "__main__":
    solve()