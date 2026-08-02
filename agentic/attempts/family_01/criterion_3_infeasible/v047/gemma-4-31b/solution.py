import sys

def solve():
    # Use fast I/O
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Adjacency list using sets for O(1) lookup
    adj = [set() for _ in range(n + 1)]
    # To ensure lexicographical smallest, we iterate through vertices in increasing order.
    # We only need to store edges (u, v) where u < v to simplify the search.
    edges_list = []
    
    ptr = 2
    for _ in range(m):
        u = int(input_data[ptr])
        v = int(input_data[ptr+1])
        ptr += 2
        if u > v:
            u, v = v, u
        adj[u].add(v)
        edges_list.append((u, v))

    # To find the lexicographically smallest (a, b, c) with a < b < c:
    # We iterate a from 1 to n.
    # For a fixed a, we look for pairs (b, c) such that a < b < c and (a,b), (a,c), (b,c) are edges.
    # To minimize b and then c, we can iterate through all neighbors of a that are > a.
    
    # Pre-sort neighbors for each node to ensure we check b in increasing order.
    sorted_adj = [sorted(list(adj[i])) for i in range(n + 1)]
    
    # To speed up the check for (b, c), we can use the set adj[b]
    # Note: adj[b] only contains neighbors > b.
    
    for a in range(1, n + 1):
        neighbors_a = sorted_adj[a]
        # We need to find b, c in neighbors_a such that b < c and (b, c) is an edge.
        # Since neighbors_a is sorted, iterating b and c in order will find the smallest.
        for i in range(len(neighbors_a)):
            b = neighbors_a[i]
            for j in range(i + 1, len(neighbors_a)):
                c = neighbors_a[j]
                # Check if (b, c) is an edge. Since b < c, we check adj[b].
                if c in adj[b]:
                    print(f"{a} {b} {c}")
                    return

if __name__ == "__main__":
    solve()