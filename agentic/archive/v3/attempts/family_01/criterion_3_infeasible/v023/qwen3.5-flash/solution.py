import sys

# Increase recursion depth just in case, though not used here.
sys.setrecursionlimit(2000)

def solve():
    # Read all input from standard input
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Adjacency list for iteration order
    adj_list = [[] for _ in range(n)]
    # Adjacency masks for fast intersection
    # Using integers as bitmasks where the k-th bit is set if there is an edge to k
    adj_mask = [0] * n

    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        adj_list[u].append(v)
        adj_list[v].append(u)
        adj_mask[u] |= (1 << v)
        adj_mask[v] |= (1 << u)

    # Sort adjacency lists to ensure neighbors are processed in increasing order
    # This is crucial for finding the lexicographically smallest triplet
    for i in range(n):
        adj_list[i].sort()

    # Iterate through each vertex as the smallest vertex 'a' in the triplet
    # a ranges from 0 to n-3 (since we need at least b and c > a)
    for a in range(n - 2):
        # Iterate through neighbors of 'a' as potential 'b'
        # We need b > a to ensure a < b < c
        for b in adj_list[a]:
            if b <= a:
                continue
            
            # Check for a common neighbor 'c' such that c > b
            # c must be connected to both a and b
            # We use bitwise AND to find common neighbors efficiently
            common = adj_mask[a] & adj_mask[b]
            
            # We only care about neighbors c > b
            # Shift right by (b + 1) to remove bits <= b
            # This operation effectively filters out candidates c <= b
            shifted = common >> (b + 1)
            
            if shifted > 0:
                # Find the smallest bit set in shifted
                # This corresponds to the smallest c > b
                # lsb = shifted & -shifted isolates the lowest set bit
                lsb = shifted & -shifted
                
                # bit_length() returns the number of bits required to represent the integer
                # For a power of 2 (lsb), bit_length() - 1 gives the 0-based index of the bit
                # We add (b + 1) because we shifted by (b + 1)
                c = lsb.bit_length() - 1 + (b + 1)
                
                # Output the triplet (converting back to 1-based indexing)
                print(f"{a + 1} {b + 1} {c + 1}")
                return

if __name__ == '__main__':
    solve()