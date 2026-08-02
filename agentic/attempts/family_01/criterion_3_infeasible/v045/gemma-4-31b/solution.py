import sys

def solve():
    # Read n and m
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Use adjacency lists for iteration and adjacency matrix for O(1) lookup
    # Given n <= 2000, an adjacency matrix takes ~4 million bits/bytes, which fits in memory.
    adj_matrix = [0] * (n + 1)
    # Using bitsets (integers in Python) to speed up intersection and lookup
    # adj_matrix[i] will be a bitmask where the j-th bit is 1 if guild i and j are linked.
    # However, for lexicographical smallest (a, b, c), we need a structured search.
    
    adj_list = [[] for _ in range(n + 1)]
    
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        if u > v:
            u, v = v, u
        adj_list[u].append(v)
        
    # Sort adjacency lists to ensure we find the lexicographically smallest triple
    for i in range(1, n + 1):
        adj_list[i].sort()

    # To efficiently check if (b, c) is an edge, we use a set of edges or a bitset.
    # Since we need lexicographically smallest (a, b, c), we iterate a from 1 to n,
    # then b from a+1 to n, then c from b+1 to n.
    
    # Create a fast lookup for edges. 
    # Using a list of sets for O(1) average lookup.
    edge_set = [set() for _ in range(n + 1)]
    # We only need to store v in edge_set[u] where u < v
    # Re-process edges to fill the set
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx+1])
        idx += 2
        if u > v:
            u, v = v, u
        edge_set[u].add(v)

    # Lexicographical search:
    # Iterate a from 1 to n
    # Iterate b from adj_list[a] (which are all > a)
    # Iterate c from adj_list[b] (where c > b)
    # Check if c is also in adj_list[a]
    
    for a in range(1, n + 1):
        # Neighbors of a that are > a
        neighbors_a = adj_list[a]
        # We need to check if any two neighbors of a are connected to each other.
        # To maintain lexicographical order (a, b, c):
        # a is already the smallest.
        # We pick b from neighbors_a in increasing order.
        # Then we pick c from neighbors_a that are > b and connected to b.
        
        # For a fixed a and b, we want the smallest c > b such that (b, c) is an edge
        # AND (a, c) is an edge.
        # Since neighbors_a is sorted, we can iterate through it.
        
        for i in range(len(neighbors_a)):
            b = neighbors_a[i]
            # Now we look for c in neighbors_a such that c > b and (b, c) is an edge.
            # Since neighbors_a is sorted, any c = neighbors_a[j] for j > i will satisfy c > b.
            for j in range(i + 1, len(neighbors_a)):
                c = neighbors_a[j]
                # Check if (b, c) is an edge.
                # We stored edges as (small, large), so check edge_set[b] for c.
                if c in edge_set[b]:
                    print(f"{a} {b} {c}")
                    return

if __name__ == "__main__":
    solve()