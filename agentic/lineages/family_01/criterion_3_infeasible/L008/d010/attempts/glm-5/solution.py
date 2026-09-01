import sys

def main():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    
    adj = [set() for _ in range(n + 1)]
    edges = []
    for _ in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        if u > v:
            u, v = v, u
        adj[u].add(v)
        adj[v].add(u)
        edges.append((u, v))
    
    best = None
    
    for a, b in edges:
        common = adj[a] & adj[b]
        for c in common:
            if c > b:
                # Check no common neighbor of all three (excluding a, b, c)
                # Iterate over smallest adjacency list
                if len(adj[a]) <= len(adj[b]) and len(adj[a]) <= len(adj[c]):
                    smallest, other1, other2 = adj[a], adj[b], adj[c]
                elif len(adj[b]) <= len(adj[c]):
                    smallest, other1, other2 = adj[b], adj[a], adj[c]
                else:
                    smallest, other1, other2 = adj[c], adj[a], adj[b]
                
                ok = True
                for w in smallest:
                    if w != a and w != b and w != c and w in other1 and w in other2:
                        ok = False
                        break
                
                if ok:
                    if best is None or (a, b, c) < best:
                        best = (a, b, c)
    
    print(f"{best[0]} {best[1]} {best[2]}")

main()