import sys

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Adjacency list for graph
    adj = [[] for _ in range(n + 1)]
    # Adjacency matrix (bitsets) for O(1) lookup
    # Since n <= 2000, a bitset per node is feasible (2000 * 2000 bits ~ 500KB)
    bit_adj = [0] * (n + 1)
    
    ptr = 2
    for _ in range(m):
        u = int(input_data[ptr])
        v = int(input_data[ptr+1])
        ptr += 2
        adj[u].append(v)
        adj[v].append(u)
        bit_adj[u] |= (1 << v)
        bit_adj[v] |= (1 << u)
        
    # To find the lexicographically smallest triple (a, b, c) with a < b < c:
    # Iterate a from 1 to n.
    # For a fixed a, we need to find the smallest b > a such that a and b are connected,
    # and then the smallest c > b such that a and c are connected AND b and c are connected.
    
    for a in range(1, n + 1):
        # Get all neighbors of a that are > a
        neighbors_a = sorted([v for v in adj[a] if v > a])
        
        # We want the smallest b from neighbors_a
        for b in neighbors_a:
            # We need the smallest c from neighbors_a such that c > b and c is connected to b
            # We can use bitwise AND to find common neighbors of a and b
            # Common neighbors are (bit_adj[a] & bit_adj[b])
            common = bit_adj[a] & bit_adj[b]
            
            # We need the smallest c > b. 
            # Mask out bits <= b.
            mask = ~((1 << (b + 1)) - 1)
            candidates = common & mask
            
            if candidates:
                # Find the lowest set bit in candidates
                # candidates.bit_length() - 1 is the highest, but we need the lowest.
                # (candidates & -candidates).bit_length() - 1 gives the index of the lowest set bit.
                c = (candidates & -candidates).bit_length() - 1
                print(f"{a} {b} {c}")
                return

if __name__ == "__main__":
    solve()