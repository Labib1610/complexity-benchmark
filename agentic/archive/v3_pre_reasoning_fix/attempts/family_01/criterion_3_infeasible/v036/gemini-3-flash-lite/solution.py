import sys

def solve():
    # Read n and m
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    n = int(input_data[0])
    m = int(input_data[1])
    
    adj = [set() for _ in range(n + 1)]
    edges = []
    idx = 2
    for _ in range(m):
        u = int(input_data[idx])
        v = int(input_data[idx + 1])
        idx += 2
        if u > v:
            u, v = v, u
        adj[u].add(v)
        edges.append((u, v))
    
    # We need to find the lexicographically smallest (a, b, c) with a < b < c
    # such that (a, b), (a, c), (b, c) are all edges.
    # To get the lexicographically smallest, we iterate through possible a, then b.
    
    # Sort edges to help with iteration
    edges.sort()
    
    # Store edges in a way that allows fast lookup
    # adj is already a list of sets
    
    # Iterate through each edge (a, b) as a candidate for the first two members
    # Since we need lexicographically smallest, we iterate a from 1 to n
    for a in range(1, n + 1):
        # Candidates for b are those connected to a
        neighbors_a = sorted(list(adj[a]))
        for i in range(len(neighbors_a)):
            b = neighbors_a[i]
            # Now we need c > b such that c is connected to both a and b
            # We want the smallest c, so we check neighbors of b that are also in neighbors_a
            # Since we want a < b < c, we only care about c > b
            
            # Intersection of neighbors_a and neighbors_b
            # To optimize, we can check smaller set
            if len(adj[a]) < len(adj[b]):
                candidates = adj[a]
                other = adj[b]
            else:
                candidates = adj[b]
                other = adj[a]
            
            # Find smallest c > b
            best_c = float('inf')
            found = False
            for c in candidates:
                if c > b and c in other:
                    if c < best_c:
                        best_c = c
                        found = True
            
            if found:
                print(f"{a} {b} {best_c}")
                return

if __name__ == '__main__':
    solve()