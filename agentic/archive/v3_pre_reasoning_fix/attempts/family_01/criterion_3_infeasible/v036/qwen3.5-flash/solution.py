import sys

# Increase recursion depth just in case, though not used here.
sys.setrecursionlimit(2000)

def solve():
    # Read all input from standard input at once for efficiency
    input_data = sys.stdin.read().split()
    
    if not input_data:
        return

    iterator = iter(input_data)
    
    try:
        n = int(next(iterator))
        m = int(next(iterator))
    except StopIteration:
        return

    # adj_mask[u] will store the bitmask of neighbors of u.
    # We use 0-based bit indexing: vertex v corresponds to bit (v-1).
    # Size is n + 1 for 1-based indexing convenience.
    adj_mask = [0] * (n + 1)
    
    # adj_list[u] will store the list of neighbors of u.
    adj_list = [[] for _ in range(n + 1)]
    
    # Read edges
    for _ in range(m):
        try:
            u = int(next(iterator))
            v = int(next(iterator))
        except StopIteration:
            break
        
        # Update adjacency mask (bitwise OR)
        adj_mask[u] |= (1 << (v - 1))
        adj_mask[v] |= (1 << (u - 1))
        
        # Update adjacency list
        adj_list[u].append(v)
        adj_list[v].append(u)
        
    # Sort adjacency lists to ensure we iterate 'b' in increasing order.
    # This is crucial for finding the lexicographically smallest triplet (a, b, c).
    # By processing 'b' in increasing order, we ensure that the first valid 'b' we find
    # for a given 'a' is the smallest possible 'b'.
    for i in range(1, n + 1):
        adj_list[i].sort()
        
    # Iterate through each vertex 'a' from 1 to n.
    # We want the smallest 'a' first.
    for a in range(1, n + 1):
        # Iterate through neighbors 'b' of 'a'.
        # Since adj_list[a] is sorted, we process 'b' in increasing order.
        for b in adj_list[a]:
            # We are looking for a triplet (a, b, c) such that a < b < c.
            # So we only consider neighbors 'b' where b > a.
            if b > a:
                # We need to find a neighbor 'c' of 'b' such that 'c' is also a neighbor of 'a'
                # AND c > b. We want the smallest such 'c'.
                
                # Find common neighbors of 'a' and 'b' using bitwise AND.
                # This gives a bitmask where the k-th bit is set if vertex k+1 is a neighbor of both.
                common = adj_mask[a] & adj_mask[b]
                
                # We are interested in c > b.
                # Vertex c corresponds to bit index (c-1).
                # c > b implies c-1 >= b.
                # So we need to check if any bit >= b is set in 'common'.
                # Shifting 'common' right by 'b' moves bit 'b' to position 0, bit 'b+1' to 1, etc.
                shifted = common >> b
                
                if shifted:
                    # If shifted is non-zero, there exists at least one common neighbor c > b.
                    # We want the smallest such c, which corresponds to the lowest set bit in 'shifted'.
                    lowbit = shifted & -shifted
                    
                    # bit_length() returns the number of bits required to represent an integer.
                    # For a power of 2 (2^k), bit_length is k + 1.
                    # The index of the set bit is k = bit_length - 1.
                    # If bit 0 of 'shifted' is set (k=0), it corresponds to vertex b + 1.
                    # If bit 1 is set (k=1), it corresponds to vertex b + 2.
                    # So, c = b + 1 + k.
                    idx = lowbit.bit_length() - 1
                    c = b + 1 + idx
                    
                    # We found the lexicographically smallest triplet (a, b, c).
                    # Since we iterate 'a' increasing, then 'b' increasing, then 'c' increasing,
                    # the first one we find is the answer.
                    print(f"{a} {b} {c}")
                    return

if __name__ == '__main__':
    solve()