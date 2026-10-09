import sys

def solve() -> None:
    data = sys.stdin.read().split()
    if not data:
        return
    it = iter(data)
    n = int(next(it))
    m = int(next(it))
    
    adj = [set() for _ in range(n + 1)]
    
    for _ in range(m):
        u = int(next(it))
        v = int(next(it))
        adj[u].add(v)
        adj[v].add(u)
    
    # Sort adjacency lists for deterministic iteration order
    adj_lists = [sorted(s) for s in adj]
    
    # Iterate to find the lexicographically smallest triangle
    for a in range(1, n + 1):
        neighbors_a = adj_lists[a]
        # Since we need a < b < c, we only consider neighbors b > a
        # and neighbors c > a. 
        # The intersection logic naturally handles b < c if we iterate properly.
        
        # Filter neighbors to only those > a
        valid_neighbors = [v for v in neighbors_a if v > a]
        
        len_vn = len(valid_neighbors)
        for i in range(len_vn):
            b = valid_neighbors[i]
            # We need c in adj[b] such that c > a and c is in adj[a]
            # Since valid_neighbors contains elements in adj[a] > a,
            # we just need to find common elements between adj[b] and valid_neighbors
            # that appear after index i (to ensure b < c).
            
            # Iterate through remaining valid neighbors to find c
            for j in range(i + 1, len_vn):
                c = valid_neighbors[j]
                if c in adj[b]:
                    print(a, b, c)
                    return

if __name__ == '__main__':
    solve()