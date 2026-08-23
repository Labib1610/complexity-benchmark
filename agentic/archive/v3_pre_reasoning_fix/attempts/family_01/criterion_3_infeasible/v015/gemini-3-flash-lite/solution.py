import sys

def solve():
    # Use fast I/O
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
        v = int(input_data[idx+1])
        if u > v:
            u, v = v, u
        adj[u].add(v)
        edges.append((u, v))
        idx += 2
        
    # Sort edges to help find the lexicographically smallest triple
    # A triple (a, b, c) with a < b < c is smallest if 'a' is minimal,
    # then 'b' is minimal, then 'c' is minimal.
    # We can iterate through 'a' from 1 to n.
    
    for a in range(1, n + 1):
        neighbors = sorted(list(adj[a]))
        # For a fixed 'a', we look for b, c in neighbors such that b < c and c in adj[b]
        # To minimize (a, b, c), we pick the smallest possible 'b' from neighbors,
        # then the smallest possible 'c' from (neighbors intersected with adj[b]).
        
        for i in range(len(neighbors)):
            b = neighbors[i]
            # We only care about b > a (already guaranteed by sorted neighbors)
            # Find common neighbors of a and b
            common = adj[a].intersection(adj[b])
            if common:
                c = min(common)
                # Since we iterate 'a' and 'b' in increasing order, the first
                # triple we find is the lexicographically smallest.
                print(f"{a} {b} {c}")
                return

if __name__ == '__main__':
    solve()