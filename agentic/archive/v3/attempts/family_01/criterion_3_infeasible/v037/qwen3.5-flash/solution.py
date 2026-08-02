import sys

# Increase recursion depth just in case, though not strictly needed here
sys.setrecursionlimit(20000)

def solve():
    # Read all input from stdin efficiently
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return
    
    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return
    
    # adj_mask[i] will store a bitmask of neighbors of machine i
    # bit j corresponds to machine j+1.
    # For example, if machine 1 is a neighbor, bit 0 is set.
    adj_mask = [0] * (n + 1)
    
    # adj_list[i] will store a sorted list of neighbors of i that are greater than i.
    # This allows us to iterate b > a efficiently.
    adj_list = [[] for _ in range(n + 1)]
    
    # Read m edges
    for _ in range(m):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
            
            # Update adjacency mask
            # Machine u corresponds to bit (u-1), Machine v to bit (v-1)
            adj_mask[u] |= (1 << (v - 1))
            adj_mask[v] |= (1 << (u - 1))
            
            # Populate adj_list
            # We only store neighbors that are strictly greater than the current machine index
            # This ensures that for any a, adj_list[a] contains candidates for b where b > a
            if u < v:
                adj_list[u].append(v)
            else:
                adj_list[v].append(u)
                
        except StopIteration:
            break
            
    # Sort the neighbor lists to ensure we check b in increasing order
    # This is crucial for finding the lexicographically smallest triplet
    for i in range(1, n + 1):
        adj_list[i].sort()
        
    # Iterate through each machine 'a' from 1 to n
    for a in range(1, n + 1):
        # Optimization: If 'a' has no neighbors greater than 'a', we can't form a triangle with a < b < c.
        # adj_mask[a] has bit k set if machine k+1 is a neighbor.
        # We need neighbors with machine index > a, which corresponds to bit index >= a.
        # If (adj_mask[a] >> a) == 0, it means no bits >= a are set.
        if (adj_mask[a] >> a) == 0:
            continue
            
        # Iterate through neighbors b of a such that b > a
        # adj_list[a] contains exactly these neighbors in sorted order.
        for b in adj_list[a]:
            # We have established a < b and edge (a, b) exists.
            # Now we need to find the smallest c > b such that (a, c) and (b, c) exist.
            # This means c must be a common neighbor of a and b, and c > b.
            # In terms of bitmasks, c corresponds to a bit index k in common = adj_mask[a] & adj_mask[b].
            # Machine c corresponds to bit c-1.
            # Condition c > b implies c >= b+1, so bit index c-1 >= b.
            # Thus, we need the smallest bit index k in 'common' such that k >= b.
            
            common = adj_mask[a] & adj_mask[b]
            
            # Shift right by b to discard bits < b (machines <= b).
            # This brings the bit at index b to position 0.
            shifted = common >> b
            
            if shifted:
                # Find the lowest set bit in shifted
                lsb = shifted & -shifted
                
                # lsb is a power of 2, say 2^k.
                # The bit index in shifted is k.
                # The bit index in common is k + b.
                # The machine index c is (k + b) + 1 = k + b + 1.
                # lsb.bit_length() returns k + 1.
                # Therefore, c = (lsb.bit_length() - 1) + b + 1 = lsb.bit_length() + b.
                c = lsb.bit_length() + b
                
                # We found the lexicographically smallest triplet (a, b, c)
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    solve()