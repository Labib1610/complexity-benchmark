import sys

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Adjacency list to store neighbors
    adj = [[] for _ in range(n + 1)]
    # Adjacency matrix for O(1) lookup. 
    # Since n <= 2000, n^2 is 4*10^6, which fits in memory (bitsets would be better, 
    # but a bytearray or list of lists is okay in Python for this constraint).
    # Using a list of sets or a bitset-like approach for efficiency.
    matrix = [0] * (n + 1)
    
    # We can use bitsets via Python's large integers to speed up intersection.
    # Each matrix[i] will be an integer where the j-th bit is 1 if (i, j) is an edge.
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
        matrix[u] |= (1 << v)
        matrix[v] |= (1 << u)

    # Sort adjacency lists to ensure we check vertices in increasing order
    for i in range(1, n + 1):
        adj[i].sort()

    # We want the lexicographically smallest (a, b, c) with a < b < c.
    # Iterate through possible 'a' from 1 to n.
    for a in range(1, n + 1):
        # Neighbors of 'a' that are greater than 'a'
        neighbors_a = [v for v in adj[a] if v > a]
        
        # Iterate through pairs (b, c) from neighbors of 'a'
        # To find the smallest b, we iterate through sorted neighbors_a.
        for i in range(len(neighbors_a)):
            b = neighbors_a[i]
            # We need to find the smallest c > b such that c is also a neighbor of b.
            # c must be in the intersection of neighbors of a and neighbors of b.
            
            # The bitmask of neighbors of 'a' that are > b
            # mask_a = matrix[a] >> (b + 1) << (b + 1)
            # But it's simpler to just iterate through the remaining sorted neighbors of 'a'.
            for j in range(i + 1, len(neighbors_a)):
                c = neighbors_a[j]
                # Check if b and c are connected
                if (matrix[b] >> c) & 1:
                    print(f"{a} {b} {c}")
                    return

if __name__ == "__main__":
    solve()