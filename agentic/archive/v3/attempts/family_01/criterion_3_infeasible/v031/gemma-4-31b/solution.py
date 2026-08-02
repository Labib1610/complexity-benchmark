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
        v = int(input_data[ptr+1])
        adj[u].append(v)
        adj[v].append(u)
        ptr += 2
    
    # To find the lexicographically smallest triple (a, b, c) where a < b < c:
    # We iterate through a from 1 to n.
    # For a fixed a, we look for the smallest b > a such that (a, b) is an edge.
    # Then we look for the smallest c > b such that (a, c) and (b, c) are edges.
    
    # Pre-sort adjacency lists to facilitate lexicographical search
    for i in range(1, n + 1):
        adj[i].sort()
        
    # Use a bitset-like approach or a boolean matrix for fast intersection
    # Since n <= 2000, a boolean matrix takes ~4MB, which fits in memory.
    matrix = [0] * (n + 1)
    # Using Python's large integers as bitsets for O(N/64) intersection
    # bitsets[i] will store neighbors of i
    bitsets = [0] * (n + 1)
    for u in range(1, n + 1):
        for v in adj[u]:
            bitsets[u] |= (1 << v)

    # Iterate through possible 'a' in increasing order
    for a in range(1, n + 1):
        # Neighbors of a that are > a
        neighbors_a = [v for v in adj[a] if v > a]
        
        # Iterate through possible 'b' in increasing order
        for b in neighbors_a:
            # We need c > b such that c is a neighbor of both a and b
            # This is the intersection of bitsets[a] and bitsets[b]
            # and we only care about bits > b.
            
            common = bitsets[a] & bitsets[b]
            if common == 0:
                continue
            
            # Find the smallest set bit in 'common' that is > b
            # Mask out bits <= b
            mask = ~((1 << (b + 1)) - 1)
            candidates = common & mask
            
            if candidates:
                # Find the lowest set bit (LSB)
                # candidates.bit_length() is the position of the highest set bit
                # To find the lowest, we can use (candidates & -candidates).bit_length() - 1
                # but in Python, bit_length of (candidates & -candidates) is the index + 1.
                lsb = (candidates & -candidates).bit_length() - 1
                print(f"{a} {b} {lsb}")
                return

if __name__ == "__main__":
    solve()