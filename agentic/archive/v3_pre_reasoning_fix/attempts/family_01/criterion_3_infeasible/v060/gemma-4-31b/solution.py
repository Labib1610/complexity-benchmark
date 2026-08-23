import sys

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Adjacency list and adjacency matrix for fast lookup
    # Since n <= 2000, an adjacency matrix fits in memory (2000*2000 bits/bools)
    # Python's list of lists or bitsets (integers) can be used.
    adj = [[] for _ in range(n + 1)]
    # We use a bitset (represented as a large integer in Python) for each node
    # to perform fast intersections.
    matrix = [0] * (n + 1)
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
        matrix[u] |= (1 << v)
        matrix[v] |= (1 << u)
    
    # To find the lexicographically smallest (a, b, c) with a < b < c:
    # Iterate a from 1 to n
    # Iterate b from a + 1 to n
    # Check if (a, b) is an edge, then find the smallest c > b such that (a, c) and (b, c) are edges.
    
    # Optimization: only iterate over neighbors of a that are > a.
    for a in range(1, n + 1):
        # Get neighbors of a that are greater than a
        neighbors_a = [v for v in adj[a] if v > a]
        neighbors_a.sort()
        
        # We want the smallest b among these neighbors
        for b in neighbors_a:
            # Find c > b such that c is a neighbor of both a and b
            # This is equivalent to finding the smallest set bit in (matrix[a] & matrix[b])
            # that is at a position > b.
            common = matrix[a] & matrix[b]
            
            # Mask out bits <= b
            # (1 << (b + 1)) - 1 creates a mask of bits from 0 to b.
            # We invert this to keep only bits > b.
            mask = ~((1 << (b + 1)) - 1)
            candidates = common & mask
            
            if candidates:
                # Find the lowest set bit in candidates
                # candidates.bit_length() gives the position of the highest set bit.
                # To find the lowest set bit: (candidates & -candidates).bit_length() - 1
                # Or simply iterate since we need the smallest c.
                # However, bit_length() is for the highest. 
                # For the lowest:
                low_bit = candidates & -candidates
                c = low_bit.bit_length() - 1
                print(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()