import sys

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Use a bitset-like approach for adjacency to speed up intersection checks
    # adj[u] will be a set of neighbors. Since n <= 2000, bitsets are efficient.
    adj = [0] * (n + 1)
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        # Use bit manipulation for speed
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
    
    # We want the lexicographically smallest (a, b, c) with a < b < c
    # Iterate a from 1 to n-2
    for a in range(1, n - 1):
        # Find neighbors of a that are > a
        neighbors_a = []
        bits = adj[a]
        for b in range(a + 1, n):
            if (bits >> b) & 1:
                neighbors_a.append(b)
        
        # Now check every pair (b, c) from neighbors_a
        # Sort neighbors_a to ensure we check in increasing order for lexicographical requirement
        # Actually, they are already appended in increasing order.
        for i in range(len(neighbors_a)):
            b = neighbors_a[i]
            # Check if b and c are connected
            # c must be a neighbor of a AND a neighbor of b
            # We need to find c > b such that c is in adj[a] and adj[b]
            common = adj[a] & adj[b]
            # We only care about c > b
            # Mask to clear bits <= b
            common &= ~((1 << (b + 1)) - 1)
            
            if common:
                # Find the smallest c
                # This is the index of the lowest set bit
                c = (common & -common).bit_length() - 1
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    solve()