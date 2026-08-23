import sys
from collections import defaultdict

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    n = int(data[0])
    m = int(data[1])
    
    edges = []
    adj = [set() for _ in range(n + 1)]
    
    index = 2
    for _ in range(m):
        u = int(data[index])
        v = int(data[index + 1])
        index += 2
        if u > v:
            u, v = v, u
        edges.append((u, v))
        adj[u].add(v)
        adj[v].add(u)
    
    # Sort adjacency lists for consistent ordering
    for i in range(1, n + 1):
        adj[i] = sorted(adj[i])
    
    # For each edge (u,v), check neighbors of u and v to find a common neighbor
    # We want the triad (a,b,c) with a<b<c and (a,b), (a,c), (b,c) all present
    
    # To ensure we get the lexicographically smallest triad, we'll iterate over
    # edges in lexicographical order and for each edge, look for the smallest
    # possible third node that connects to both endpoints.
    
    edges.sort()
    
    best_triad = None
    
    for u, v in edges:
        if u >= v:
            continue
        # Find common neighbors of u and v
        # Iterate through neighbors of u and check if they are also neighbors of v
        # Since we want a < b < c, and we have u < v, we set a=u, b=v, and search for c > v
        # Or we could have a=u, and search for b and c such that u < b < c
        # Actually, let's think differently:
        # A triad is three nodes a<b<c with edges (a,b), (a,c), (b,c)
        # So given an edge (u,v) with u<v, it can be (a,b) with a=u,b=v,
        # and we need to find c > v such that (u,c) and (v,c) exist.
        
        # Alternatively, (u,v) could be (a,c) with a=u, c=v, so b is between u and v
        # Or (u,v) could be (b,c) with b=u, c=v, so a < u
        
        # Let's consider all three cases:
        
        # Case 1: u=a, v=b, find c > v such that (a,c) and (b,c) exist
        if u < v:
            for c in adj[v]:
                if c > v and c in adj[u]:
                    triad = (u, v, c)
                    if best_triad is None or triad < best_triad:
                        best_triad = triad
                        break  # Since adj lists are sorted, first match is smallest c
        
        # Case 2: u=a, v=c, so b is between u and v, i.e., u < b < v
        # Check for such b where (u,b) and (b,v) exist
        if u < v:
            for b in adj[u]:
                if u < b < v and v in adj[b]:
                    triad = (u, b, v)
                    if best_triad is None or triad < best_triad:
                        best_triad = triad
                        break  # First such b due to sorted order gives minimal triad
        
        # Case 3: u=b, v=c, so a < u, i.e., a < u < v
        # Check for such a where (a,u) and (a,v) exist
        if u < v:
            for a in adj[u]:
                if a < u and v in adj[a]:
                    triad = (a, u, v)
                    if best_triad is None or triad < best_triad:
                        best_triad = triad
                        break  # First such a due to sorted order gives minimal triad
    
    if best_triad:
        print(best_triad[0], best_triad[1], best_triad[2])
    else:
        # Fallback - should not happen per problem statement
        pass

if __name__ == "__main__":
    main()