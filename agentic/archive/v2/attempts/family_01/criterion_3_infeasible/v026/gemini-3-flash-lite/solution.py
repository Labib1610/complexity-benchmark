import sys

def solve():
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
        
    # Sort edges to ensure we check potential triples in lexicographical order
    # An edge is (a, b) with a < b. We look for c such that a < b < c.
    # The condition is a-b, a-c, b-c exist.
    # Since we want the lexicographically smallest (a, b, c),
    # we iterate through sorted edges (a, b) and check common neighbors c > b.
    
    edges.sort()
    
    # To optimize: convert sets to sorted lists for faster intersection
    adj_list = [sorted(list(s)) for s in adj]
    
    for a, b in edges:
        # We need a node c such that c > b, c in adj[a], and c in adj[b]
        # Since adj_list is sorted, we can find intersections efficiently
        set_a = adj[a]
        set_b = adj[b]
        
        # Iterate over the smaller adjacency list to find common neighbors
        if len(set_a) < len(set_b):
            candidates = [c for c in set_a if c > b]
            for c in candidates:
                if c in set_b:
                    print(f"{a} {b} {c}")
                    return
        else:
            candidates = [c for c in set_b if c > b]
            for c in candidates:
                if c in set_a:
                    print(f"{a} {b} {c}")
                    return

if __name__ == '__main__':
    solve()