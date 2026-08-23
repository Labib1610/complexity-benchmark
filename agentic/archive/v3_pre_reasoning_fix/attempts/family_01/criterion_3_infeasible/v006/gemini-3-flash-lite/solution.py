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
        v = int(input_data[idx+1])
        if u > v:
            u, v = v, u
        adj[u].add(v)
        edges.append((u, v))
        idx += 2
        
    # Sort edges to ensure we check in lexicographical order (u, v)
    edges.sort()
    
    # We want the lexicographically smallest (a, b, c) with a < b < c.
    # A triple (a, b, c) is a clique of size 3 if b in adj[a], c in adj[a], c in adj[b].
    # To find the smallest lexicographical triple, we iterate through all edges (a, b)
    # and look for a common neighbor c such that c > b.
    # By iterating edges (a, b) in sorted order, the first valid c we find 
    # for the smallest (a, b) will give the smallest (a, b, c).
    
    for a, b in edges:
        # We need c > b such that c is in adj[a] and c is in adj[b]
        # To get the lexicographically smallest, we check neighbors of a
        # that are also in b's set.
        common = adj[a].intersection(adj[b])
        
        candidates = [c for c in common if c > b]
        if candidates:
            c = min(candidates)
            print(f"{a} {b} {c}")
            return

if __name__ == '__main__':
    solve()