import sys

# Increase recursion depth just in case, though not strictly needed here.
sys.setrecursionlimit(2000)

def solve():
    # Read all input from stdin efficiently
    # Using sys.stdin.read().split() handles all whitespace (newlines, spaces)
    try:
        input_data = sys.stdin.read().split()
    except Exception:
        return
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Adjacency list to iterate neighbors in sorted order
    # Adjacency mask for O(1) edge existence check and fast intersection using bitmasks
    adj_list = [[] for _ in range(n + 1)]
    adj_mask = [0] * (n + 1)

    # Parse edges
    for _ in range(m):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
            adj_list[u].append(v)
            adj_list[v].append(u)
            # Set the bit corresponding to the node index
            # We use 1-based indexing for nodes, so 1 << v sets the v-th bit
            adj_mask[u] |= (1 << v)
            adj_mask[v] |= (1 << u)
        except StopIteration:
            break

    # Sort adjacency lists to ensure we visit neighbors in increasing order
    # This is necessary to find the lexicographically smallest triple (a, b, c)
    # Specifically, we need to check smaller b before larger b for a fixed a.
    for i in range(1, n + 1):
        adj_list[i].sort()

    # Iterate through all possible 'a' from 1 to n
    # We want to minimize a, so we start from 1.
    for a in range(1, n + 1):
        # Iterate through neighbors 'b' of 'a'
        # Since adj_list[a] is sorted, we encounter smallest valid b first.
        for b in adj_list[a]:
            if b <= a:
                continue
            
            # We have edge (a, b) with a < b.
            # We need to find the smallest 'c' such that c > b and (a, c) and (b, c) are edges.
            # This corresponds to finding the lowest set bit in the intersection of neighbors of a and b
            # that is at a position > b.
            
            # Intersection of neighbors of a and b
            common = adj_mask[a] & adj_mask[b]
            
            # We want c > b. 
            # 'common' has bits set for neighbors.
            # We shift right by (b + 1) to discard bits <= b.
            # The lowest set bit in the shifted value corresponds to the smallest valid c.
            shifted = common >> (b + 1)
            
            if shifted:
                # Find the lowest set bit in shifted
                # shifted & -shifted isolates the lowest set bit
                lsb = shifted & -shifted
                
                # Calculate the index of this bit.
                # bit_length() returns the number of bits required to represent an integer.
                # For a power of 2 (2^k), bit_length() is k + 1.
                # So the bit index (0-based) is bit_length() - 1.
                # Since we shifted by (b + 1), the original index c is (bit_length() - 1) + (b + 1).
                # Simplifying: c = bit_length() + b.
                c = lsb.bit_length() + b
                
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    solve()