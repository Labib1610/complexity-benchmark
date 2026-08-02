import sys

def solve():
    # Read n and m
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    m = int(input_data[1])
    
    # Use an adjacency set for fast lookups
    adj = [set() for _ in range(n + 1)]
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        adj[u].add(v)
        adj[v].add(u)
        idx += 2
        
    # To find the lexicographically smallest triplet (a, b, c) where a < b < c,
    # we iterate through possible values of a, then b, then c.
    # Since n <= 2000, an O(n * m) or O(n^2 * avg_degree) approach is feasible.
    
    # Sort adjacency lists to help with lexicographical order
    sorted_adj = [sorted(list(adj[i])) for i in range(n + 1)]
    
    for a in range(1, n + 1):
        # Candidates for b must be > a and connected to a
        neighbors_a = [x for x in sorted_adj[a] if x > a]
        for b in neighbors_a:
            # Candidates for c must be > b and connected to both a and b
            # We intersect neighbors of a and b that are > b
            neighbors_b = adj[b]
            for c in neighbors_a:
                if c > b and c in neighbors_b:
                    print(f"{a} {b} {c}")
                    return

if __name__ == '__main__':
    solve()