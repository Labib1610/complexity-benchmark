import sys

def solve():
    input_data = sys.stdin.buffer.read().split()
    idx = 0
    n = int(input_data[idx]); idx += 1
    m = int(input_data[idx]); idx += 1
    
    adj = [0] * (n + 1)
    edges = []
    
    for _ in range(m):
        u = int(input_data[idx]); idx += 1
        v = int(input_data[idx]); idx += 1
        adj[u] |= (1 << v)
        adj[v] |= (1 << u)
        if u < v:
            edges.append((u, v))
        else:
            edges.append((v, u))
    
    # Sort edges by (u, v)
    edges.sort()
    
    best = None
    
    for u, v in edges:
        # Find common neighbors > v
        common = adj[u] & adj[v]
        # Mask out vertices <= v
        mask = ~((1 << (v + 1)) - 1)
        common &= mask
        
        if common:
            # Find lowest set bit
            c = (common & -common).bit_length() - 1
            candidate = (u, v, c)
            if best is None or candidate < best:
                best = candidate
                # Since edges are sorted, first found is smallest (u,v)
                # But c might not be smallest possible for this (u,v)... 
                # Actually we want smallest c > v, which is what we found
                # And since we process edges in order, first triangle is answer
                print(f"{u} {v} {c}")
                return
    
    # Shouldn't reach here per problem statement
    if best:
        print(f"{best[0]} {best[1]} {best[2]}")

solve()