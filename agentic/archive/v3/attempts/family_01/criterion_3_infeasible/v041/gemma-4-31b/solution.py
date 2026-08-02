import sys

def solve():
    # Read n and m
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Adjacency lists and adjacency matrix (bitsets for efficiency)
    # Since n is up to 2000, a bitset (Python's large integers) 
    # allows for O(n/64) intersection checks.
    adj_bits = [0] * (n + 1)
    adj_list = [[] for _ in range(n + 1)]
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        # Ensure u < v for consistent storage
        if u > v:
            u, v = v, u
        adj_bits[u] |= (1 << v)
        adj_list[u].append(v)

    # To find the lexicographically smallest triple (a, b, c) where a < b < c:
    # We iterate a from 1 to n, then b from a+1 to n.
    # For a fixed a and b, we need the smallest c > b such that
    # c is connected to both a and b.
    
    # Pre-sort adjacency lists to iterate b in increasing order
    for i in range(1, n + 1):
        adj_list[i].sort()

    for a in range(1, n - 1):
        # Only check a if it has at least 2 neighbors > a
        if len(adj_list[a]) < 2:
            continue
        
        # b must be a neighbor of a and b > a
        for b in adj_list[a]:
            # We need a < b < c. Since adj_list[a] is sorted and we only
            # stored v > u in adj_list[u], b is already > a.
            
            # We need the smallest c such that c > b, c is connected to a,
            # and c is connected to b.
            # The candidates for c are the neighbors of a that are > b.
            # The intersection of neighbors of a and neighbors of b
            # gives all common neighbors.
            
            # common_neighbors = adj_bits[a] & adj_bits[b]
            # However, adj_bits[b] only contains neighbors > b.
            # adj_bits[a] contains all neighbors > a.
            # So (adj_bits[a] & adj_bits[b]) contains all c > b connected to both.
            
            common = adj_bits[a] & adj_bits[b]
            if common:
                # Find the lowest set bit in 'common'
                # (common & -common).bit_length() - 1 gives the index of the LSB
                c = (common & -common).bit_length() - 1
                print(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()