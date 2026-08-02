import sys

# Increase recursion depth just in case, though not needed for this iterative solution
sys.setrecursionlimit(2000)

def solve():
    # Read all input from standard input efficiently
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # Adjacency masks for fast intersection (bitsets)
    # adj_mask[u] will have the v-th bit set if (u, v) is an edge
    adj_mask = [0] * n
    # Adjacency lists for iterating neighbors in sorted order
    adj_list = [[] for _ in range(n)]
    
    # Read m edges
    for _ in range(m):
        u = int(next(iterator)) - 1
        v = int(next(iterator)) - 1
        adj_mask[u] |= (1 << v)
        adj_mask[v] |= (1 << u)
        adj_list[u].append(v)
        adj_list[v].append(u)
        
    # Sort adjacency lists to ensure we process b in increasing order
    # This is crucial for finding the lexicographically smallest triple
    for i in range(n):
        adj_list[i].sort()
        
    # Iterate through each node a as the first element of the triple
    for a in range(n):
        # Iterate through neighbors b of a
        for b in adj_list[a]:
            # We need a < b < c. Since we iterate a in increasing order,
            # we just need to ensure b > a.
            if b <= a:
                continue
            
            # We need to find c such that (a, c) and (b, c) are edges, and c > b.
            # This means c must be a common neighbor of a and b.
            # We compute the intersection of neighbors of a and b using bitwise AND.
            common = adj_mask[a] & adj_mask[b]
            
            # We need the smallest bit set in 'common' that is greater than b.
            # Create a mask that has 0s for bits 0 to b, and 1s for bits > b.
            # (1 << (b + 1)) - 1 creates a mask with bits 0..b set to 1.
            # ~ inverts it, setting bits 0..b to 0 (and higher bits to 1).
            # We AND this with 'common' to keep only bits > b.
            # Note: In Python, ~x is equivalent to -x-1 (two's complement with infinite bits).
            # Since common is non-negative, the operation works correctly.
            mask_gt_b = common & ~((1 << (b + 1)) - 1)
            
            if mask_gt_b == 0:
                continue
            
            # Find the lowest set bit in mask_gt_b.
            # mask_gt_b & -mask_gt_b isolates the lowest set bit (power of 2).
            isolated = mask_gt_b & -mask_gt_b
            
            # bit_length() returns the number of bits required to represent an integer.
            # For a power of 2 (isolated bit), bit_length() - 1 is the index of the bit.
            c = isolated.bit_length() - 1
            
            # We found the lexicographically smallest triple (a, b, c)
            # because we iterate a increasing, b increasing, and pick smallest c.
            print(f"{a + 1} {b + 1} {c + 1}")
            return

if __name__ == '__main__':
    solve()