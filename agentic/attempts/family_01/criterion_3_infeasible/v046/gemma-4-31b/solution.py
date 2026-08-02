import sys

def solve():
    # Set recursion limit just in case, though not needed for this iterative approach
    sys.setrecursionlimit(2000)
    
    # Read n and m
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Adjacency list to store the interference graph
    adj = [[] for _ in range(n + 1)]
    # Adjacency matrix for O(1) lookup of edges
    # Using a bitset-like approach or a list of sets for efficiency in Python
    # Given n=2000, a bitset (integer) per node is efficient in Python
    adj_bitset = [0] * (n + 1)
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        adj[u].append(v)
        adj[v].append(u)
        adj_bitset[u] |= (1 << v)
        adj_bitset[v] |= (1 << u)
    
    # To find the lexicographically smallest (a, b, c) with a < b < c:
    # We iterate a from 1 to n, then b from a+1 to n, then c from b+1 to n.
    # However, a naive O(n^3) is too slow.
    # We can optimize by iterating through a and then checking pairs (b, c) among a's neighbors.
    
    # Sort adjacency lists to help with lexicographical order
    for i in range(1, n + 1):
        adj[i].sort()
        
    for a in range(1, n + 1):
        # Neighbors of a that are greater than a
        neighbors_a = [v for v in adj[a] if v > a]
        
        # We need to find the smallest b, c from neighbors_a such that b < c and (b, c) is an edge.
        # Since neighbors_a is sorted, we can iterate b in order.
        for i in range(len(neighbors_a)):
            b = neighbors_a[i]
            # We need to find the smallest c in neighbors_a such that c > b and c is connected to b.
            # We can use bitwise AND between the adjacency bitset of b and the 
            # bitset representing neighbors of a that are greater than b.
            
            # Create a mask for nodes in neighbors_a that are greater than b
            # Actually, we can just check the intersection of adj_bitset[b] and adj_bitset[a]
            # and find the smallest bit set that is > b.
            
            common = adj_bitset[a] & adj_bitset[b]
            if common:
                # Find the smallest bit set in common that is > b
                # Mask out bits <= b
                mask = ~((1 << (b + 1)) - 1)
                valid_c = common & mask
                if valid_c:
                    # Find the lowest set bit (LSB)
                    # In Python, (valid_c & -valid_c).bit_length() - 1 gives the index of LSB
                    c = (valid_c & -valid_c).bit_length() - 1
                    print(f"{a} {b} {c}")
                    return

if __name__ == "__main__":
    solve()